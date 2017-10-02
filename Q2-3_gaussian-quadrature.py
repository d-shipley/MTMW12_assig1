#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#   gaussian-quadrature.py
#
#   A program to integrate any function of one variable between any limits and 
#   to any required resolution.
#
#   The integration is carried out by the function "gauss_int".
#
#   A couple of test functions, whose integrals are known analytically, are also
#   included as functions to test the code.
#
#	This code was written to answer Q2 & 3, Assignment 1, for MTMW12 "Intro. to 
#   Numerical Modelling"
#

import numpy as np
import matplotlib.pyplot as plt

def gauss_int(f, lLim, uLim, nInts=20):
    #  Help text
    """
    A function to integrate numerically using 1-point Gaussian quadrature. Takes
    as input:
        f:		a function of one variable
        lLim:	lower limit of the integral
        uLim:	upper limit of the integral
        nInts:	number of intervals to divide the integration range into 
                (default = 20)
    1-point Gaussian quadrature works by adding together rectangles of height 
    equal to the value of the function evaluated halfway between adjacent 
    x-points. n-point Gaussian quadrature should be exact for polynomials of 
    degree n, so use this to check the code!
    """
    
    #  re-write this code to take an array of values as an input? So you can 
    #  numerically integrate a function for which we don't have an analytical 
    #  expression, or just a set of data points
    
    #  calculate interval length from input values
    dx = (uLim - lLim)/nInts
    
    #  initialise integral
    I = 0.
    
    #  sum contributions from each interval
    for i in xrange(0,nInts):
        I += f(lLim + (i+0.5)*dx) * dx
    return I;

def line_eq(x):
    #  Help text
    """
    Returns the equation of a line: y = 3.*x - 2.
    """
    return 3.*x - 2.;
    
def sin3(x):
    #  Help text
    '''
    Returns sin(3*x)
    '''
    return np.sin(3*x)

def main():
    #  Help text
    """
    The body of the program. Calls the function "gauss_int" to numerically 
    integrate a function specified by the writer. Has a boolean switch between 
    code for questions 2. and 3. of the assignment; if qNo == 2, runs code for 
    Q2; if qNo == 3, runs code for Q3.
    """
    
    #  set question number; must be an integer
    qNo = 3
    
    if qNo == 2:
        
        #  define integration parameters
        start = 0.	#  lower limit of integral (float)
        stop = np.pi	#  upper limit of integral (float)
        nInts = 20	#  number of intervals (int)
        
        #  perform the integration
        Integral = gauss_int(sin3, lLim=start, uLim=stop, nInts=nInts)
        
        #  print result to screen
        print "integral = ", Integral
    
    elif qNo == 3:
        #  This part of the code calculates the integral of sin(x) on the 
        #  interval [0,pi] using 1-point Gaussian quadrature, for
        #  nInts = {int(4e+3), int(4e+4), int(4e+5), int(4e+6)}, and computes 
        #  the absolute error of the method for each number of intervals.
        
        #  exact value of integral; should be 2
        exactInt = - np.cos(np.pi) + np.cos(0.)
        
        #  array containing different numbers of intervals
        nInts = [int(4e+3), int(4e+4), int(4e+5), int(4e+6)]
        Integral = np.zeros( len(nInts) )
        error = np.zeros( len(nInts) )
        
        #  define integration parameters
        start = 0.	#  lower limit of integral (float)
        stop = np.pi	#  upper limit of integral (float)
        
        #  print table headings to terminal
        print "nInts \t Integral \t Error "
        
        #  Perform the numerical integration for each element of nInts
        for i in xrange(0,len(nInts)):
            #  retrieve num. intervals from array
            n = nInts[i]
            #  integrate, and store in Integral array
            Integral[i] = gauss_int(np.sin, lLim=start, 
                            uLim=stop, nInts=n)
            #  calculate absolute error; store in error array
            error[i] = abs(Integral[i] - exactInt)
            
            #  print results to terminal
            print nInts[i], "\t", Integral[i], "\t", error[i]
            
        #  Calculate order of convergence between subsequent nInts
        for i in xrange(1,len(nInts)):
            #  calc. order of convergence between nInts[i], nInts[i-1]
            order = abs( (np.log10(error[i]) - np.log10(error[i-1]))/ \
                    (np.log10(nInts[i]) - np.log10(nInts[i-1])) )
            #  print to screen
            print "order of convergence between ", i-1, " and ", i, \
                    "=", order            
        
        plt.figure(1)
        plt.plot(np.log10(nInts), np.log10(error))
        plt.xlabel("log(Number of intervals)")
        plt.ylabel("log(Absolute error)")
        plt.title("Absolute error vs. number of intervals for 1-point "
                "Gaussian quadrature numerical integration of sin(x)")
        plt.show()
        plt.savefig("Q3_gauss_quad_error-vs-intervals.png")
        plt.close()
    
    else:
        raise Exception("Incorrect Question Number! qNo must be 2 or 3")
    
    return 0;

#   run main function
main()

#   Assignment: 
#   
#   2.  a)  Yes, the code integrates linear functions exactly.
#           Test function: y1 = 3*x - 2
#           Indefinite integral: y2 = (3/2)*x**2 - 2*x + const.
#           Exact integral over the interval [0,1]: - 0.5
#           Integral calculated using this code for 
#           nInts = 1: -0.5; 2: -0.5; 3: -0.5; 4: -0.5; 20: -0.5
#
#       b)  Integrating sin(m*x) on the interval [0,pi] for m=1,3; 20 
#           intervals.
#           Exact integral for m = 1: 2.0
#           Calculated integral for m = 1: 2.00205764829
#               ==> % error for m = 1 (= 100*|calc-exact|/exact ): ~0.1%
#           Exact integral for m = 3: 2/3
#           Calculated integral for m = 3: 0.672875357578
#               ==> % error for m = 3: ~0.9%
#           The relative error is much larger for m = 3; I presume this 
#           is because sin(3x) is further away from a linear function,
#           i.e. sin(3x) has three turning points in the interval [0,pi]
#           and so requires at least a quartic to approximate it on that
#           interval. sin(x), however, has only one turning point, so
#           only requires at least a quadratic to approximate it on 
#           [0,pi]. This gives a greater relative error because the 
#           1-pt Gaussian quadrature method loses accuracy for each 
#           polynomial degree > 1. (It's not the gradient, it's the 
#           curvature that's the problem.)
#
#   3.  Below is a table showing the absolute error in calculating the 
#       integral of sin(x) on the interval [0,pi] using 1-point Gaussian 
#       quadrature for different numbers of intervals:
#
#       nInts 	Integral 	    Error 
#       4000    2.0000000514 	5.14041884614e-08
#       40000 	2.00000000051 	5.14035480847e-10
#       400000 	2.00000000001 	5.13411535508e-12
#       4000000 2.00000000000   7.59392548844e-14
#
#       From this I calculated the order of convergence,
#       order == | (log(error1) - log(error2)) / (log(n1) - log(n2)) |,
#       for each increase in resolution:
#       order of convergence between  0  and  1 = 2.00000541033
#       order of convergence between  1  and  2 = 2.0005274745
#       order of convergence between  2  and  3 = 1.82999929079
#       
#       (log(error) vs. log(nInts) is also plotted in the file 
#       "Q3_gauss_quad_error-vs-intervals.png" in this directory.)
#       
#       The order of convergence decreases for the highest resolution
#       because at this point machine precision comes into play, i.e.
#       the absolute error is so small that machine precision becomes
#       significant in the calculation -- adding tiny numbers to a much
#       larger number many times!
