'''def function_example(str):
    if x == 'Dimitrios Zanganas':
        print('To onomateponimo sas einai:',str)
    else:
        print('Eisagate lathos onomatepwnymo!')


x = input('Your name is:')
function_example(x)

def function_listadding(list):
    x = list[0]
    y = list[-1]
    k = int(x) + int(y)
    print (k)

q = input('Give me a list:')
function_listadding(q)

file1 = open('workearly.txt', 'w+')
for i in range(10):
      file1.write("The line is %d\r\n" % (i+1))
file1.close()

file1 = open('workearly.txt','r')
if file1.mode == 'r':
      contents = file1.read()
      print(contents)

file1 = open('workearly.txt', 'r')
f2 = file1.readline()
print(f2)

file1 = open('workearly.txt','a')
file1.write('This will add a new line in our file')
file1.close()'''


import numpy as np

arr1 = np.array(5)
arr2 = np.array([1,2,3,4,5,1,2,3,4,5])
arr3 = np.array([[1,2],[3,4]])
arr4 = np.array([[[0,1],[1,2],[8,7]],[[3,4],[4,5],[5,6]]])

'''print(arr1.ndim, arr2.ndim, arr3.ndim, arr4.ndim)
print(arr4[1,2])
print(arr2[2:])
print(arr3[1,0:2])

copy = arr3.copy()
copy[1,1] = 25
print(arr3)
print(copy)
print(arr4)

print(arr2.reshape(2,5))

import numpy as np

arr = np.array([1, 2, 3, 4, 5, 6])

arrList = np.array_split(arr, 5)

for arr in arrList:
    print(arr)
print(np.where(arr2 == 2))

import numpy as np

arr = np.array([2.666, 4.65648, 3.849])
print(np.fix(arr))


import pandas as pd
x = [23,18,49]
my_first_series = pd.Series(x)

print(my_first_series)


import pandas as pd

d1 = { 'Name':['Dimitrios', 'Ioannis', 'Alexandros'],
       'Age':[26, 27, 25],
       'Position':['Data Analyst', 'Doctor','Physiotherapist']}

d2 = { 'Name':['Konstantis', 'Georgios', 'Vasileios'],
       'Age':[26, 27, 25],
       'Position':['Engineer', 'Bartender','Worker']}

df1 = pd.DataFrame(d1, index=[1,2,3])
df2 = pd.DataFrame(d2, index=[4,5,6])

df = pd.concat([df1,df2])

print(df)

import matplotlib.pyplot as plt
import numpy as np


age = np.array([10, 20, 30, 40, 50, 60, 70, 80, 90, 100])

cardiac_cases = np.array([5, 15, 20, 40, 55, 55, 70, 80, 90, 95])

survival_chances = np.array([99, 99, 90, 90, 80, 75, 60, 50, 30, 25])

plt.xlabel('Age')
plt.ylabel('Percentage')

plt.plot(age, survival_chances, marker='o', label='Survival chances', color='green',markerfacecolor='yellow', markersize=12)
plt.plot(age, cardiac_cases, marker='h', label='Cardiac cases', color='black',markerfacecolor='red', markersize=12)
plt.legend()
plt.show()
from bs4 import BeautifulSoup
url = "https://en.wikipedia.org/wiki/List_of_highest-paid_film_actors"
url_txt = requests.get(url).text
s = BeautifulSoup(url_txt, "html.parser")
my_table = s.find('table', class_='wikitable sortable plainrowheaders')
table_links = my_table.find_all('a')
actors = []
for links in table_links:
      actors.append(links.get('title'))
print(actors)'''
