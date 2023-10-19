import numpy as np
import pandas as pd
import scipy
from scipy import stats
import matplotlib.pyplot as plt

data = [16,15,17,17,18,21,20,24,25,26,9,10,13,11,14,18,18,22,21,25]

lvl1_avg=[]
for i in range(len(data)-3):
  lvl1_avg.append((data[i]+data[i+1]+data[i+2]+data[i+3])/4)

lvl2_avg=[]
for i in range(len(lvl1_avg)-1):
  lvl2_avg.append((lvl1_avg[i]+lvl1_avg[i+1])/2)

perc_values=[]
for i in range(2,len(data)-2):
  perc_values.append((lvl2_avg[i-2]/data[i])*100)

calc1 = []
calc1.append(0)
calc1.append(0)
for i in range(len(perc_values)):
  calc1.append(perc_values[i])
calc1.append(0)
calc1.append(0)

k=0
main = []
temp = []
for i in range(len(calc1)):
  if k==4:
    k=0
    main.append(temp)
    temp=[]
  temp.append(calc1[i])
  k+=1
main.append(temp)

print(main)

ar1=[]
ar2=[]
ar3=[]
ar4=[]
for i in range(len(main)):
  for j in range(len(main[i])):
    if j==0:
      ar1.append(main[i][j])
    if j==1:
      ar2.append(main[i][j])
    if j==2:
      ar3.append(main[i][j])
    if j==3:
      ar4.append(main[i][j])
ar1.sort()
ar2.sort()
ar3.sort()
ar4.sort()

q1=0
q2=0
q3=0
q4=0
for i in range(0,4):
  q1+=ar1[i]
  q2+=ar2[i]
  q3+=ar3[i]
  q4+=ar4[i]
q1/=3
q2/=3
q3/=3
q4/=3

sum=q1+q2+q3+q4

q = 400/sum
sum1=(q1*q)+(q2*q)+(q3*q)+(q4*q)

new_data=[]
for i in range(len(data)):
  new_data.append(data[i]*q)

print("The deseasonalized data is: ",new_data)

x = [i+1 for i in range(len(new_data))]
#print(x)
import scipy
res = scipy.stats.linregress(x,new_data)
y_plot = []
for i in range(len(x)):
  y_plot.append(res.intercept+(res.slope*i))
t_value,p_value = scipy.stats.ttest_ind(y_plot,new_data)

plt.plot(x,new_data,'o')
plt.plot(x,y_plot,'r')

