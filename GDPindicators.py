import sqlite3
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import io
import base64
from flask import Flask, render_template, jsonify

app = Flask(__name__)

# Database setup
def init_db():
    conn = sqlite3.connect('economic_data.db')
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS indicators
                 (year INTEGER, indicator TEXT, value REAL)''')
    conn.commit()
    return conn

def populate_db(conn):
    c = conn.cursor()
    indicators = ['GDP Growth Rate', 'Industrial Production Index', 'Consumer Demand Index',
                  'Purchasing Managers Index', 'Consumer Price Index', 'Unemployment Rate',
                  'Retail Sales Growth', 'Business Confidence Index', 'Capacity Utilization Rate',
                  'Government Debt to GDP']
    years = range(2014, 2024)
    for indicator in indicators:
        for year in years:
            value = np.random.uniform(0, 100)  # Replace with real data in production
            c.execute("INSERT INTO indicators VALUES (?, ?, ?)", (year, indicator, value))
    conn.commit()

# Initialize and populate the database
conn = init_db()
populate_db(conn)

@app.route('/')
def index():
    c = conn.cursor()
    c.execute("SELECT DISTINCT indicator FROM indicators")
    indicators = [row[0] for row in c.fetchall()]
    return render_template('dashboard.html', indicators=indicators)

def create_plot(data, title):
    plt.figure(figsize=(10, 6))
    plt.plot(data['year'], data['value'], marker='o')
    plt.title(title)
    plt.xlabel('Year')
    plt.ylabel('Value')
    plt.grid(True)
    
    img = io.BytesIO()
    plt.savefig(img, format='png')
    img.seek(0)
    plot_url = base64.b64encode(img.getvalue()).decode()
    plt.close()
    
    return plot_url

@app.route('/data/<indicator>')
def get_data(indicator):
    c = conn.cursor()
    c.execute("SELECT year, value FROM indicators WHERE indicator=? ORDER BY year", (indicator,))
    data = pd.DataFrame(c.fetchall(), columns=['year', 'value'])
    plot_url = create_plot(data, indicator)
    return jsonify({'plot_url': plot_url, 'data': data.to_dict()})

if __name__ == '__main__':
    app.run(debug=True)