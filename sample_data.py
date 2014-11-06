
import numpy as np

np.random.seed(42)

trend = np.array(range(520))
trend = 2*trend
trend_plus_noise = trend + 15*np.random.rand(520)


sample = {
    'item': 'switch_1',
    'data': trend_plus_noise
}