from arch import arch_model
import backtrader as bt
import pandas as pd
import numpy as np
from statsmodels.stats.diagnostic import acorr_ljungbox

class GARCH_rolling(bt.Indicator):
    '''
    Author: Gabriel Contarini
    
    This is a GARCH rolling window forecast indicator 
    implemention for backtrader. Standard deviation forecasts
    are made with horizon 1, those forecasts can be used to construct
    bands around the close price. It was implementated using
    an arch library for the GARCH estimation.
    
    Args:
        period: int number of data points used in each window.
        p_arch: int p parameter from GARCH model.
        q_arch: int autoregressive lags parameter.
    
    Returns:
        Float: conditional standard deviation forecast for returns.
        Bool: flag indicating if the model fits the data (False for no fit).
    
    To do:
        Implement plot functions.
        Other models besides vanilla garch.
    '''


    params = (
        ('period', 30),
        ('p_arch', 1),
        ('q_arch', 1),
        ('lags', 10)
        )

    # Return lines for backtrader
    lines = ('conditional_sd', 'flag',)

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
                dist='SkewStudent'
                ).fit(disp='off')
        
        # Make forecast
        forc = garch_model.forecast(horizon=1).variance
        ret_var = forc['h.1'].iloc[-1]
        ret_std = np.sqrt(ret_var)
        
        # Model fit test on residuals
        test = acorr_ljungbox(garch_model.resid, lags=[self.p.lags], return_df=True)
        
        # True if model is well fit
        flag = True
        for p in test['lb_pvalue'].values:
            if p < .05:
                flag = False
                break

        # Return end values
        self.l.conditional_sd[0] = ret_std
        self.l.flag[0] = flag

class GARCH_rollband(GARCH_rolling):
    ''' Uses the GARCH forecast to construct 2 lines around the price. '''

    params = (
        ('period', 30),
        ('p_arch', 1),
        ('q_arch', 1),
        ('lags', 10)
        )

    lines = ('above', 'below', 'flag',)

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
                dist='SkewStudent'
                ).fit(disp='off')

        # Make forecast
        forc = garch_model.forecast(horizon=1).variance
        ret_var = forc['h.1'].iloc[-1]
        ret_std = np.sqrt(ret_var)

        # Model fit test on residuals
        test = acorr_ljungbox(garch_model.resid, lags=[self.p.lags], return_df=True)
        
        # True if model is well fit
        flag = True
        for p in test['lb_pvalue'].values:
            if p < .05:
                flag = False
                break

        # Compute return bands
        last_ret = ((self.datas[0].close / self.datas[-1].close) - 1) * scale_factor
        ret_pos = last_ret + ret_std
        ret_neg = last_ret - ret_std
        # Compute price bands
        pos = self.datas[0].close * ((ret_pos / scale_factor) + 1)
        neg = self.datas[0].close * ((ret_neg / scale_factor) + 1)

        # Return end values
        self.l.above[0] = pos
        self.l.below[0] = neg
