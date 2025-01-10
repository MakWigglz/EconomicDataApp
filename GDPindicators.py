import yfinance as yf  # For stock market data
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# GDP Components (Simplified - Requires external data source for accurate values)
# In reality, you would fetch this from a reliable source like the BEA (Bureau of Economic Analysis)
# For demonstration, we'll use placeholder data for the past decade (2014-2023)
years = range(2014, 2024)
consumption = [12, 12.5, 13, 13.8, 14.5, 15, 15.8, 16.5, 17.2, 18] # Trillion USD (Placeholder)
investment = [3, 3.2, 3.5, 3.8, 4, 4.3, 4.6, 4.9, 5.2, 5.5] # Trillion USD (Placeholder)
government = [3.5, 3.6, 3.7, 3.9, 4.1, 4.3, 4.5, 4.7, 4.9, 5.1] # Trillion USD (Placeholder)
net_exports = [-0.5, -0.6, -0.7, -0.8, -0.9, -1, -1.1, -1.2, -1.3, -1.4] # Trillion USD (Placeholder)

gdp_data = pd.DataFrame({
    'Year': years,
    'Consumption': consumption,
    'Investment': investment,
    'Government': government,
    'Net Exports': net_exports
})

gdp_data['GDP'] = gdp_data['Consumption'] + gdp_data['Investment'] + gdp_data['Government'] + gdp_data['Net Exports']

# Stock Market Data (Example: Apple, Microsoft, Amazon)
tickers = ["AAPL", "MSFT", "AMZN"]
stock_data = yf.download(tickers, period="10y") # Download last 10 years of data

# Basic Stock Analysis (Example: Closing Price Trend)
plt.figure(figsize=(12, 6))
for ticker in tickers:
    plt.plot(stock_data['Close'][ticker], label=ticker)
plt.title("Stock Closing Prices (Last 10 Years)")
plt.xlabel("Date")
plt.ylabel("Price (USD)")
plt.legend()
plt.show()

# GDP Growth Rate Calculation:
gdp_data['GDP Growth Rate'] = gdp_data['GDP'].pct_change() * 100

# GDP Visualization
plt.figure(figsize=(10, 6))
plt.plot(gdp_data['Year'], gdp_data['GDP'], marker='o')
plt.title('US GDP (2014-2023)')
plt.xlabel('Year')
plt.ylabel('GDP (Trillion USD)')
plt.grid(True)
plt.show()

print(gdp_data)

# Example: Sector Analysis (Using a hypothetical sector classification)
# You would need to map companies to sectors in a real application
sector_data = {
    "AAPL": "Technology",
    "MSFT": "Technology",
    "AMZN": "Consumer Discretionary"
}

# Further analysis and projections would require more sophisticated techniques
# such as time series analysis (ARIMA, etc.) and econometric models.
