#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Dec 28 23:39:51 2016

@author: christophergreen

Quadratic primes
Problem 27
Euler discovered the remarkable quadratic formula:

n^2+n+41
It turns out that the formula will produce 40 primes for the consecutive integer values 0≤n≤39. 
However, when n=40,40^2+40+41=40(40+1)+41n=40, 40^2+40+41=40(40+1)+41 is divisible by 41, and certainly 
when n=41,41^2+41+41 is clearly divisible by 41.

The incredible formula n^2−79n+1601 was discovered, which produces 80 primes for the 
consecutive values 0≤n≤79 The product of the coefficients, −79 and 1601, is −126479.

Considering quadratics of the form:

n^2+an+b, where |a|<1000 and |b|≤1000

where |n| is the modulus/absolute value of n
e.g. |11|=11 and |−4|=4
Find the product of the coefficients, a and b, for the quadratic expression that produces
 the maximum number of primes for consecutive values of n, starting with n=0;
"""

import math

def is_prime(x):
    if x<1:
        return False;
    for i in range(2,math.floor(math.sqrt(x)+1)):
        if x%i==0:
            return False
    return True


def list_primes(max):
    primes=[]; 
    j=2;
    while j<=max:
        if is_prime(j):
            primes.append(j)
        j+=1
    return primes;

#|b| must be prime and <=1000: bearing in mind that |b| must be prime:   
p=list_primes(1001);
bvals=[];
for j in p:
    bvals.append(j);
    #bvals.append(-j);

#assemble all possible [a,b] pairs:
possibles=[];
a=-1000;
while a<1000:
    k=0;
    while k<len(bvals):
        possibles.append([a,bvals[k]]);
        k+=1;
    a+=1; 
#print(len(possibles)); -->672,000




def num_consec_primes(a,b):
    x=0;
    while is_prime(x**2+a*x+b):
        x+=1;
    return x;

def main():    
    z=0;  
    while z<len(possibles):
        #print("trying the pair with index",z);
        #if (z+1)%100==0:
            #print("tying the pair with index",z);
        consec = num_consec_primes(possibles[z][0],possibles[z][1]);
        if consec>30:
            print("a=",possibles[z][0],"and b=",possibles[z][1],"produces",consec,"consec primes");
        z+=1;
    print(" ");
    print(z);
    return;  #-->highest was a= -61 and b= 971 produces 71 consec primes CORRECT

    
        