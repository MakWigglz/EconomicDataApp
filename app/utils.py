import sqlite3
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import io
import base64

def init_db():
    conn = sqlite3.connect('economic_data.db')
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS indicators
                 (year INTEGER, indicator TEXT, value REAL)''')
    conn.commit()
    return conn

def populate_db(conn):
    # ... (same as before)

def get_indicators():
    conn = init_db()
    c = conn.cursor()
    c.execute("SELECT DISTINCT indicator FROM indicators")
    indicators = [row[0] for row in c.fetchall()]
    conn.close()
    return indicators

def get_indicator_data(indicator):
    conn = init_db()
    c = conn.cursor()
    c.execute("SELECT year, value FROM indicators WHERE indicator=? ORDER BY year", (indicator,))
    data = pd.DataFrame(c.fetchall(), columns=['year', 'value'])
    conn.close()
    return data

def create_plot(data, title):
    # ... (same as before)