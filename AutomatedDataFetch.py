#!/usr/bin/env python
# coding: utf-8

# In[5]:


import requests
from nsepython import *   
print(indices)
import datetime
from pynse import *
nse=Nse()


# In[6]:


A = nse.info('SBIN')
df1 = pd.DataFrame(A.items())
df1


# In[7]:


def export_csv(df):
  with io.StringIO() as buffer:
    df.to_csv(buffer)
    return buffer.getvalue()


# In[11]:


buffer = io.BytesIO()
buffer.write(export_csv(df1).encode())
buffer.seek(0)
buffer.name = f'SBIN.csv'


# In[12]:


base_url = "https://api.telegram.org/bot2116923117:AAFccongYIN7CJwXcIjMbtidduE6IiYEFuM/sendDocument"

parameters = {
    "chat_id" : "-777737632",
    "caption" : "SBIN"
}

files = {
    "document" : buffer
}

resp = requests.get(base_url, data = parameters, files = files)


# In[13]:


nse.update_symbol_list()


# In[14]:


A = fnolist()
df2 = pd.DataFrame({'col':A})
df2


# In[15]:


buffer = io.BytesIO()
buffer.write(export_csv(df2).encode())
buffer.seek(0)
buffer.name = f'fnolist.csv'


# In[16]:


base_url = "https://api.telegram.org/bot2116923117:AAFccongYIN7CJwXcIjMbtidduE6IiYEFuM/sendDocument"

parameters = {
    "chat_id" : "-777737632",
    "caption" : "fnolist"
}

files = {
    "document" : buffer
}

resp = requests.get(base_url, data = parameters, files = files)


# In[17]:


print(running_status())


# In[18]:


nse.market_status()


# In[19]:


df4 = nse.pre_open()
df4


# In[20]:


buffer = io.BytesIO()
buffer.write(export_csv(df4).encode())
buffer.seek(0)
buffer.name = f'pre_open.csv'


# In[21]:


base_url = "https://api.telegram.org/bot2116923117:AAFccongYIN7CJwXcIjMbtidduE6IiYEFuM/sendDocument"

parameters = {
    "chat_id" : "-777737632",
    "caption" : "pre_open"
}

files = {
    "document" : buffer
}

resp = requests.get(base_url, data = parameters, files = files)


# In[22]:


A = nse_blockdeal()
df5 = pd.DataFrame(A.items())
df5


# In[23]:


buffer = io.BytesIO()
buffer.write(export_csv(df5).encode())
buffer.seek(0)
buffer.name = f'nse_blockdeal.csv'


# In[24]:


base_url = "https://api.telegram.org/bot2116923117:AAFccongYIN7CJwXcIjMbtidduE6IiYEFuM/sendDocument"

parameters = {
    "chat_id" : "-777737632",
    "caption" : "pre_open"
}

files = {
    "document" : buffer
}

resp = requests.get(base_url, data = parameters, files = files)


# In[26]:


df6 = nse_fiidii()
df6


# In[27]:


buffer = io.BytesIO()
buffer.write(export_csv(df6).encode())
buffer.seek(0)
buffer.name = f'nse_fiidii.csv'


# In[28]:


base_url = "https://api.telegram.org/bot2116923117:AAFccongYIN7CJwXcIjMbtidduE6IiYEFuM/sendDocument"

parameters = {
    "chat_id" : "-777737632",
    "caption" : "nse_fiidii"
}

files = {
    "document" : buffer
}

resp = requests.get(base_url, data = parameters, files = files)


# In[30]:


df7 = nse.top_gainers(index=IndexSymbol.FnO, length=10)
df7


# In[31]:


buffer = io.BytesIO()
buffer.write(export_csv(df7).encode())
buffer.seek(0)
buffer.name = f'top_gainers.csv'


# In[32]:


base_url = "https://api.telegram.org/bot2116923117:AAFccongYIN7CJwXcIjMbtidduE6IiYEFuM/sendDocument"

parameters = {
    "chat_id" : "-777737632",
    "caption" : "top_gainers"
}

files = {
    "document" : buffer
}

resp = requests.get(base_url, data = parameters, files = files)


# In[33]:


df8 = nse.top_losers(index=IndexSymbol.FnO, length=10)
df8


