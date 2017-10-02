#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#	finite-sum.py
#	
#	This code was written to answer Q1, Assignment 1, for MTMW12 "Intro
#	to Numerical Modelling"
#	
#	The code calculates the sum of a finite sequence of numbers, 
#   generally known as an "arithmetic progression".
#	

def finite_arithmetic_sum(diff, lLim=1, uLim=int(1e4), start=0.):
    '''
    Function to evaluate a finite arithmetic sum. 
    Takes as input:
           diff =  difference between consecutive terms
           lLim = lower limit of sum (default = 1)
           uLim = upper limit of sum (default = int(1e4))
           start = initial value of sum (default = 0.)
    Returns the value of the sum as a float.
    '''
    
    total = start      #  sum initialised

    for i in xrange(lLim, uLim+1):    
        #  lower value of range is inclusive, upper value is exclusive
        
        total += diff    #  adds "diff" to the sum
    
    return total;   #  returns final value of the sum
                    #  (could modify to also return some of the other
                    #  parameters?)

print finite_arithmetic_sum(1e-2,uLim=int(1e4))

#   Assignment: 
#   Answers for sum:
#   N               | 1e4       | 1e7           | 1e6
#   program answer  | 100.0     | 99999.9999863 | 10000.0000002
#   true answer     | 100.0     | 100000.0      | 10000.0
#
#   This is a decimal-binary-decimal conversion error; the computer does
#   not add 0.01 to itself N times, it adds the closest 32-bit binary
#   representation of 0.01 to itself N times -- this representation is 
#   not exact, so after many operations, the computed value of the sum
#   diverges from the true value.


