#!/usr/bin/env python
# coding: utf-8

# In[1]:


tu = (23, 'abc', 4.56, (2,3), 'def')
li = ['abc', 34, 4.34, 23]
print(tu)


# In[2]:


numeros= list(range(100))
print(numeros)
print(numeros[40:60])


# In[3]:


for i in range (101):
    if i%7==0:
        print('%d\n' % numeros[i])
    else:
        print(numeros[i],end=' ')


# In[4]:


numeros= list(range(1,11))

print (numeros)

for n in numeros:
    print (n*n, end=', ')


# In[5]:


print=(numeros[90:],numeros[:20])


# In[6]:


print(103 in numeros)


# In[ ]:




