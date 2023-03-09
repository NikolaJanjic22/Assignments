#!/usr/bin/env python
# coding: utf-8

# In[11]:


class Geom():
 geomType = 'Generic Geometry Type'
 def __init__(self):
    self.name = random.choice(['Bill','Sally','Tamica','Josh','Lammar','Hussain'])
    self.color = random.choice(['BLUE', 'RED', 'PURPLE'])
 def print_name(self):
     print('My name is ',self.name, 'and my color is ',self.color)
 def makeString(self):
     return f"Name: {self.name}, Color: {self.color}, Area: {self.area()}"
class Triangle(Geom):
 def _init_ ():
     self.side = side
     super().__init__()
 def area(self):
     return (sqrt(3) * (side)**2) / 4


# In[ ]:




