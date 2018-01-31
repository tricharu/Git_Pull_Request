'''
This will tell you what is list comprehension with examples
'''
'''
List Comprehension Syntax

list_name=[expression(i) for i in old_list if filter(i)]
'''

# we will do the suqare of the number using for loop and list comprehension

x=[1,2,3,4,5]
square_x=[]

# common logic using list_comprehension
for i in x:
  square_x.append(i*i)
 print(square_x)
 
 
 # benefit of list comprehension
 print([i*ior i in x])
