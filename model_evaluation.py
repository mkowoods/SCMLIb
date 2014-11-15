# -*- coding: utf-8 -*-
"""
Created on Fri Nov 14 19:52:57 2014

@author: mwoods
"""

import numpy as np

def mean_deviation(err):
    return err.sum()/err.size

def mean_absolute_deviation(err):
    return (err.abs()).sum()/err.size
    
def mse(err):
    return (err**2).sum()/err.size

def rmse(err):
    return np.sqrt(mse(err))

