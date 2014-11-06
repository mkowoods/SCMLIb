#!/usr/bin/env python

import numpy as np
import pylab


class UnivariatePattern(object):
    def __init__(self, name, pattern):
        self.name = name
        self.pattern = pattern

    def get_summary_stats(self):
        std = np.std(self.pattern)
        mean = np.mean(self.pattern)
        n = self.pattern.size

        print "-----Results for %s - Size = %s" % (self.name, n)
        print "mean: %.2f, std: %.2f" % (mean, std)

    def basic_plot(self):
        fig = pylab.figure()
        ax1 = fig.add_subplot(221)
        ax1.hist(self.pattern)

        ax2 = fig.add_subplot(222)
        ax2.boxplot(self.pattern)

        ax3 = fig.add_subplot(223)
        ax3.plot(self.pattern)

        ax4 = fig.add_subplot(224)
        ax4.scatter(range(self.pattern.size), self.pattern)


if __name__ == "__main__":
    import sample_data

    part_id = sample_data.sample['item']
    part_data = np.array(sample_data.sample['data'])

    U = UnivariatePattern(part_id, part_data)
    U.basic_plot()
