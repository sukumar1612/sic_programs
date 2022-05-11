#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed May 11 21:42:50 2022

@author: apple
"""

# Kohonen

weights = [
    [0.2, 0.6, 0.5, 0.9],
    [0.8, 0.4, 0.7, 0.3]
]

xip=[
     [1, 1, 0, 0],
     [0, 0, 0, 1],
     [1, 0, 0, 0],
     [0, 0, 1, 1]
]
alpha = 0.5

if __name__ == "__main__":
    for x in xip:
        cnt=0
        min_cnt=-1
        min_d=10000
        print(weights)
        for w in weights:
            d = 0
            for count in range(0, len(w)):
                d += (w[count]-x[count])**2
            
            print(d)
            if d < min_d:
                min_d = d
                min_cnt=cnt
            
            cnt+=1
        
        #weight updation
        for count in range(0, len(weights[min_cnt])):
            weights[min_cnt][count] = weights[min_cnt][count] + alpha*(x[count] - weights[min_cnt][count])
        
        print(weights)
    
    
    
        
        
        
        
        