#!/usr/bin/env python
# coding: utf-8

# In[14]:


import math as mth
import random

class Geom():
    geomType = 'Generic Geometry Type'
    def __init__(self):
        self.name = random.choice(['Bill','Sally','Tamica','Josh','Lammar','Hussain'])
        self.color = random.choice(['BLUE', 'RED', 'PURPLE'])
    def print_name(self):
        print('My name is ',self.name, 'and my color is ',self.color)
    def makeString(self):
        return f"Name: {self.name}, Color: {self.color}, Area: {self.area()}"
class Circle(Geom):
    def __init__ (self,radius):
        self.radius = radius
        super().__init__()
    def area(self):
        return mth.pi * self.radius **2
circle_list = [Circle(i) for i in range(2,3)]
print(circle_list)
for x in circle_list:
    x.print_name()
print([x.makeString() for x in circle_list])


# In[ ]:




