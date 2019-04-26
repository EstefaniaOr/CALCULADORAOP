# -*- coding: utf-8 -*-
"""
Created on Thu Apr 11 09:15:02 2019

@author: prestamour
"""

import math

class Point:       
    
    def __init__(self,x=0,y=0):
        self.x=x 
        self.y=y
    
    def distance(self,other):
        return ((self.x-other.x)**2 + (self.y-other.y)**2)**0.5

    def reflect_x(self):
        return Point(self.x,-self.y)
    
    def __str__(self):
        return "({0} , {1})".format(self.x, self.y)
        
    def slope(self, target):
        m = ((self.y-target.y)/(self.x-target.x))
        return m
    
    def sumup(self,target):
        return Point((self.x + target.x),(self.y + target.y))
    
    def intersect(self,target):
        m = self.slope(target)
        b = (m)*(-self.x) + self.y  
        return b
    
    def get_line(self, target):
        b = str(self.intersect(target))
        m = str(self.slope(target))
        return "y = " + m + "x + " +b
    
    def angle_to_orig(self):
        h = self.y
        x = self.x
        ang = math.degrees((2*math.pi)-(math.atan(h/x)))
        return ang

p = Point(3,2)
q = Point(2,1)
r = Point()

print("distancia entre los puntos \n", r.distance(p))
print("reflexión alrededor del eje x \n", p.reflect_x())
print("pendiente entre los puntos \n", p.slope(q))
print("suma entre los puntos \n",p.sumup(q))
print("y intersecto de los puntos \n",p.intersect(q))
print("ecuación de la recta que pasa por los puntos",p, q, " es: \n", p.get_line(q))
print(p.angle_to_orig())