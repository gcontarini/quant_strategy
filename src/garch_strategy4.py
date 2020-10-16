import backtrader as bt
import itertools
from garch_rollbands import GARCH_rollingbands

class GARCH_strategybands(bt.Strategy):
	'''Multitrade strategy implementation using garch 
	rolling window forecast for backtrader. Exit rule based in
	volatility.
	
	Args:
		None
	
	Returns:
		None
	'''
	
	# To log close price with dates
	def log(self, txt, dt=None):
		dt = dt or self.datas[0].datetime.date(0)
		print('{}, {}'.format(dt.isoformat(), txt))

	def __init__(self):
		# To track the last close price
		self.dataclose = self.datas[0].close

		# How much to buy/sell in each order
		self.stake = 0.01
		# How much volatility
		self.volmult = 2
		# Width of garch band in decimals (less than 1)
		self.band_width = .001

		# To track order position status
		self.order = {}
		self.paidcomm = []

		# Track multiple orders
		self.tradeid = itertools.cycle([i for i in range(9000)])
		self.curtradeid = next(self.tradeid)

		# Indicators
		self.garch = GARCH_rollingbands(period=30, p_arch=1, q_arch=1)
		self.atr = bt.indicators.ATR(self.data, period=30)

	# Info about order status
	def notify_order(self, order):
		# Check status order
		if order.status in [order.Submitted, order.Accepted]:
			# Order has been submetted to broker - do nothing
			return

		# Check if order has been completed
		if order.status in [order.Completed]:
			# Print order buy price
			if order.isbuy():
				self.log(
					'BUY EXECUTED, Price {:.2f}, Cost {:.2f}, Comm {:.2f}, TrID {}'.format(
						order.executed.price,
						order.executed.value,
						order.executed.comm,
						order.tradeid
						))

				self.paidcomm.append(order.executed.comm)
			
			# Print order sell price
			elif order.issell():
				self.log(
					'SELL EXECUTED, Price {:.2f}, Cost {:.2f}, Comm {:.2f}, TrID {}'.format(
						order.executed.price,
						order.executed.value,
						order.executed.comm,
						order.tradeid
						))

				self.paidcomm.append(order.executed.comm)

			# It'll tell when the order was executed
			self.bar_executed = len(self)

		elif order.status in [order.Canceled, order.Margin, order.Rejected]:
			# Don't log if order is limit or stop
			if order.ref == self.order[order.tradeid][1].ref:
				return
			
			elif order.ref == self.order[order.tradeid][2].ref:
				return
			
			else:
				self.log('Order Canceled/Margin/Rejected')

		# Erase order status
		self.order[order.tradeid][0] = None

	# Info about trade, profit etc
	def notify_trade(self, trade):
		# Report profit per trade
		if trade.isclosed:
			self.log(
				'OPERATION PROFIT, GROSS {:.2f}, NET {:.2f}, TrID {}'.format(
					trade.pnl,
					trade.pnlcomm,
					trade.tradeid
					))

	# Where really the strategy happens
	def next(self):
		# Print current price
		self.log('Close, {:.2f}, PoSize, {}'.format(
			self.dataclose[0],
			self.position.size
			))

		# A order is pending
		if self.order.get(self.curtradeid):
			if self.order[self.curtradeid][0]:
				return			

		# Open long
		if self.dataclose[0] < self.garch.neg_b[-1] * (1 - self.band_width):
			# Log order
			self.log('BUY CREATE {:.2f}, TrID {}'.format(
				self.dataclose[0],
				self.curtradeid
				))

			limit = (self.atr[0] * self.volmult) + self.dataclose[0]
			stop = (self.atr[0] * self.volmult) - self.dataclose[0]
			price = self.dataclose[0]
			
			# Create position
			self.order[self.curtradeid] = self.buy_bracket(
				size=self.stake,
				limitprice=limit,
				stopprice=stop,
				exectype=bt.Order.Market,
				stopexec=bt.Order.Stop, 
				tradeid=self.curtradeid
				)

			self.curtradeid = next(self.tradeid)

		# Open short
		elif self.dataclose[0] > self.garch.pos_b[-1] * (1 + self.band_width):
			# Log order
			self.log('SELL CREATE {:.2f}, TrID {}'.format(
				self.dataclose[0],
				self.curtradeid
				))

			limit = (self.atr[0] * self.volmult) - self.dataclose[0]
			stop = (self.atr[0] * self.volmult) + self.dataclose[0]
			price = self.dataclose[0]
			
			# Create position
			self.order[self.curtradeid] = self.sell_bracket(
				size=self.stake,
				limitprice=limit,
				stopprice=stop,
				exectype=bt.Order.Market,
				stopexec=bt.Order.Stop, 
				tradeid=self.curtradeid
				)

			self.curtradeid = next(self.tradeid)