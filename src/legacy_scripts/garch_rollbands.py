from arch import arch_model
import backtrader as bt
import pandas as pd
import numpy as np

class GARCH_rollingbands(bt.Indicator):
    '''
    Author: Gabriel Contarini
    
    This is a GARCH rolling window band forecast indicator 
    implemention for backtrader. It was implementated using
    an arch library for the GARCH estimation.
    
    Args:
        period: int number of data points used in each window.
        p_arch: int p parameter from GARCH model.
        q_arch: int autoregressive lags parameter.
    
    Returns:
        A positive and a negative band around close price.
    
    To do:
        Implement plot functions.
        Other models besides vanilla garch.
        Scale factor as a param.
    '''


    params = (
    	('period', 30),
    	('p_arch', 1),
    	('q_arch', 1)
    	)

    # Return lines for backtrader
    lines = ('pos_b', 'neg_b',)

    def __init__(self):
        # Min periods
        self.addminperiod(self.p.period)
    
    def next(self):
        # Scale factor to help garch opt
        scale_factor = 10000
        
        # Select data
        raw_data = self.data.get(size=self.p.period)
        # Compute returns
        data = pd.Series(raw_data)
        fit_data = data.pct_change().iloc[1:] * scale_factor
        
        # Fit GARCH model
        garch_model = arch_model(
        	fit_data, 
        	mean='Zero', 
        	vol='GARCH', 
        	p=self.p.p_arch, 
        	q=self.p.q_arch, 
        	dist='Normal'
        	).fit(disp='off')
        
        # Make forecast
        forc = garch_model.forecast(horizon=1).variance
        ret_var = forc['h.1'].iloc[-1]
        ret_std = np.sqrt(ret_var)
        
        # Compute return bands
        last_ret = ((self.datas[0].close / self.datas[-1].close) - 1) * scale_factor
        ret_pos = last_ret + ret_std
        ret_neg = last_ret - ret_std
        # Compute price bands
        pos = self.datas[0].close * ((ret_pos / scale_factor) + 1)
        neg = self.datas[0].close * ((ret_neg / scale_factor) + 1)

        # Return end values
        self.l.pos_b[0] = pos
        self.l.neg_b[0] = neg 