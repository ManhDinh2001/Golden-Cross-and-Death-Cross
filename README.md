# Stock Analysis
## Date Set

The dataset provided here has been extracted from the investing.com website. The Stock price data provided is from 02/01/2020 to 18/04/2023 for six stocks: MWG, MSN, HPG, HSG, EIB, SSI

Please note that for the days where it is not possible to calculate the required Moving Averages, it is better to ignore these rows rather than trying to deal with NULL by filling it with average value as that would make no practical sense.

Create a new schema named 'Assignment' Import the CSV files in SQL Server, naming the tables as the name of the stocks.

## Results Expected

1. Create buy and sell signals using the Golden Cross and Death Cross strategies in Jupyter Notebook using Python, along with visualization of the signals on a stock chart.

2. The 'Signal' represents the buy/sell signal based on the Golden Cross and Death Cross strategy. If the 50-day moving average is greater than the 200-day moving average, the signal is buy signal, otherwise it's sell signal.
