#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed May 11 20:39:01 2022

@author: apple
"""

x = [
     [11.0, 13],
     [9.0, 12],
     [8.5, 18],
     [12.0, 8],
     [13.0, 18],
     [18.0, 5],
     [20.0, 7.5],
     [16.5, 6],
     [19.0, 6.5],
     [12.0, 9],
]

actual = ['MI', 'MI', 'MI', 'MI', 'MI', 'A', 'A', 'A', 'A', 'A']
actual_val = [1.0,1.0,1.0,1.0,1.0,0.0,0.0,0.0,0.0,0.0]

w = [-0.3, 1.0]
threshold = 0.0
alpha = 0.01

if __name__ == "__main__":
    for i in range(0, 100):
        print()
        output_val =[]
        for j in range(0, len(x)):
            output = round(w[0]*x[j][0] + w[1]*x[j][1], 5)
            output_val.append(output)
            
            if output > threshold:
                output = 1.0
                print('MI', end=' ')
                if output != actual_val[j]:
                    w[0] = w[0] + alpha * (actual_val[j] - output)*x[j][0]
                    w[1] = w[1] + alpha * (actual_val[j] - output)*x[j][1]
            else:
                output = 0.0
                print('A', end=' ')
                if output != actual_val[j]:
                    w[0] = w[0] + alpha * (actual_val[j] - output)*x[j][0]
                    w[1] = w[1] + alpha * (actual_val[j] - output)*x[j][1]
        print()
        print(output_val)

