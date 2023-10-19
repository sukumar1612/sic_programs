# -*- coding: utf-8 -*-
"""
Created on Mon Sep 25 22:19:42 2023

@author: 91900
"""
import numpy as np
import sympy as sp

K = sp.Array([10,5,15])
a = sp.Array([1,1,1])
D = sp.Array([2,4,4])
h = sp.Array([0.3,0.1,0.2])
A = 25
n = 3
y = sp.IndexedBase('y')
i,k = sp.symbols('i k')
TCU= sp.summation(K[i]*D[i]/y[i]+h[i]*y[i]/2, (i,0,n-1))
constraint  = sp.summation(a[i]*y[i],(i,0,n-1))-A
print("The function to be minimised is \n",TCU,"\n")

print("The constraint is \n",constraint ," <= 0\n")

lamda = sp.symbols('lambda')
L = TCU-constraint*lamda
gradL = [sp.diff(L,y[j]) for j in range(n)] + [sp.diff(L,lamda)]

print(gradL)
print("\n")

eq2 = gradL.copy()
sol2 = sp.nsolve(eq2,[y[i] for i in range(n)]+[lamda],[1,1,1,1])
i=0
for j in sol2:
    print("y",i," = ",j)
    i=i+1