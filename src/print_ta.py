def print_ta(analysis):
	'''
	Print Trade Analyzer report in a nice format.
	
	------------
	Args:
		TradeAnalyzer.get_analysis() object
	
	------------
	Returns:
		None
	'''
	# print('+' * 30)
	# print('{:*^30}'.format('Trade Analyzer Report'))
	# print('-' * 30)
	# print('{:^30}'.format('Total Open/Closed trades'))
	# print('{:^25} {}'.format('Total:', analysis['total']['total']))
	# print('{:<15} {:>15}'.format(
	# 	'Open',  
	# 	'Close',
	# 	))
	# print('{:<15} {:>15}'.format( 
	# 	analysis['total']['open'],
	# 	analysis['total']['closed']
	# 	))
	# print('-' * 30)
	# print('{:^30}'.format('Streak'))
	# print('{:<15} {:>15}'.format(
	# 	'Longest won', 
	# 	'Longest lose'
	# 	))
	# print('{:<15} {:>15}'.format(
	# 	analysis['streak']['won']['longest'], 
	# 	analysis['streak']['lost']['longest']
	# 	))
	# print('-' * 30)
	# print('{:^30}'.format('ProfitNLoss General'))
	# print('{:<15} {:>15}'.format('Gross:', 'Net:'))
	# print('{:<15} {} {:>15} {}'.format(
	# 	'Tot',
	# 	analysis['pnl']['gross']['total'],
	# 	'Tot',
	# 	analysis['pnl']['net']['total']
	# 	))
	# print('{:<15} {} {:>15} {}'.format(
	# 	'Avg',
	# 	analysis['pnl']['gross']['average'],
	# 	'Avg',
	# 	analysis['pnl']['net']['average']
	# 	))
	# print('-' * 30)
	# print('{:^30}'.format('Win Stats'))
	# print('{:<15} {:>15}'.format('Total:', 'PNL:'))
	# print('{:<15} {:>15} {}'.format(
	# 	analysis['won']['total'],
	# 	'Tot',
	# 	analysis['won']['pnl']['total']
	# 	))
	# print('{:>30} {}'.format(
	# 	'Avg', 
	# 	analysis['won']['pnl']['average']
	# 	))
	# print('{:>30} {}'.format(
	# 	'Max', 
	# 	analysis['won']['pnl']['max']
	# 	))
	# print('-' * 30)
	# print('{:^30}'.format('Lose Stats'))
	# print('{:<15} {:>15}'.format('Total:', 'PNL:'))
	# print('{:<15} {:>15} {}'.format(
	# 	analysis['lost']['total'],
	# 	'Tot',
	# 	analysis['lost']['pnl']['total']
	# 	))
	# print('{:>30} {}'.format(
	# 	'Avg', 
	# 	analysis['lost']['pnl']['average']
	# 	))
	# print('{:>30} {}'.format(
	# 	'Max', 
	# 	analysis['lost']['pnl']['max']
	# 	))
	# print('-' * 30)
	# print('Long Stats')
	# print('  Total: {}'.format(analysis['long']['total']))
	# print('  Won: {}'.format(analysis['long']['won']))
	# print('  Lost: {}'.format(analysis['long']['lost']))
	# print('  PNL: ')
	# print('    Total: {}'.format(analysis['long']['pnl']['total']))
	# print('    Average: {}'.format(analysis['long']['pnl']['average']))
	# print('    Won: ')
	# print('      Total: {}'.format(analysis['long']['pnl']['won']['total']))
	# print('      Average: {}'.format(analysis['long']['pnl']['won']['average']))
	# print('      Max: {}'.format(analysis['long']['pnl']['won']['max']))
	# print('    Lost: ')
	# print('      Total: {}'.format(analysis['long']['pnl']['lost']['total']))
	# print('      Average: {}'.format(analysis['long']['pnl']['lost']['average']))
	# print('      Max: {}'.format(analysis['long']['pnl']['lost']['max']))
	# print('-' * 30)
	# print('Short Stats')
	# print('  Total: {}'.format(analysis['short']['total']))
	# print('  Won: {}'.format(analysis['short']['won']))
	# print('  Lost: {}'.format(analysis['short']['lost']))
	# print('  PNL: ')
	# print('    Total: {}'.format(analysis['short']['pnl']['total']))
	# print('    Average: {}'.format(analysis['short']['pnl']['average']))
	# print('    Won: ')
	# print('      Total: {}'.format(analysis['short']['pnl']['won']['total']))
	# print('      Average: {}'.format(analysis['short']['pnl']['won']['average']))
	# print('      Max: {}'.format(analysis['short']['pnl']['won']['max']))
	# print('    Lost: ')
	# print('      Total: {}'.format(analysis['short']['pnl']['lost']['total']))
	# print('      Average: {}'.format(analysis['short']['pnl']['lost']['average']))
	# print('      Max: {}'.format(analysis['short']['pnl']['lost']['max']))
	# print('-' * 30)
	# print('Length Stats')
	# print('  Total bars: {}'.format(analysis['len']['total']))
	# print('  Average bars: {}'.format(analysis['len']['average']))
	# print('  Max bars: {}'.format(analysis['len']['max']))
	# print('  Min bars: {}'.format(analysis['len']['min']))
	# print('  Won: ')
	# print('    Total: {}'.format(analysis['len']['won']['total']))
	# print('    Average: {}'.format(analysis['len']['won']['average']))
	# print('    Max: {}'.format(analysis['len']['won']['max']))
	# print('    Min: {}'.format(analysis['len']['won']['min']))
	# print('  Lost: ')
	# print('    Total: {}'.format(analysis['len']['lost']['total']))
	# print('    Average: {}'.format(analysis['len']['lost']['average']))
	# print('    Max: {}'.format(analysis['len']['lost']['max']))
	# print('    Min: {}'.format(analysis['len']['lost']['min']))
	# print('  Long: ')
	# print('    Total: {}'.format(analysis['len']['long']['total']))
	# print('    Average: {}'.format(analysis['len']['long']['average']))
	# print('    Max: {}'.format(analysis['len']['long']['max']))
	# print('    Min: {}'.format(analysis['len']['long']['min']))
	# print('    Won: ')
	# print('      Total: {}'.format(analysis['len']['long']['won']['total']))
	# print('      Average: {}'.format(analysis['len']['long']['won']['average']))
	# print('      Max: {}'.format(analysis['len']['long']['won']['max']))
	# print('      Min: {}'.format(analysis['len']['long']['won']['min']))
	# print('    Lost: ')
	# print('      Total: {}'.format(analysis['len']['long']['lost']['total']))
	# print('      Average: {}'.format(analysis['len']['long']['lost']['average']))
	# print('      Max: {}'.format(analysis['len']['long']['lost']['max']))
	# print('      Min: {}'.format(analysis['len']['long']['lost']['min']))
	# print('  Short: ')
	# print('    Total: {}'.format(analysis['len']['short']['total']))
	# print('    Average: {}'.format(analysis['len']['short']['average']))
	# print('    Max: {}'.format(analysis['len']['short']['max']))
	# print('    Min: {}'.format(analysis['len']['short']['min']))
	# print('    Won: ')
	# print('      Total: {}'.format(analysis['len']['short']['won']['total']))
	# print('      Average: {}'.format(analysis['len']['short']['won']['average']))
	# print('      Max: {}'.format(analysis['len']['short']['won']['max']))
	# print('      Min: {}'.format(analysis['len']['short']['won']['min']))
	# print('    Lost: ')
	# print('      Total: {}'.format(analysis['len']['short']['lost']['total']))
	# print('      Average: {}'.format(analysis['len']['short']['lost']['average']))
	# print('      Max: {}'.format(analysis['len']['short']['lost']['max']))
	# print('      Min: {}'.format(analysis['len']['short']['lost']['min']))
	# print('+' * 30)

	print('+' * 30)
	print('TradeAnalyzer')
	print('-' * 30)
	print('Total Open/Closed trades')
	print('	 Total: {}'.format(analysis['total']['total']))
	print('	 Open: {}'.format(analysis['total']['open']))
	print('	 Closed: {}'.format(analysis['total']['closed']))
	print('-' * 30)
	print('Streak')
	print('  Longest won: {}'.format(analysis['streak']['won']['longest']))
	print('  Longest lose: {}'.format(analysis['streak']['lost']['longest']))
	print('-' * 30)
	print('ProfitNLoss General')
	print('  Gross:')
	print('    Total: {}'.format(analysis['pnl']['gross']['total']))
	print('    Avg: {}'.format(analysis['pnl']['gross']['average']))
	print('  Net:')
	print('    Total: {}'.format(analysis['pnl']['net']['total']))
	print('    Avg: {}'.format(analysis['pnl']['net']['average']))
	print('-' * 30)
	print('Win Stats')
	print('  Total: {}'.format(analysis['won']['total']))
	print('  PNL: ')
	print('    Total: {}'.format(analysis['won']['pnl']['total']))
	print('    Average: {}'.format(analysis['won']['pnl']['average']))
	print('    Max: {}'.format(analysis['won']['pnl']['max']))
	print('-' * 30)
	print('Lose Stats')
	print('  Total: {}'.format(analysis['lost']['total']))
	print('  PNL: ')
	print('    Total: {}'.format(analysis['lost']['pnl']['total']))
	print('    Average: {}'.format(analysis['lost']['pnl']['average']))
	print('    Max: {}'.format(analysis['lost']['pnl']['max']))
	print('-' * 30)
	print('Long Stats')
	print('  Total: {}'.format(analysis['long']['total']))
	print('  Won: {}'.format(analysis['long']['won']))
	print('  Lost: {}'.format(analysis['long']['lost']))
	print('  PNL: ')
	print('    Total: {}'.format(analysis['long']['pnl']['total']))
	print('    Average: {}'.format(analysis['long']['pnl']['average']))
	print('    Won: ')
	print('      Total: {}'.format(analysis['long']['pnl']['won']['total']))
	print('      Average: {}'.format(analysis['long']['pnl']['won']['average']))
	print('      Max: {}'.format(analysis['long']['pnl']['won']['max']))
	print('    Lost: ')
	print('      Total: {}'.format(analysis['long']['pnl']['lost']['total']))
	print('      Average: {}'.format(analysis['long']['pnl']['lost']['average']))
	print('      Max: {}'.format(analysis['long']['pnl']['lost']['max']))
	print('-' * 30)
	print('Short Stats')
	print('  Total: {}'.format(analysis['short']['total']))
	print('  Won: {}'.format(analysis['short']['won']))
	print('  Lost: {}'.format(analysis['short']['lost']))
	print('  PNL: ')
	print('    Total: {}'.format(analysis['short']['pnl']['total']))
	print('    Average: {}'.format(analysis['short']['pnl']['average']))
	print('    Won: ')
	print('      Total: {}'.format(analysis['short']['pnl']['won']['total']))
	print('      Average: {}'.format(analysis['short']['pnl']['won']['average']))
	print('      Max: {}'.format(analysis['short']['pnl']['won']['max']))
	print('    Lost: ')
	print('      Total: {}'.format(analysis['short']['pnl']['lost']['total']))
	print('      Average: {}'.format(analysis['short']['pnl']['lost']['average']))
	print('      Max: {}'.format(analysis['short']['pnl']['lost']['max']))
	print('-' * 30)
	print('Length Stats')
	print('  Total bars: {}'.format(analysis['len']['total']))
	print('  Average bars: {}'.format(analysis['len']['average']))
	print('  Max bars: {}'.format(analysis['len']['max']))
	print('  Min bars: {}'.format(analysis['len']['min']))
	print('  Won: ')
	print('    Total: {}'.format(analysis['len']['won']['total']))
	print('    Average: {}'.format(analysis['len']['won']['average']))
	print('    Max: {}'.format(analysis['len']['won']['max']))
	print('    Min: {}'.format(analysis['len']['won']['min']))
	print('  Lost: ')
	print('    Total: {}'.format(analysis['len']['lost']['total']))
	print('    Average: {}'.format(analysis['len']['lost']['average']))
	print('    Max: {}'.format(analysis['len']['lost']['max']))
	print('    Min: {}'.format(analysis['len']['lost']['min']))
	print('  Long: ')
	print('    Total: {}'.format(analysis['len']['long']['total']))
	print('    Average: {}'.format(analysis['len']['long']['average']))
	print('    Max: {}'.format(analysis['len']['long']['max']))
	print('    Min: {}'.format(analysis['len']['long']['min']))
	print('    Won: ')
	print('      Total: {}'.format(analysis['len']['long']['won']['total']))
	print('      Average: {}'.format(analysis['len']['long']['won']['average']))
	print('      Max: {}'.format(analysis['len']['long']['won']['max']))
	print('      Min: {}'.format(analysis['len']['long']['won']['min']))
	print('    Lost: ')
	print('      Total: {}'.format(analysis['len']['long']['lost']['total']))
	print('      Average: {}'.format(analysis['len']['long']['lost']['average']))
	print('      Max: {}'.format(analysis['len']['long']['lost']['max']))
	print('      Min: {}'.format(analysis['len']['long']['lost']['min']))
	print('  Short: ')
	print('    Total: {}'.format(analysis['len']['short']['total']))
	print('    Average: {}'.format(analysis['len']['short']['average']))
	print('    Max: {}'.format(analysis['len']['short']['max']))
	print('    Min: {}'.format(analysis['len']['short']['min']))
	print('    Won: ')
	print('      Total: {}'.format(analysis['len']['short']['won']['total']))
	print('      Average: {}'.format(analysis['len']['short']['won']['average']))
	print('      Max: {}'.format(analysis['len']['short']['won']['max']))
	print('      Min: {}'.format(analysis['len']['short']['won']['min']))
	print('    Lost: ')
	print('      Total: {}'.format(analysis['len']['short']['lost']['total']))
	print('      Average: {}'.format(analysis['len']['short']['lost']['average']))
	print('      Max: {}'.format(analysis['len']['short']['lost']['max']))
	print('      Min: {}'.format(analysis['len']['short']['lost']['min']))
	print('+' * 30)

	return None