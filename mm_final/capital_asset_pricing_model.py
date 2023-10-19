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

R = 8
market_var = 12

data = {"Portfolio": ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H'],
        "mu": [20, 18, 12, 16, 14, 10, 17, 15], # expected returns
        "beta": [1.0, 2.5, 1.5, 1.0, 0.8, 1.2, 1.6, 2.0], #
        "residue_var": [40, 35, 30, 35, 25, 15, 30, 35] }

df = pd.DataFrame(data)
df

def u_r(df, R):
    l = []
    for i in range(len(df)):
        l.append(round((df.mu[i] - R) / df.beta[i] , 4))
    return l

def u_rb(mu, R, beta, residue_var):
    l = []
    for i in range(len(mu)):
        l.append(round(((mu[i] - R) * beta[i]) / residue_var[i] , 4))
    return l

def beta_sqrd(beta, residue_var):
    l = []
    for i in range(len(beta)):
        l.append(round((beta[i]**2 / residue_var[i]), 4))
    return l

def c(market_var, cumsum1, cumsum2):
    l = []
    for i in range(len(cumsum1)):
        l.append((market_var * cumsum1[i]) / (1 + (market_var * cumsum2[i])))
    return l

def z(df, optimal_c):
  df['zi'] = ''
  for i in range(4):
    z = (df['beta'][i] / df['residue_var'][i]) * (df['mu-r'][i] - optimal_c)
    df['zi'][i] = z
  return df

def construct_table(df, R, market_var):
  df['mu-r'] = u_r(df, R)
  df.sort_values(by = 'mu-r', ascending = False, inplace = True)
  df.reset_index(inplace = True, drop = True)

  df["mu-r-e2"] = u_rb(df["mu"], R, df["beta"], df["residue_var"])
  df['cum-mu-r-e2'] = df['mu-r-e2'].cumsum()

  df["beta-res"] = beta_sqrd(df["beta"], df["residue_var"])
  df['cum-beta-res'] = df['beta-res'].cumsum()

  df["ci"] = c(market_var, df["cum-mu-r-e2"], df["cum-beta-res"])
  optimal_c = max(df['ci'])

  df = z(df, optimal_c)

  df["weights"] = ''
  for i in range(4):
    df['weights'][i] = df['zi'][i] / sum(df['zi'][:4])

  return df

construct_table(df, R, market_var)

weights_sum = 0
for i in range(4):
    weights_sum += df["weights"][i]
weights_sum

