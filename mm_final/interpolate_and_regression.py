import pandas as pd
import numpy as np
import scipy.interpolate as interpolate
import matplotlib.pyplot as plt
df = pd.read_csv("BPCL.NS.csv")

df

df2 = df.filter(['Open'], axis=1)

Y = list(df['Open'])

intial=1
df.insert(0,'S.No',range(intial,intial+df.shape[0]))

X = list(df['S.No'])

f = interpolate.interp1d(X, Y)
xnew = np.arange(1, len(df)+1, 1)
ynew = f(xnew)   # use interpolation function returned by `interp1d`

plt.plot(X, Y, 'o', xnew, ynew, '-')

plt.show()

from scipy import stats

res = stats.linregress(X, Y)

y_plot = []
for i in X:
  y_plot.append(res.intercept + res.slope*i)

plt.plot(X, Y, 'o', label='original data')
plt.plot(X, y_plot, 'r', label='fitted line')

predicted=[]
for i in X:
  predicted.append(res.intercept + res*slope*i)

import scipy.stats as stats
def t_test(predicted, Y):
    t_value, p_value = stats.ttest_ind(predicted, Y)
    return t_value
t_test(forecasted,expected_values)