# In[35]:


buffer = io.BytesIO()
buffer.write(export_csv(df8).encode())
buffer.seek(0)
buffer.name = f'top_losers.csv'


# In[36]:


base_url = "https://api.telegram.org/bot2116923117:AAFccongYIN7CJwXcIjMbtidduE6IiYEFuM/sendDocument"

parameters = {
    "chat_id" : "-777737632",
    "caption" : "top_losers"
}

files = {
    "document" : buffer
}

resp = requests.get(base_url, data = parameters, files = files)


# In[37]:


df9 = nse_get_top_gainers()
df9


# In[38]:


buffer = io.BytesIO()
buffer.write(export_csv(df9).encode())
buffer.seek(0)
buffer.name = f'nse_get_top_gainers.csv'


# In[39]:


base_url = "https://api.telegram.org/bot2116923117:AAFccongYIN7CJwXcIjMbtidduE6IiYEFuM/sendDocument"

parameters = {
    "chat_id" : "-777737632",
    "caption" : "nse_get_top_gainers"
}

files = {
    "document" : buffer
}

resp = requests.get(base_url, data = parameters, files = files)


# In[40]:


df10 = nse_get_top_losers()
df10


# In[41]:


buffer = io.BytesIO()
buffer.write(export_csv(df10).encode())
buffer.seek(0)
buffer.name = f'nse_get_top_losers.csv'


# In[42]:


base_url = "https://api.telegram.org/bot2116923117:AAFccongYIN7CJwXcIjMbtidduE6IiYEFuM/sendDocument"

parameters = {
    "chat_id" : "-777737632",
    "caption" : "nse_get_top_losers"
}

files = {
    "document" : buffer
}

resp = requests.get(base_url, data = parameters, files = files)


# In[43]:


df11 = nse_get_advances_declines()
df11


# In[44]:


buffer = io.BytesIO()
buffer.write(export_csv(df11).encode())
buffer.seek(0)
buffer.name = f'nse_get_advances_declines.csv'


# In[45]:


base_url = "https://api.telegram.org/bot2116923117:AAFccongYIN7CJwXcIjMbtidduE6IiYEFuM/sendDocument"

parameters = {
    "chat_id" : "-777737632",
    "caption" : "nse_get_advances_declines"
}

files = {
    "document" : buffer
}

resp = requests.get(base_url, data = parameters, files = files)


# In[46]:


df12 = nse_results("equities","Quarterly")
df12


# In[47]:


buffer = io.BytesIO()
buffer.write(export_csv(df12).encode())
buffer.seek(0)
buffer.name = f'nse_results.csv'


# In[48]:


base_url = "https://api.telegram.org/bot2116923117:AAFccongYIN7CJwXcIjMbtidduE6IiYEFuM/sendDocument"

parameters = {
    "chat_id" : "-777737632",
    "caption" : "nse_results"
}

files = {
    "document" : buffer
}

resp = requests.get(base_url, data = parameters, files = files)


# In[49]:


df13 = nse_events()
df13


# In[50]:


buffer = io.BytesIO()
buffer.write(export_csv(df13).encode())
buffer.seek(0)
buffer.name = f'nse_events.csv'


# In[51]:


base_url = "https://api.telegram.org/bot2116923117:AAFccongYIN7CJwXcIjMbtidduE6IiYEFuM/sendDocument"

parameters = {
    "chat_id" : "-777737632",
    "caption" : "nse_events"
}

files = {
    "document" : buffer
}

resp = requests.get(base_url, data = parameters, files = files)


# In[52]:


df14 = pd.json_normalize(nse_holidays()['FO'])
df14


# In[53]:


buffer = io.BytesIO()
buffer.write(export_csv(df14).encode())
buffer.seek(0)
buffer.name = f'nse_holidays.csv'


# In[54]:


base_url = "https://api.telegram.org/bot2116923117:AAFccongYIN7CJwXcIjMbtidduE6IiYEFuM/sendDocument"

parameters = {
    "chat_id" : "-777737632",
    "caption" : "nse_holidays"
}

files = {
    "document" : buffer
}

resp = requests.get(base_url, data = parameters, files = files)


# In[ ]:




