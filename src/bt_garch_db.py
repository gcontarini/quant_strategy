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

	# Add data from SQL -> Pandas -> Datafeed
	# Info to connect to db
	# Open from credentials file
	f = open('credentials', 'r')
	f.readline()
	db_name = f.readline()[:-1]
	user_name = f.readline()[:-1]
	user_pw = f.readline()[:-1]
	port = f.readline()
	# Close file
	f.close()
	# Create engine to connect
	engine = create_engine(
		'postgresql://{u}:{pw}@localhost:{p}/{db}'.format(
			u=user_name,
			pw=user_pw,
			p=port,
			db=db_name
			))
	# Query data as df
	df = pd.read_sql(
		'SELECT * FROM bitcoin', 
		engine
		)
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