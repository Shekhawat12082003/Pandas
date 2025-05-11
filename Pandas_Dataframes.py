
import numpy as np
import pandas as pd

"""# **Creating Dataframes**"""

# Using lists
Students_Data = [
    [100,80,10],
    [98,70,8],
    [80,58,2]
]
pd.DataFrame(Students_Data,columns=['iq','marks','dataframes'])

# Using Dicts
Students_Data = {
    'iq':[100,98,80],
    'marks':[80,70,58],
    'dataframes':[10,8,2]
}
pd.DataFrame(Students_Data)

# using read_csv
ipl = pd.read_csv('/content/ipl-matches (1).csv')
pd.DataFrame(ipl)

movies = pd.read_csv('/content/movies (1).csv')
pd.DataFrame(movies)

"""# **DataFrames Attributes and Methods**"""

# Shapes
movies.shape

ipl.shape

# dtypes
movies.dtypes

ipl.dtypes

# Index
ipl.index

# Column
ipl.columns

# Head and Tail
movies.head()

movies.tail()

# Samples
ipl.sample()

ipl.info()

# Describe
movies.describe()

# isnull
ipl.isnull().sum()
# This function id used for define how many missing value are in dataset

# Duplicate - duplicate function is used for findind duplicate in dataset & if we add sum it wil add all true data and provide us output or if u want to change data name permanently we use inplace function as true
ipl.duplicated().sum()

# Rename - Used for rename columns in Datasets
ipl.rename(columns={'city':'City'})

# .iloc[] is primarily integer-based indexing for selection by position.
# It allows selecting rows and columns by their integer index.
ipl.iloc[1]

# loc - search using indexing
ipl.loc[54]

# Filtring a dataframe
# find all the final winner
mask=ipl['MatchNumber'] =='Final'
df= ipl[mask]
df[['Season','WinningTeam']]

# Adding New Columns
movies ['Country'] = "India"
movies.head()

#  astypes
ipl['ID'].astype('int32 ')
