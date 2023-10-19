import matplotlib.pyplot as plt
import numpy as np

"""###Random Number Generation from Uniform Distribution"""

rng = np.random.default_rng()
arr_uni = rng.uniform(10,20,10000)

plt.hist(arr_uni)
plt.show()

counts, bins = np.histogram(arr_uni)
plt.plot(bins[:-1]+1, counts)

"""###Random Number Generation from Poisson Distribution"""

poissonDistributionSample = np.random.poisson(5,1000)

poissonIntervals = []
for i in range(1, 14, 2):
  poissonIntervals.append(i)

poissonIntervals

poissonCounter = dict()
for i in range(0,len(poissonIntervals)):
  poissonCounter[poissonIntervals[i]] = 0

for i in poissonDistributionSample:
  for j in poissonIntervals:
    if i<=j:
      poissonCounter[j]+=1
      break;

poissonCounter

plt.hist(poissonDistributionSample, bins=poissonIntervals, density=True)
plt.show()

plt.plot(poissonIntervals, poissonCounter.values(), color='green', marker='*', linestyle='-')
plt.show()

"""Random distribution Gaussian Distribution"""

rng = np.random.default_rng()
Gaussian = rng.standard_normal(10000)

plt.hist(Gaussian)
plt.show()

counts, bins = np.histogram(Gaussian)
plt.plot(bins[:-1]+1, counts)

size=1000
low=1000
high=6000
interval = 100
uniformDistributionSample = np.random.uniform(low,high,size)
intervals = []
for num in range(low, high, interval):
  intervals.append(num)

intervals_counter = dict()

for i in range (0,len(intervals)):
  intervals_counter[intervals[i]]=0

for i in uniformDistributionSample:
  for j in intervals:
    if i < j:
      intervals_counter[j]+=1
      break;

intervals_counter

plt.hist(uniformDistributionSample, bins=intervals, density=True)
plt.show()

plt.plot(intervals, intervals_counter.values(), color='green', marker='x', linestyle='-')
plt.show()