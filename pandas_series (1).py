import pandas as pd
import numpy as np

"""# **Series from list**"""

# String
name= ["Gagandeep","Sumit","Rahul","Aryan"]

pd.Series(name)

# Integers
age = [21,22,17,19]

pd.Series(age)

marks = [99,95,93,98]
subjects = ["Maths","Physics","Chemistry","Biology"]

pd.Series(marks,index=subjects)

"""# **Series from Dist**"""

x = {

         'English':99
         ,'Maths':95
         ,'Physics':93
         ,'Chemistry':98

}

marks = pd.Series(x)
marks

"""# **Series using read_csv**"""

# With one col
subs = pd.read_csv('/content/subs.csv')
subs

# with 2 cols
vk=pd.read_csv('/content/kohli_ipl.csv',index_col='match_no')
vk

bollywood=pd.read_csv('/content/bollywood.csv',index_col='movie')
bollywood

"""# **Series method**"""

# Head and Tail
subs.head()

subs.tail()

# Sample
bollywood.sample(5)

# value count
bollywood.value_counts()

"""# **Series Maths Methods**"""

# Count
subs.count()

# Sums -> Product
subs.sum()

subs.product()

# mean -> mode -> Median -> std -> var
subs.mean()
print(subs.mode())
print(subs.median())
print(subs.std())
print(subs.var())

# min -> max
subs.min()

subs.max()

"""# **Series Indexing**"""

x=pd.Series([1,2,3,4,5,6,7,8,9])
x

# integer indeing
x[6]

# Slicing
vk[1:6]

vk[-5:]

"""# **Editing Series**"""

marks

# Using Indexing
marks[2]=100
marks

