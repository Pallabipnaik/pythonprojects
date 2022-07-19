#!/usr/bin/env python
# coding: utf-8

# In[120]:


print ("______________Calculator________________\n")

a = float(input("First number"))
operator = str(input("What do you want to do: add, subtract, divide, multiply \n"))
b = float(input("Second number \n"))

def cal():
    if operator == "add" or "+":
            res = (a+b)
    elif operaor == "subtract" or "-":
            res = (a-b)
    elif operator == "divide" or "/":
            res = (a/b)
    elif operator == "multiply" or "*" "X":
            res = (a*b)
    else:
        print ("Enter a valid input")
        
print ("\nThe result is", str(res))

print ("_"*50)

cal()




# In[ ]:





# In[ ]:




