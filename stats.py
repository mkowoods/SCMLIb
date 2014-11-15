from scipy.stats import t, norm
import numpy as np


def coef_of_variation(arr):
    return arr.std()/arr.mean()
    
    

def conf_interval(arr, confidence = 0.95):
    N = arr.size

    if N <= 30:
        z = t.interval(0.95, N - 1)
    else:
        z = norm.interval(0.95)

    s = arr.std()
    x_bar = arr.mean()

    return (x_bar - z*(s/np.sqrt(N)), x_bar + z*(s/np.sqrt(N)))
    



    
    

    