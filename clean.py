# import pandas as pd
# #read data file from desktop of type .csv
# df1= pd.read_csv(r'C:/Users/Dr. Shano/Desktop/moocs recording/files/csv.csv', 'r')
# # print(df1)
# import webbrowser
from urllib import error

# with open(r'C:\Users\apurv\Downloads\Swayam\text file.txt','a') as var:
#   var.write('I am adding new line into text line')


# with open(r'C:\Users\apurv\Downloads\Swayam\text file.txt', 'r') as f:
#  for line in f:
#   print(line)



with open(r'C:\Users\apurv\Downloads\Swayam\text file.txt', 'w') as f:
 f.write('I am learning Python\n')
 f.write('Python is free and open source\n')

with open(r'C:\Users\apurv\Downloads\Swayam\text file.txt', 'r') as f:
 for line in f:
  print(line)

# with open(r'C:\Users\apurv\Downloads\Swayam\text file.txt', 'w') as s:
#  for data in s:
#   print(data)

dict = {
 "name":"apurv",
 "age":"22",
"gender":"male"
}

import json

with open('data.json','w') as f:
 data = json.dump(dict,f)

print(dict)

list = [1,2,3,4]

print(list[3])

with open(r'bookings.txt','a') as f:
     f.write("pax no 1 - kartik\n")
     f.write('pax no 2 - lucy')

try:

        import webbrowse
    # webbrowser.open('youtube.com')

except ModuleNotFoundError:
  print('Please import the required module first')

try:
    divide = 10/0
    print(divide)

except Exception as e:
    print('It is not possible in python to divide by zero')

with open('bookings.txt','r') as f :
     data = f.read()
print(data)

x = 0
y = 4
try:
  if  eval('x==x'):
      print("x is equal to x")
except SyntaxError as e:
      print('not possible')

# import  webbrowser
# try:
#     if NameError:
#        webbrowser.open('helosis09.github.io/Tourcraft')
#
# except NameError as e:
#     print('unknown error')

list = ["apple","banana","kiwi"]

print('index of kiwi is '[0:5])
print(list[0])

import webbrowser
try:
    if NameError:
       webbrowser.open('helosis09.github.io/check')

except NameError:
    print('Unkown error')

finally:
      with open(r'bookings.txt','r') as f:
       Final_var = f.read(56)
       print(Final_var)







