#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun May 15 11:48:46 2022

@author: apple
"""


import sympy
import random
import math

MAX_VAL = 2**16
MIN_VAL = 2**8
SIZE_V=5

def third_party_gen_n():
    p = sympy.randprime(MIN_VAL, MAX_VAL)
    q = sympy.randprime(MIN_VAL, MAX_VAL)
    
    return p*q

def generate_secret(n):
    val = sympy.randprime(1, MAX_VAL)
    while math.gcd(val, n)!=1:
        val = random.randint(1, n-1)
    
    return val


def generate_alice_secrets(n):
    s = [generate_secret(n) for i in range(0, SIZE_V)]
    v = [pow(pow(s[i], 2, n), -1, n) for i in range(0, SIZE_V)]
    
    return s, v

def calculate_witness(n):
    r = random.randint(0, n-1)
    x = pow(r, 2, n)
    
    return r, x

def calculate_response(r,s,c):
    return r*pow(s, c)
    

if __name__ == "__main__":
    n = third_party_gen_n()
    s, v = generate_alice_secrets(n)
    
    for i in range(0, 20):
        r, x = calculate_witness(n)
        
        c = [random.randint(0, 1) for i in range(0, SIZE_V)]
        
        y = r
        for i in range(0, SIZE_V):
            y = pow(y, 1, n) * pow(s[i]**c[i], 1, n)
            y= pow(y, 1, n)
        
        y = pow(y, 1, n)
        
        
        yvc = y**2
        for i in range(0, SIZE_V):
            yvc = pow(yvc, 1, n) * pow(v[i]**c[i], 1, n)
            yvc = pow(yvc, 1, n)
        
        yvc = pow(yvc, 1, n)
                
        
        if pow(yvc, 1, n) == x:
            print("verified")
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
