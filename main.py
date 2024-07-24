import pandas as pd

# Load data from CSV
df = pd.read_csv('BTCUSDT.csv', delimiter='|', header=None, names=[
    'open_timestamp', 'open', 'high', 'low', 'close', 'volume',
    'taker_buy_quote_asset_volume', 'taker_buy_base_asset_volume',
    'quote_asset_volume', 'number_of_trades'])

# Convert the timestamp to datetime format
df['open_timestamp'] = pd.to_datetime(df['open_timestamp'], unit='s')

# Set the timestamp as the index
df.set_index('open_timestamp', inplace=True)

# Resample the data to 4-hour intervals
resampled_df = df.resample('4H').agg({
    'open': 'first',
    'high': 'max',
    'low': 'min',
    'close': 'last',
    'volume': 'sum',
    'taker_buy_quote_asset_volume': 'sum',
    'taker_buy_base_asset_volume': 'sum',
    'quote_asset_volume': 'sum',
    'number_of_trades': 'sum'
})

# Reset the index to have the timestamp as a column again
resampled_df.reset_index(inplace=True)

# Save the resampled data to a new CSV file
resampled_df.to_csv('BTCUSDT_4H.csv', index=False)
