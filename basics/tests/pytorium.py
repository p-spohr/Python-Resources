#!/usr/bin/env python
# coding: utf-8

# In[3]:


if type([1,2,3]) == tuple:
	print('Es ist ein list.')
else:
    print('Es ist kein list.')


# In[4]:


if 'h' in 'hello':
	print('Es gibt ein h!')


# In[5]:


if 'h' in 'hello':
	print(5* len('hello'))


# In[6]:


x = {'name':'bill', 'pet': 'cat', 'food': 'pizza'}


# In[7]:


len(x)


# In[8]:


meine_liste = [1,2,3]


# In[10]:


2 in meine_liste


# In[12]:


if type([1,2,3]) == tuple:
	print('Es ist ein tuple.')
else:
    print('Es ist kein tuple.')


# In[29]:


z = list(range(1,4,1))
z.reverse()
for i in z:
	print(i)


# In[30]:


zahl = 0

while zahl < 5:
    print(zahl)
    
    zahl += 1  # tippt das zuerst!!!


# In[35]:


x = 1
liste = []
while x < 10:
    liste.append(x)
    x += 1


# In[36]:


liste


# In[37]:


liste = [4,0,2,3,1,2,3,1]
while 1 in liste:
	liste.pop()
print(liste)


# In[38]:

# %%
check = 0
match check:	
    case 0:
        print('true')
    case _:
        print('false')


gruppe = [
		  {'name': 'Tim', 'alter':55, 'essen': 'pizza'},
		  {'name': 'Tina', 'alter':33, 'essen': 'kuchen'},
		  {'name': 'Zed', 'alter':20, 'essen': 'schnitzel'}]

for freund in gruppe:
    freund_name = freund['name']
        match freund_name:
        case 'Tina':
            print('Meine Beste Freundin!')
        case _:
            print('Hallo.')


# In[40]:


# gruppe = [
# 		  {'name': 'Tim', 'alter':55, 'essen': 'pizza'},
# 		  {'name': 'Tina', 'alter':33, 'essen': 'kuchen'},
# 		  {'name': 'Zed', 'alter':20, 'essen': 'schnitzel'}]

# for freund in gruppe:
# 	match freund['name']:
# 		case 'Tina':
# 			print('Meine Beste Freundin!')
# 			print('Lass uns', freund['essen'], 'essen!')
# 		case _:
# 			print('Hallo.')


# In[ ]:




