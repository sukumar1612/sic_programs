# -*- coding: utf-8 -*-
"""
Created on Mon Sep 25 23:19:41 2023

@author: 91900
"""

"""LubeCar specializes in fast automobile oil change. 
The garage buys car oil in bulk at $3 per gallon discounted to $2.50 per gallon if the order quantity is more than 1000 gallons. 
The garage services approximately 150 cars per day, and each oil change takes 1.25 gallons. 
LubeCar stores bulk oil at the cost of $.02 per gallon per day. Also, the cost of placing an order is $20. 
There is a 2-day lead time for delivery.
Determine the optimal inventory policy. The consumption of oil per day is"""

import math 

D  = 150*1.25
c1 = 3
c2 = 2.5
q = 1000
h = 0.02
K = 20

ym = math.sqrt((2*K*D)/h)

if q < ym:
    print("The optimal inventory policy is ",ym)

a = 1
TCU_y1 = (c1*D) + ((K*D)/ym) + ((h*ym)/2)
b = (2 * (c2*D - TCU_y1))/h
c = ((2*K*D)/h)

temp = (b*b) - (4*a*c)

root1 = ((-1*b) + math.sqrt(temp))/(2*a)
root2 = ((-1*b) - math.sqrt(temp))/(2*a)

Q=0
if root1 < q:
    Q = root2
else:
    Q = root1
    
print("The value of root greater than q is ",Q)

y_star = 0

if q<ym:
    y_star = ym
    print("ZONE 1")

elif q > ym and q<=Q:
   y_star = q
   print("ZONE 2")

else:
    y_star = ym
    print("Zone 3")