import pandas as pd

# Load the aggregated data
df = pd.read_csv('BTCUSDT_4H.csv')

# Check for missing values
missing_data = df.isnull().sum()
print("Missing data in each column:\n", missing_data)

# Check for datetime consistency
df['open_timestamp'] = pd.to_datetime(df['open_timestamp'])
if not df['open_timestamp'].is_monotonic_increasing:
    print("Timestamps are not in order!")

# Check for value consistency
value_consistency_issues = df[
    (df['high'] < df['low']) |
    (df['open'] > df['high']) |
    (df['close'] > df['high']) |
    (df['open'] < df['low']) |
    (df['close'] < df['low'])
]

if not value_consistency_issues.empty:
    print("Value consistency issues found in the following rows:\n", value_consistency_issues)

# Check for non-negative values
non_negative_issues = df[
    (df['volume'] < 0) |
    (df['taker_buy_quote_asset_volume'] < 0) |
    (df['taker_buy_base_asset_volume'] < 0) |
    (df['quote_asset_volume'] < 0) |
    (df['number_of_trades'] < 0)
]

if not non_negative_issues.empty:
    print("Negative values found in the following rows:\n", non_negative_issues)

print("Data validation completed.")
