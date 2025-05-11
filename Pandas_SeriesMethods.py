

import numpy as np
import pandas as pd

subs = pd.read_csv('/content/subs (1).csv')
vk = pd.read_csv('/content/kohli_ipl (1).csv')
movies = pd.read_csv('/content/bollywood (1).csv')

# astype
import sys
sys.getsizeof(vk)

sys.getsizeof(vk.astype('int32'))

# Between
vk[vk.between(20,40)].size

# drop_duplicates- In this command the duplicate data will be deleted
pd = pd.Series([1,1,1,2,2,2,3,4,4,3])
pd.drop_duplicates()

vk.drop_duplicates()

# Dropna
pd.dropna()

# isin- isin() checks if values are in a list and returns a boolean mask
vk[vk.isin([49,99])]

# apply- apply() applies a function to rows or columns
movies .apply(lambda x:x.split()[0])

# copy
new = vk.head(5)

new = vk.head().copy()
