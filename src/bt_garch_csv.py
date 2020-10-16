import backtrader as bt
import pandas as pd
import psycopg2
from sqlalchemy import create_engine
from garch_strategy4 import GARCH_strategybands
from print_ta import print_ta
import matplotlib.pyplot as plt

# Main function
if __name__ == '__main__':
	# Start cerebro object
	cerebro = bt.Cerebro()

	# Add strategy
	cerebro.addstrategy(GARCH_strategybands)

	df = pd.read_csv('bitcoin.csv')
	# Clean data
	df = df[['time', 'open', 'high', 'low', 'close', 'volume']]
	df.columns = ['Date', 'Open', 'High', 'Low', 'Close', 'Volume']
	df.set_index('Date', inplace=True)
	# Create datafeed object
	data = bt.feeds.PandasData(dataname=df)
	# Add data to cerebro
	cerebro.adddata(data)

	# Set start cash
	cerebro.broker.setcash(10000)

	# Set broket commission - 0.1%
	cerebro.broker.setcommission(commission=.001)

	# Analyzer
	cerebro.addanalyzer(bt.analyzers.TradeAnalyzer, _name='trade_anal')

	print('Portfolio start value: {:.2f}'.format(
		cerebro.broker.getvalue()
		))

	# Run everything
	thestrats = cerebro.run()
	thestrat = thestrats[0]

	# Print analizer report
	analysis = thestrat.analyzers.trade_anal.get_analysis()

	print_ta(analysis)

	print('Final portfolio value: {:.2f}'.format(
		cerebro.broker.getvalue()
		))

	# Plot
	cerebro.plot()