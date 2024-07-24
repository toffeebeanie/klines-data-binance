# klines-data-binance

FOREWORD - disclaimers on data and where it comes from
- BTCUSDT.csv: 1 minute OHLCV data from 17 Aug 2017 to 24 Jul 2024. Downloaded from https://www.cryptoarchive.com.au/asset/BTC. FAQ on this source: https://www.cryptoarchive.com.au/faq
- BTCUSDT_4H.csv: 4 hourly OHLCV data, aggregated programatically (Python). May differ slightly from CEX data (Exchange-Specific Factors: Binance may use specific algorithms or methods to calculate their OHLCV data, such as handling order book depth, internal transactions, or other market activities that might not be captured in publicly available 1-minute data.)
- BTCUSDT_4H_BN.csv: 4 hourly OHLCV perps data, extracted from Binance (USDT-M). Source: https://data.binance.vision/?prefix=data/futures/
