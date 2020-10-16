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
		self.positionprice = {}
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

				if not self.positionprice.get(order.tradeid):
					self.positionprice[order.tradeid] = order.executed.price

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

				if not self.positionprice.get(order.tradeid):
					self.positionprice[order.tradeid] = order.executed.price

				self.paidcomm.append(order.executed.comm)

			# It'll tell when the order was executed
			self.bar_executed = len(self)

		elif order.status in [order.Canceled, order.Margin, order.Rejected]:
			self.log('Order Canceled/Margin/Rejected')

		# Erase order status
		del self.order[order.tradeid]

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
		self.log('Close, {:.2f}, Position size, {}'.format(
			self.dataclose[0],
			self.position.size
			))

		# A order is pending
		if len(self.order) > 0:
			return

		if self.position:
			# Long position
			if self.position.size > 0:
				if self.dataclose[0] >= (self.atr[0] * self.volmult) + self.positionprice[self.curtradeid]:
					# Close order
					self.log('CLOSE LONG {:.2f}, TrID {}'.format(
						self.dataclose[0],
						self.curtradeid
						))
					
					self.order[self.curtradeid] = self.close(
						tradeid=self.curtradeid
						)

					self.curtradeid = next(self.tradeid)

					return
					
			# Short position
			elif self.position.size < 0:
				if self.dataclose[0] <= (self.atr[0] * self.volmult) - self.positionprice[self.curtradeid]:
					# Close order
					self.log('CLOSE SHORT {:.2f}, TrID {}'.format(
						self.dataclose[0],
						self.curtradeid
						))
					
					self.order[self.curtradeid] = self.close(
						tradeid=self.curtradeid
						)

					self.curtradeid = next(self.tradeid)

					return

		# Open long
		if self.dataclose[0] < self.garch.neg_b[-1] * (1 - self.band_width):			
			if self.position.size < 0:
				# Close order
					self.log('CLOSE SHORT {:.2f}, TrID {}'.format(
						self.dataclose[0],
						self.curtradeid
						))
					
					self.order[self.curtradeid] = self.close(
						tradeid=self.curtradeid
						)

					self.curtradeid = next(self.tradeid)

			# Log order
			self.log('BUY CREATE {:.2f}, TrID {}'.format(
				self.dataclose[0],
				self.curtradeid
				))

			# Create position
			self.order[self.curtradeid] = self.buy(
				size=self.stake, 
				tradeid=self.curtradeid
				)

		# Open short
		elif self.dataclose[0] > self.garch.pos_b[-1] * (1 + self.band_width):
			if self.position.size > 0:
				# Close order
				self.log('CLOSE LONG {:.2f}, TrID {}'.format(
					self.dataclose[0],
					self.curtradeid
					))
				
				self.order[self.curtradeid] = self.close(
					tradeid=self.curtradeid
					)

				self.curtradeid = next(self.tradeid)

			# Log order
			self.log('SELL CREATE {:.2f}, TrID {}'.format(
				self.dataclose[0],
				self.curtradeid
				))

			# Create position
			self.order[self.curtradeid] = self.sell(
				size=self.stake, 
				tradeid=self.curtradeid
				)