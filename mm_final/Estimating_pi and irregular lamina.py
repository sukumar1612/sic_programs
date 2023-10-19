import random
import numpy as np
import matplotlib.pyplot as plt


inside = []
outside = []

def pi_calc(iter):
  interval = 0
  circle_points = 0
  square_points = 0
  while(interval<iter):
    x = random.uniform(-1,1)
    y = random.uniform(-1,1)

    d = x*x + y*y

    if(d<=1):
      inside.append([x,y])
      circle_points+=1
    else:
      outside.append([x,y])
    square_points+=1
    interval+=1

  return [circle_points, square_points]

c,s = pi_calc(1000)
pi = 4*(c/s)
print("Value of pi when 1000 points are taken is approx: ",pi)

c,s = pi_calc(10000)
pi = 4*(c/s)
print("Value of pi when 10000 points are taken is approx: ",pi)

c,s = pi_calc(100000)
pi = 4*(c/s)
print("Value of pi when 100000 points are taken is approx: ",pi)

outsidex=[i[0] for i in outside]
outsidey=[i[1] for i in outside]

insidex=[i[0] for i in inside]
insidey=[i[1] for i in inside]

plt.scatter(outsidex,outsidey,color = 'blue')
plt.scatter(insidex,insidey,color = 'red')

"""##Estimating area of rectangular lamina using simulation(shoelace algorithm)"""

def det(x1,y1,x2,y2):
  return ((x1*y2)-(x2*y1))

no_of_points = 4#random.randint(3,5)
print("No of points: ",no_of_points)

x = []
y = []
for i in range(0,no_of_points):
  x.append(int(random.randint(-10,10)))
  y.append(int(random.randint(-10,10)))
x.sort()
for i in range(0,no_of_points):
  print("(",x[i],",",y[i],")")

coord = []
for i in range(0,no_of_points):
  arr = []
  arr.append(x[i])
  arr.append(y[i])
  coord.append(arr)
arr = []
arr.append(x[0])
arr.append(y[0])
coord.append(arr)
xpoints,ypoints = zip(*coord)
print(xpoints)
print(ypoints)
plt.plot(xpoints,ypoints)
plt.show()

area = 0
for i in range(0,no_of_points-1):
  area += det(x[i],x[i+1],y[i],y[i+1])
i+=1
area += det(x[i],x[0],y[i],y[0])
area /= 2
print("Area of polygon: ",abs(area))

