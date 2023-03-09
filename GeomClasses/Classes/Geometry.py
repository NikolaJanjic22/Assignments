#!/usr/bin/env python
# coding: utf-8

# In[29]:


import random
import math as mth

class Geom():
  geomType = 'Generic Geometry Type'
  def __init__(self):
    self.name = random.choice(['Bill','Sally','Tamica','Josh','Lammar','Hussain'])
    self.color = random.choice(['BLUE', 'RED', 'PURPLE'])
    self.type = "geometry" 
  def print_name(self):
    print('My name is',self.name, ', a', self.type, ', and my color is',self.color)
  def makeString(self):
    return f"Name: {self.name}, Type: {self.type}, Color: {self.color}, Area: {self.area()}"
class Square(Geom):
  
  def __init__ (self,side):
    super().__init__()
    self.side = side
    self.type = "square"
  def area(self):
     return self.side **2


# In[ ]:




