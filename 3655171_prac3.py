########################################

### PRAC 3 ###

########################################

# Benito van der Merwe
# 3655171

########################################

### Question 1 ###

########################################

def q1_1(i):#defining the function
  if i > 0:#starting argument for i
    return "positive"#return statement
  
  elif i == 0:#else statement of i if its = 0
    return "zero"#return statement
    
  else:#the statement if i is not greater and/or 0
      return "negative"#return statement
 #Test   
print(q1_1(0))
print(q1_1(5))
print(q1_1(-10)) 

def q1_2(s):#defining the function
  s = len(s)#starting argument for s
  if s > 4:#if statement when s is greater than 4
    return "too long"#return statement
  else:#statement when s is less than and/or equal to 4
    return "OK"#return statement
#Test    
print(q1_2("hello"))
print(q1_2("hi"))

def q1_3(n):#defining the function
  if n > 10000:#starting argument for n
    return n#return statement
#Test
print(bool(q1_3(10000)))
print(bool(q1_3(10001)))

def q1_4(m):#defining the function
  if m % 10 == 0:#statement to check the divisiblity of the function
    print ("True")#print statement if m is divisible by 10
  else:#else statement if the above statement does not hold up
    print ("False")#print statement if m is not divisible by 10
#Test   
print(bool(q1_4(20)))
print(bool(q1_4(21)))

########################################

### Question 2 ###

########################################

import matplotlib.pyplot as plt#importing mathplotlib to draw the graph
import numpy as np#importing numpy library

def q2_1(x):#defining the funtion
  return np.e**(-x)*np.sin(x*3)#returning the function
x1 = np.arange(1.0, 10, 0.1)#the x values as a array
plt.plot(x1, q2_1(x1))# plotting the points
plt.xlabel('x - axis')# naming the x axis
plt.ylabel('y - axis')#naming the y axis
plt.title('Q2_1')#naming the the graph
plt.show()# function to show the plot

import matplotlib.pyplot as plt#importing mathplotlib to draw the graph
import numpy as np#importing numpy library

def q2_2(z):#defining the funtion
  return np.log(z)*np.cos(z/10)#returning the function
x1 = np.arange(1.0, 10, 0.1)#the x values as a array
plt.plot(x1, q2_2(x1))# plotting the points
plt.xlabel('x - axis')# naming the x axis
plt.ylabel('y - axis')#naming the y axis
plt.title('Q2_2')#naming the the graph
plt.show()# function to show the plot


########################################

### Question 3 ###

########################################

import matplotlib.pyplot as plt#importing mathplotlib to draw the graph
import numpy as np#importing numpy library
from math import cos, sin, pi#importing pi

def q3(x,t):#defining the funtion
  return A*np.sin(kx - wt + ph)#returning the function

A = 3#Amplitude of the function
w = 60#angular frequency
k = 1#wave number
ph = 0.5 * pi#phase constant

x1 = np.arange(1.0, 10, 0.1)#generic x values as a array
t1 = np.arange(1.0, 10, 0.1)#generic t values as a array

kx = k * x1
wt = w * t1


plt.plot(x1, q3(x1, t1))# plotting the points
plt.xlabel('x - axis')# naming the x axis
plt.ylabel('y - axis')#naming the y axis
plt.title('Asin(kx - wt - ph)')#naming the the graph
plt.show()# function to show the plot

########################################

### Question 4 ###

from math import cos, sin, pi#importing trig functions
import matplotlib.pyplot as plt#importing mathplotlib
import numpy as np#importing numpy

x0 = 0#initial position, x-component
y0 = 0#initial position, y-component
g= 1.62#gravity on the moon
theta = 45#angle of the ball
v0 = 50#initial velocity

vx = v0 * cos((pi/180) * theta)#velocity, x-component
vy = v0 * sin((pi/180) * theta)#veleocity, y-component
t = 0#initial time

t_fin = 2 * vy/g#time flight
t_half = 0.5 * t_fin#half of the total time
t_end = round(t_fin)#final time interval
print ("time ball travelled is",t_end, "s")

y_max = (vy **2)/ (2 * g)#calculating the height
height = round(y_max)#final height of the projectile
print ("The height of the ball is", height, "m upwards")

x_max = vx * t_fin#calculating the distance
x_half = vx * t_half#half of the total distance
dis = round(x_max)#final distance traveled
print ("total distance covered by the ball is",dis, "m")

vxn = np.arange(0, 1550, 100)#x axis values
vyn = np.arange(0, 400, 100)#y axis values

plt.plot(vx, vy)# plotting the points
plt.xlabel('vx')# naming the x axis
plt.ylabel('vy')# naming the y axis
plt.title("Visualising some soccer")# naming the graph
 
plt.show()# function to show the plot


########################################



########################################

### Question 5 ###

########################################

def q5_1():
    # Put your code here 
    return 

### q5_2 ###
### This question is written only, no code required.

########################################

########################################
