# -*- coding: utf-8 -*-
"""
Created on Mon Sep 25 23:07:53 2023

@author: 91900
"""

"""Neon lights on the U of A campus are replaced at the rate of 100 units per day. 
The physical plant orders the neon lights periodically. 
It costs $100 to initiate a purchase order. 
A neon light kept in storage is estimated to cost about $.02 per day. 
The lead time between placing and receiving an order is 12 days. 
Determine the optimal inventory policy for ordering the neon lights."""

import math 
def EOQ(D,H,K,L):
    
    Y = math.sqrt((2*K*D)/H)
    
    t0 = Y/D
    
    n = math.floor(L/t0)
    
    Le = L - (n*t0)
    
    LeD = Le * D
    
    print("The inventary order should take place when level drops to ",LeD)
    
    TCU_Y = math.sqrt(2*K*D*H)
    
    print("The optimal inventary cost of neon lights is",TCU_Y)
    
     
D = 100
K = 100
H = 0.02
L = 12

EOQ(D,H,K,L)