import matplotlib.pyplot as plt
import numpy as np

"""The Linear Congruential Generator"""

a=191
b=525
m=1000
x0=118

Ans=[]
ele=((a*x0)+b)%m
for i in range(1,10001):
  Ans.append(ele)
  ele=((a*ele)+b)%m

#print(Ans)

plt.hist(Ans)
plt.show()

counts,bins = np.histogram(Ans)
plt.plot(bins[:-1]+1,counts)

"""Multiplicative Congruence method"""

a=191
m=525
x0=118

Ans=[]
ele=(a*x0)%m
for i in range(1,10001):
  Ans.append(ele)
  ele=(a*ele)%m

#print(Ans)

plt.hist(Ans)
plt.show()

counts,bins = np.histogram(Ans)
plt.plot(bins[:-1]+1,counts)

"""Additive Congruence method"""

b=191
m=525
x0=118

Ans=[]
ele=(a+x0)%m
for i in range(1,10001):
  Ans.append(ele)
  ele=(a+ele)%m

#print(Ans)

plt.hist(Ans)
plt.show()

counts,bins = np.histogram(Ans)
plt.plot(bins[:-1]+1,counts)

"""Middle Square Method"""

x0=173
Ans=[]
for i in range(1,10001):
  ele=x0*x0
  stringele=str(ele)
  final=""
  final+=stringele[0]
  n=len(stringele)
  final+=stringele[n-1]
  ans=int(final)
  Ans.append(ans)
  x0=ans

#print(Ans)

plt.hist(Ans)
plt.show()

counts,bins = np.histogram(Ans)
plt.plot(bins[:-1]+1,counts)

"""Xor Shift algorithm"""

x=111
y=59
z=91
w=41

Ans=[]
for i in range(1,10001):
  a = x ^ ((x << 3) & 0xFF)
  x=y
  y=z
  z=w
  w = (w ^ (w >> 4)) ^ (a ^ (a >> 5))
  Ans.append(w)
  x=w

#print(Ans)

plt.hist(Ans)
plt.show()

counts,bins = np.histogram(Ans)
plt.plot(bins[:-1]+1,counts)

