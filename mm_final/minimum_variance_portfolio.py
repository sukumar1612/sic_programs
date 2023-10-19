import math
import pandas as pd
import numpy as np
import pandas as pd
import statistics
from scipy.stats import norm
import math
import seaborn as sns
import matplotlib.pyplot as plt
import yfinance as yf

"""TextBook Problem"""

u = np.array([0.1, 0.15, 0.2])
sig = np.array([0.28, 0.24, 0.25])

c = np.array([
    [0.28**2,-0.10*0.28*0.24,0.25*0.28*0.25],
    [-0.10*0.28*0.24, 0.24**2, 0.20*0.24*0.25],
    [0.25*0.28*0.25, 0.20*0.24*0.25, 0.25**2]
])

c_1 = np.linalg.inv(c)
m = u
u = np.array([1,1,1])

np.matmul([1,1,1], c_1)

w = np.matmul(u, c_1)/np.matmul(np.matmul(u, c_1), u.T)
np.matmul(m, w) #uv
np.sqrt(np.matmul(np.matmul(w, c), w.T)) # sigma v

"""With Dataset"""

df1 = yf.download('ZTS', start='2010-10-10', end='2020-2-20', progress=False)
df1 = df1.dropna()
df1.reset_index(inplace=True)
df1.rename(columns={"index":"date"},inplace=True)
df1.head()

df2 = yf.download('AAPL', start='2010-10-10', end='2020-2-20', progress=False)
df2 = df2.dropna()
df2.reset_index(inplace=True)
df2.rename(columns={"index":"date"},inplace=True)
df2.head()

def calc_returns(df):
  returns = []
  for open, close in zip(df['Open'], df['Close']):
    returns.append(round((close - open)/open, 2)) # returns for each month
  df['Returns'] = returns
  return df

def month_wise_total_returns(df):
  return df.groupby(df['Date'].dt.month)['Returns'].sum().values

def calc_expected_return(return_sum):
  return sum(return_sum)/len(return_sum) # assumption is that prob of states in k are equal = 1/len(no of vals)

def calc_variance(return_sum, expected_return):
  n = len(return_sum)
  var_sum = 0
  for r in return_sum:
    var_sum+=(r - expected_return)**2

  return var_sum/n # not sure, please check

def calc_covk1k2(k1, k2, Ek1, Ek2, n):
  sum = 0
  for ki1, ki2 in zip(k1, k2):
    sum+=(ki1 - Ek1)*(ki2 - Ek2)

  return sum/(n-1)

def calc_optimal_weights(df_1, df_2):
  df_1 = calc_returns(df_1)
  df_2 = calc_returns(df_2)

  return_sum1 = month_wise_total_returns(df_1)
  return_sum2 = month_wise_total_returns(df_2)

  print(f"return for df1: {return_sum1}")
  print(f"return for df2: {return_sum2}")

  Ek1 =  calc_expected_return(return_sum1)
  Ek2 =  calc_expected_return(return_sum2)

  print(f"expected returns for df1: {Ek1}")
  print(f"expected returns for df2: {Ek2}")

  sigmak1 = calc_variance(return_sum1, Ek1)
  sigmak2 = calc_variance(return_sum2, Ek2)

  print(f"variance for df1: {sigmak1}")
  print(f"variance for df2: {sigmak2}")

  covk1k2 = calc_covk1k2(return_sum1, return_sum2, Ek1, Ek2, len(return_sum1))
  cov_matrix = [[sigmak1**2, covk1k2], [covk1k2, sigmak2**2]]

  u = np.array([1,1])
  cov_matrix_1 = np.linalg.inv(np.array(cov_matrix))

  print(f"\n\ncovariance matrix inverse is: {cov_matrix_1}")

  return np.matmul(u, cov_matrix_1)/np.matmul(np.matmul(u, cov_matrix_1), u.T), np.array(cov_matrix), np.array([Ek1, Ek2])

w, c, m = calc_optimal_weights(df1, df2)

def calc_expected_returnand_sd_for_portfolio(m, c, w):
  print(f"The expected return and risk (standard deviation) of this portfolio are {np.matmul(m, w.T)*100}%, {np.sqrt(np.matmul(np.matmul(w, c), w.T))}")

calc_expected_returnand_sd_for_portfolio(m, c, w)

