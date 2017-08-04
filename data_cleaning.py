import pandas as pd
import numpy as np

trump = pd.read_csv('data/trump.csv')
clinton = pd.read_csv('data/clinton.csv')

columns = trump.columns.values

trump = trump.iloc[:,:-1]
trump.reset_index(inplace= True)
trump.columns = columns

clinton = clinton.iloc[:,:-1]
clinton.reset_index(inplace= True)
clinton.columns = columns

data = pd.concat([trump, clinton], axis = 0)

data.to_csv('data/donor_data.csv')

