#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun May 15 12:07:22 2022

@author: apple
"""


import sympy
import random
import math

MAX_VAL = 2**16
MIN_VAL = 2**8
SIZE_V=5

def gen_coprime(phi_n):
    e = random.randint(1, phi_n)
    
    while math.gcd(e, phi_n)!=1:
        e = random.randint(1, phi_n)
    
    return e
        

def third_party_gen_n():
    p = sympy.randprime(MIN_VAL, MAX_VAL)
    q = sympy.randprime(MIN_VAL, MAX_VAL)
    
    n = p*q
    phi_n = (p-1)*(q-1)
    
    e = gen_coprime(phi_n)
    
    return phi_n, n, e

def calculate_witness(n, e):
    r = random.randint(0, n-1)
    x = pow(r, e, n)
    
    return r, x

def generate_keys(n, e):
    s = random.randint(1, n-1)
    v = pow(pow(s, e, n), -1, n)
    
    return s, v



if __name__ == "__main__":
    phi_n, n, e = third_party_gen_n()
    
    s, v = generate_keys(n, e)
    
    for i in range(0, 20):
        r, x = calculate_witness(n, e)
        c = random.randint(0, e-1)
        
        y = (pow(r, e, n) * pow(s, c*e, n))%n
        vc = pow(v, c, n)
        yvc = (y*vc)%n
        
        if yvc == x:
            print("verified")
        
        









