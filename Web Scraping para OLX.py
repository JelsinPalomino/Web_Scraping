#!/usr/bin/env python
# coding: utf-8

# # Web Scraping de OLX Cusco
# <p>Haciendo web scraping para los productos que se encuentran en OLX Cusco </p> 

# In[1]:


from bs4 import BeautifulSoup
import requests
import pandas as pd


# In[2]:


url = 'https://www.olx.com.pe/cusco_g4070683'
page = requests.get(url)
soup = BeautifulSoup(page.content, 'html.parser')


# In[8]:


# Extraemos la información de precios y descripción
olx  =soup.find_all('span', class_='_2tW1I')


# In[9]:


# creamos una lista "equipos"
productos = list()

for i in olx:
    productos.append(i.text)
    
print(productos, len(productos))


# In[11]:


# Extraemos los precios
precio  =soup.find_all('span', class_='_89yzn')

precios = list()

count = 0
for i in precio:
    if count < 20:
        precios.append(i.text)
    else:
        break
    count +=1
    
print(precios, len(precios))


# In[13]:


# Dataframe
olx2 = pd.DataFrame({'Producto': productos, 'Precios': precios}, index = list(range(1,21)))
print(olx2)


# In[ ]:


# Exportamos a csv
olx2.to_csv('olx.csv', index = False)

