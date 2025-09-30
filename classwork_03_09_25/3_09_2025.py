#!/usr/bin/env python
# coding: utf-8

# In[1]:


print('Hello world')


# In[5]:


age = int(input())
print(f"Чётное: {age % 2 == 0}")


# In[6]:


a = 10
a *= 2
print(a)


# In[26]:


for i in range(0, 10):
    for j in range(0, 10):
        print(f'[{i}, {j}]', end=' ')
    print()


# In[10]:


def num_digits(number): # 10
    str_number = str(number) # '10'
    len_string = len(str_number)
    print(len_string)
num = int(input())
num_digits(num)


# In[28]:


def num_digits(number): 0
    size = 0
    while number > 0:
        size += 1
        number //= 10
    print(size)
        


# In[30]:


fruits = ['Apple', 'Peach', 'Banana']
print(fruits)
print(len(fruits))
fruits.append("Pear")
print(fruits[0])
last_el = fruits.pop()
print(last_el)


# In[32]:


def summ(a, b):
    a + b
result = summ(10, 20)
print("Ваш чек:", result)


# In[33]:


print(print())


# In[3]:


# import time
from time import time

def decorator(func):
    def wrapper():
        print("Inside wrapper")
        start = time()
        func()
        end = time()
        print(f"Working time: {end - start}")
    return wrapper

@decorator
def function():
    for i in range(40000000):
        i * i
function = decorator(function)




# In[ ]:





# In[15]:


from time import time, sleep
start = time() 
sleep(3)
end = time() 
print(start)
print(end)


# In[12]:


from math import pi
from random import randint, seed


# In[21]:


seed(2)
for i in range(10):
    print(randint(0, 10))


# In[23]:


import datetime


# In[25]:


print(datetime.datetime.now())


# In[58]:


now = datetime.datetime.now()
formatted_date = now.strftime('%Y/%d/%m %H:%M:%S') # -> str
formatted_date = formatted_date.replace("e", "Декабрь")

print(formatted_date)


# In[59]:


curr_date = "2025/03/09 19:04:46"


# In[60]:


datetime.datetime.strptime(curr_date, '%Y/%d/%m %H:%M:%S')


# In[61]:


datetime.datetime.now() - datetime.timedelta(days=7)


# In[68]:


def summ(*args, **kwargs): # key word arguments
    print(args)
    print(kwargs)

summ(32131, 123, academy='Alif')


# In[73]:


lst = ['apple']
lst[0]
print(dct[1])


# In[77]:


dct = {
    1: 'Alif',
    2: 'Academy',
    'alif': 'uz'
}
for key in dct:
    print(key, dct[key])


# In[79]:


import json


# In[80]:


json.dumps(dct)


# In[81]:


import json
dct = {
    1: '9494',
    2: 12039,
    'alif': 1283
}
with open("some.json", "w") as file:
    # file.read()
    json.dump(dct, file)
    


# In[84]:


import json
with open("some.json", "r") as file:
    data = json.load(file)
    print(type(data))
    print(data)
    # data = file.read()
    # json.dump(dct, file)
    


# In[86]:


Формат ввода
Вводится слово, чье искажение нужно искать.
Затем вводятся строки слов, записанных через пробел.
Формат вывода
Выбрать строки, в которых слово для поиска встречается не как отдельное слово,
а внутри другого, то есть перед ним или после него есть хотя бы по одному символу.
Вывести такие строки в исходном порядке.
Пример 1
Ввод
mud
Johansson and his men
landed on the sloping smuddy shore
of this monstrous Acropolis
climbed up the mud gigantic wet
blocks of an obviously
inhuman amudden staircase

Вывод
landed on the sloping smuddy shore
inhuman amudden staircase

landed, on, the, sloping, smuddy, shore


word = input('Введите слово: ')
for i in range(6):
    line = input('Введите предложение: ')
    line = line.split(' ')
    for el in line:
        if word in el:
            print(line)
            print(' '.join(line))
            break


# In[85]:





# In[88]:


some = lambda a:  a ** a
print(some(10))
# def some(a, b):
#     return a + b


# In[ ]:




