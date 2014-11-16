# -*- coding: utf-8 -*-
"""
Created on Fri Nov 14 21:34:48 2014

@author: mwoods
"""

import numpy as np
import sample_data

def exp_smoothing():
    pass

def holt_winter():
    pass

class SimpleExponentialSmoothing:
    
    def __init__(self, data, name = "unknown"):
        self.data = data
        self.name = name
        self.model = None
        
    def _train(self, alpha=0.2):
        if alpha < 0 or alpha > 1:
            raise ValueError("Alpha needs to be between 0 and 1")
        
        if alpha < 0.1 or alpha > 0.3: 
            print "Warning: alpha out of normal range" 
        
        res = np.zeros_like(self.data, dtype = 'float')
        res[0] = self.data[0]
        
        for n in range(1, len(res)):
            res[n] = alpha*self.data[n-1] + (1 - alpha)*res[n-1]   
        
        self.model = res
        

    def forecast(self, periods = []):
        """takes in a list of periods measured at the same rate as the training
        data and will provide the forecasted results"""
        pass
        

if __name__ == "__main__":
    s = sample_data.sample2
    
    model = SimpleExponentialSmoothing(s['data'], s['item'])
    
