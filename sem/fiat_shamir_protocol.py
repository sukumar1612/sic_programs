#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun May 15 11:22:34 2022

@author: apple
"""

import sympy
import random

MAX_VAL = 2**16
MIN_VAL = 2**8

def third_party_gen_n():
    p = sympy.randprime(MIN_VAL, MAX_VAL)
    q = sympy.randprime(MIN_VAL, MAX_VAL)
    
    return p*q

def generate_secret(n):
    return random.randint(1, n-1)


def generate_alice_secrets(n):
    s = generate_secret(n)
    v = pow(s, 2, n)
    
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
        
        c = random.randint(0, 1)
        
        y = calculate_response(r,s,c)
        xvc = calculate_response(x, v, c)
        
        if pow(y, 2, n) == pow(xvc, 1, n):
            print("verified")
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    