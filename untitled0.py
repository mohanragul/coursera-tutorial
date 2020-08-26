# -*- coding: utf-8 -*-
"""
Created on Wed Oct  2 21:56:39 2019

@author: admin
"""
a=45
b=12
print(a,b)
print(a+b)
print(a-b)
print(a//b)
print (a**b)
male,female,Tg=1,12,3
print(male*female*Tg)
type(male) is float
a+=male
print(a)
print(female!=b)
#list creating
#following three are top level components
id=[1,2,3,4,5]
employee_name=["a","b","c","d","e"] #strings are in double cotation ""
num_emp=[5]
#this is sub level component
emp_list=[id,employee_name,num_emp]# here v define a list then v print by following comment
print(emp_list)
#indexing or accessing the index
employee_name[-1]#-ve index
employee_name[3]#+veindex
print(employee_name[4],employee_name[1])# these are calls using index numbers or also (or) accessing top and sub level components
employee_name.index("e")# this is getting the index number using the element
print(emp_list[1])
print(emp_list[1][4])#[1] refers to employee_name, [4] refers to "e" so v access e in the list "employee_name"
#modifying the list  using index
emp_list[1][3]="f" # here v have renamed "d" as "f"
print(emp_list)
emp_list[0][3]=8# here v have renamed 4 as 8
print(emp_list)
# adding elements to a list
# append() command is used to add a list or element at last of a list
emp_list[0].append(6)
emp_list[1].append("h")
print(emp_list)
emp_list[2].append(6)
print(emp_list)
# adding list to a list
age=[2,3,6,9,8,7]
emp_list.append([age]) #we added the list 'age' to the list 'emp_list'
print(emp_list)
# adding list or element at a specific point using insert()
emp_list[1].insert(3,"p") # (3,"p") in this 3 is the top level and p is the value to be replaced
# removing an element or list using the command del
del emp_list[3] # here v remove the list 'age'
print(emp_list)
# removing an element or list using the command remove()
emp_list[2].remove(5) # v have removed the element 5 in list 2
print(emp_list)
# knowing the element going to be removed and if u print the list that element would have been removed
emp_list[1].pop(3)
print(emp_list)
# creating a tuple and accessing using indrx
emplyee_details=("p12",'ram',12,50000,'ex12',859)
print(emplyee_details)
print(emplyee_details[3])
#slicing a tuple
print(emplyee_details[0:3])
print(emplyee_details[:4]) # prints the value upto index value 3 from the beginning
# length of tuple
len(emplyee_details)
# finding min & max in a tuple
height=(78,89,52,63,41,45,56,65)
min(height)
max(height)
# adding two tuples
emplyee_details2=("aa",12)
print(emplyee_details+emplyee_details2)
#adding two tuples and saving in new variable
new=(emplyee_details+emplyee_details2)
print(new)







