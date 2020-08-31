#!/usr/bin/env python
# coding: utf-8

# In[3]:


pip install altair vega_datasets


# In[42]:


import altair as alt
from vega_datasets import data


# In[43]:


source = data.seattle_temps()
source


# In[56]:


New_Source= source[2300:7300]


# In[57]:


#Altair only needs three main concepts to create chart: Data, Marks and Encodings. 
#Data in Altair is built around the Pandas Dataframe. Marks are the various charts such as points, line, area, scatter, histograms, and maps etc. 
#Encodings are the mappings of data to visual properties such as axis, color of marker, shape of marker etc.

alt.Chart(New_Source).mark_line().encode(
    x='date',
    y='temp')


# In[58]:


alt.Chart(New_Source).mark_line().encode(
    x='month(date):T',
    y='mean(temp):Q'
)


# In[59]:


alt.Chart(New_Source).mark_rect().encode(
    x = alt.X('date(date):O', title='day'),
    y = alt.Y('month(date):O', title='month'),
    color='max(temp):Q'
).properties(
    title="2010 Daily High Temperatures in Seattle (F) WTF"
)


# In[65]:


###Now lets play with COV19 Data
import os as os
import pandas as pd
import altair as alt


# In[66]:


os.getcwd()


# In[70]:


#change direcroy
os.chdir ('/Users/margamarga/Documents/Scripts')


# In[71]:


#List all the documents
os.listdir()


# In[69]:


print(os.getcwd())


# In[74]:


full_clean_data = pd.read_csv('covid_19_clean_complete_06_Apr_2020.csv')


# In[75]:


full_clean_data


# In[76]:


countries = ['US', 'Italy', 'China', 'Spain', 'France', 'Chile', 'United Kingdom', 'Switzerland','Brazil']


# In[77]:


selected_data = full_clean_data[full_clean_data['Country/Region'].isin(countries)]


# In[78]:


selected_data


# In[122]:


alt.Chart(selected_data).mark_circle().encode(
    x='Date',
    y='Country/Region',
    color='Country/Region',
    size='Deaths'
).properties(
    width=980,
    height=300,
)


# In[112]:


#The circules doesn't mark the difference, so lets make it bigger by using alt.Size
alt.Chart(selected_data).mark_circle().encode(
    x='monthdate(Date):O',
    y='Country/Region',
    color='Country/Region',
    size=alt.Size('New cases:Q',
        scale=alt.Scale(range=[0, 2000]),
        legend=alt.Legend(title='Daily new cases')
    ) 
)


# In[113]:


interval = alt.selection_interval()


# In[114]:


alt.Chart(selected_data).mark_circle().encode(
    x='monthdate(Date):O',
    y='Country/Region',
    color='Country/Region',
    size=alt.Size('New cases:Q',
        scale=alt.Scale(range=[0, 3000]),
        legend=alt.Legend(title='Daily new cases')
    ) 
).properties(
    width=1000,
    height=300,
    selection=interval
)


# In[116]:


alt.Chart(selected_data).mark_circle().encode(
    x='monthdate(Date):O',
    y='Country/Region',
    color=alt.condition(interval, 'Country/Region', alt.value('lightgray')),
    size=alt.Size('New cases:Q',
        scale=alt.Scale(range=[0, 3000]),
        legend=alt.Legend(title='Daily new cases')
    ) 
).properties(
    width=1000,
    height=300,
    selection=interval
)


# In[132]:


alt.Chart(selected_data).mark_bar().encode(
    y='Country/Region',
    color = 'Country/Region',
    x='sum(New cases):Q'
).properties(
    width=1000,
)

    




# In[130]:


interval = alt.selection_interval()

circle = alt.Chart(selected_data).mark_circle().encode(
    x='monthdate(Date):O',
    y='Country/Region',
    color=alt.condition(interval, 'Country/Region', alt.value('lightgray')),
    size=alt.Size('New cases:Q',
        scale=alt.Scale(range=[0, 3000]),
        legend=alt.Legend(title='Daily new cases')
    ) 
).properties(
    width=1000,
    height=300,
    selection=interval
)

bars = alt.Chart(selected_data).mark_bar().encode(
    y='Country/Region',
    color='Country/Region',
    x='sum(Deaths):Q'
).properties(
    width=1000
).transform_filter(
    interval
)

circle & bars


# In[ ]:




