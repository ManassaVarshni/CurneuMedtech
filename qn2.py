
# coding: utf-8

# In[2]:


import pandas as pd
data=pd.read_csv("E:/curneu/User1data.csv")
print(data)


# In[7]:


df=pd.DataFrame(data)
df[df.columns[4:6]]


# In[37]:


data.dropna(inplace=True)
#new=data["Recommended"].str.split("(",n=1,expand=True)
data["x"]=new[0]
data["y"]=new[1]
#data['z']=data['y'].str.strip().str[4]
data.drop(columns=["x"],inplace=True)
#data.drop(columns=["z"],inplace=True)
#data.drop(columns=["Recommended"],inplace=True)
#data['z']=y[:-1] for y in data['z']
new1=data["y"].replace(')','')
data["l"]=new1[0]
#data[5].str.slice(0,-1)
data

