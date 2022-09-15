#!/usr/bin/env python
# coding: utf-8

# In[2]:


#Importing the necessary libraries 
import pandas as pd
import numpy as np 
import matplotlib.pyplot as plt
import seaborn as sns


# In[3]:


df=pd.read_csv('CO2 Emissions_Canada.csv')


# In[4]:


df.describe()


# In[5]:


#Removing Null Values
a = df.dropna()
print(a)


# In[7]:


#Removing duplicated values 
x = a.drop_duplicates()


# In[8]:


print(x)


# In[9]:


a.count()


# In[16]:


a.plot.hist(x='Cylinders',y='Engine Size(L)')
plt.xlabel('Cylinders')
plt.ylabel('Engine Size(L)')


# In[8]:


import pandas as pd
b=pd.read_csv (r'C:\Users\HP\Desktop\CO2 Emissions_Canada.csv')


# In[5]:


import numpy as np 
import matplotlib.pyplot as plt
import seaborn as sns


# In[13]:


c=b['Fuel Consumption City (L/100 km)']
print(c)

d=b['CO2 Emissions(g/km)']

plt.scatter(c,d)
plt.xlabel('Fuel Consumption City (L/100 km)')
plt.ylabel('CO2 Emissions(g/km)')


# In[14]:


b.corr()


# In[16]:


sns.heatmap(b.corr())


# In[ ]:




