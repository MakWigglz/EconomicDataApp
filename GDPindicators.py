import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import io
import base64
from flask import Flask, render_template, jsonify

app = Flask(__name__)

# Mock data for GDP indicators (10 years of data)
years = range(2014, 2024)
gdp_indicators = {
    'GDP Growth Rate': np.random.uniform(1, 4, 10),
    'Industrial Production Index': np.random.uniform(95, 110, 10),
    'Consumer Demand Index': np.random.uniform(90, 105, 10),
    'Purchasing Managers Index': np.random.uniform(48, 55, 10),
    'Consumer Price Index': np.random.uniform(225, 260, 10),
    'Unemployment Rate': np.random.uniform(3, 6, 10),
    'Retail Sales Growth': np.random.uniform(-1, 5, 10),
    'Business Confidence Index': np.random.uniform(95, 105, 10),
    'Capacity Utilization Rate': np.random.uniform(75, 85, 10),
    'Government Debt to GDP': np.random.uniform(100, 110, 10)
}

# Mock data for stock market parameters
stock_market_data = {
    'NASDAQ Composite': np.random.uniform(8000, 15000, 10),
    'Dow Jones Industrial Average': np.random.uniform(25000, 35000, 10),
    'S&P 500': np.random.uniform(3000, 4500, 10),
    'Apple (AAPL)': np.random.uniform(100, 180, 10),
    'Microsoft (MSFT)': np.random.uniform(150, 300, 10),
    'Amazon (AMZN)': np.random.uniform(2000, 3500, 10),
    'Google (GOOGL)': np.random.uniform(1500, 2800, 10),
    'Facebook (FB)': np.random.uniform(200, 350, 10),
    'Tesla (TSLA)': np.random.uniform(200, 900, 10),
    'JPMorgan Chase (JPM)': np.random.uniform(100, 170, 10)
}

# Combine all data
all_data = {**gdp_indicators, **stock_market_data}
df = pd.DataFrame(all_data, index=years)

def create_plot(data, title):
    plt.figure(figsize=(10, 6))
    plt.plot(data.index, data.values, marker='o')
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

@app.route('/')
def index():
    return render_template('dashboard.html', indicators=list(all_data.keys()))

@app.route('/data/<indicator>')
def get_data(indicator):
    plot_url = create_plot(df[indicator], indicator)
    return jsonify({'plot_url': plot_url, 'data': df[indicator].to_dict()})

if __name__ == '__main__':
    app.run(debug=True)