import backtrader as bt
import pandas as pd
import psycopg2
from sqlalchemy import create_engine
from garch_strategy import GARCH_strategybands
import matplotlib.pyplot as plt
import os

def data_db(table):
        ''' Add data from DB server '''
        
        # Info to connect to db
        # Open from credentials file
        f = open('credentials', 'r')
        f.readline()
        db_name = f.readline()[:-1]
        user_name = f.readline()[:-1]
        user_pw = f.readline()[:-1]
        host = f.readline()[:-1]
        port = f.readline()
        
        # Close file
        f.close()
        
        # Create engine to connect
        engine = create_engine(
                'postgresql://{u}:{pw}@{h}:{p}/{db}'.format(
                        u=user_name,
                        pw=user_pw,
                        p=port,
                        db=db_name,
                        h=host
                        ))
        
        # Query data as df
        df = pd.read_sql(
                'SELECT * FROM {}'.format(table), 
                engine
                )         
        
        return df
        
def data_csv(relative_path):
        ''' Add data from csv file '''
        
        # Get fullpath to file  
        fullpath = os.path.join(os.path.abspath(os.path.dirname(__file__)), relative_path)
        # Open csv
        df = pd.read_csv(fullpath)

        return df

# Main function
if __name__ == '__main__':
        # Start cerebro object
        cerebro = bt.Cerebro()

        # Add strategy
        cerebro.addstrategy(GARCH_strategybands)

        # Open data (0 to  csv and 1 to sql server)
        open_data_mode = 0
        if open_data_mode == 0:
                df = data_csv('../data/bitcoin.csv')
        elif open_data_mode == 1:
                df = data_db('bitcoin.csv')
        
        # Clean data
        df = df[['time', 'open', 'high', 'low', 'close', 'volume']]
        df.columns = ['Date', 'Open', 'High', 'Low', 'Close', 'Volume']
        df['Date'] = pd.to_datetime(df['Date'])
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

        print('Final portfolio value: {:.2f}'.format(
                cerebro.broker.getvalue()
                ))

        # Plot
        cerebro.plot()
