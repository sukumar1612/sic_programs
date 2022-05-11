#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed May 11 22:51:35 2022

@author: apple
"""

#HMM
from math import log2

H = {
     'A':0.2,
     'C':0.3,
     'G':0.3,
     'T':0.2
     }

L = {
     'A':0.3,
     'C':0.2,
     'G':0.2,
     'T':0.3
     }
start_h_l = 0.5

self_h = 0.5
self_l = 0.6

trans_hl = 0.5
trans_lh = 0.4


if __name__ == "__main__":
    path = 'GGCA'
    h = start_h_l * H[path[0]]
    l = start_h_l * L[path[0]]
    prev_h = h
    prev_l = l
    
    for node in path[1:]:
        print(h, l)
        h = prev_h * self_h * H[node] + prev_l * trans_lh * H[node]
        l= prev_l * self_l * L[node] + prev_h * trans_hl * L[node]
        
        prev_h = h
        prev_l = l
    
    print(h+l)
    
    path = 'GGCACTGAA'
    h = log2(start_h_l) + log2(H[path[0]])
    l = log2(start_h_l) + log2(L[path[0]])
    prev_h = h
    prev_l = l
    
    for node in path[1:]:
        if h>l:
            print('H', end='')
        else:
            print('L', end='')
            
        
        h = log2(H[node]) + max(prev_h+log2(self_h), prev_l+log2(trans_lh))
        l = log2(L[node]) + max(prev_l+log2(self_l), prev_h+log2(trans_hl))
        
        
        prev_h = h
        prev_l = l
    
    if h>l:
        print('H', end='')
    else:
        print('L', end='')
    
    probability = pow(2, max(h, l))
    print("\nprobability of path :", probability)
        
        
    
        














