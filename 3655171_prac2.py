########################################

### PRAC 2 ###

########################################

# Benito van der Merwe
# 3655171

########################################

### Question 1 ###

########################################

def q1_1(seconds): #defining the function in terms of seconds
   return seconds/60 #converting the function into minutes
   
print (q1_1(120), "min")#Answer

def q1_2(au): #defining the function in terms of au
   return (au*149598073) #converting the function into km
   
print (q1_2(1), "km") #Answer
print (q1_2(39.5), "km") #Answer

def q1_3(age): #defining the function in terms of age
   return(age*365*60*60*24) #converting the function into seconds
   
print (q1_3(1), "seconds") # Answer
print (q1_3(21), "seconds") #Answer

def q1_4(string): #defining the function
   return len(string) #using len to get the length of a string
   
print (q1_4("a")) #Answer
print (q1_4("hello")) #Answer

########################################

### Question 2 ###

########################################

import numpy as np #importing python library
def q2_1(x): #defining the function
  return np.exp(-x)*np.sin(3*x) #computing the function using numpy

x = 4 #Selecting a value for x
print (q2_1(x)) #Answer

x = np.array([2.6, 9.1, 3.7]) #setting x as a array using numpy
print (q2_1(x)) #Answer 

import numpy as np #importing python library
def q2_2(x): #defining the function
  return np.log(x)*np.cos(x/10)#computing the function using numpy

x = 4 #Selecting a value for x
print (q2_2(x)) #Answer

x = np.array([2.6, 9.1, 3.7]) #setting x as a array using numpy
print (q2_2(x)) #Answer

########################################

### Question 3 ###

########################################

from math import pi #import a constant, pi, from the math library
def v(r, T): #defining the function
  return 2*pi*r/T #computing the angular speed
  
print (v(9, 15), "m/s") #Answer

########################################

### Question 4 ###

########################################

import numpy as np #importing python library
from scipy.misc import derivative #importing the derivative function from the scipy library

xn = 1 #initial value
x = np.linspace(-10, 10, 100) #array of x-values

def f(x): #defining the function
    return 1-(x/10)*np.log(x)

def x_next(f, x, xn): #defining the function x_next, which is the x-value following xn
  slope = derivative(f, xn, dx=0.1)#slope of the tangent
  return xn - f(xn) / slope
  
for n in range(10): #selecting the number of attempts
  print("x_{} = {:.3f}".format(n+1, xn)) #Printing the outputs to 3 decimal places
  xn = x_next(f, x, xn)

########################################

### Question 5 ###

########################################

def q5_1():
    # Put your code here 
    return 

def q5_2():
    # Put your code here 
    return 

########################################

########################################