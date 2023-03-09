#!/usr/bin/env python
# coding: utf-8

# In[22]:


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
class Square(Geom):
    def __init__ (self,side):
        self.side = side
        super().__init__() 
def area(self):
        return self.side **2
side = 8
my_square = Square(side)
my_square.print_name()
print('My area is ', my_square)


# In[ ]:




