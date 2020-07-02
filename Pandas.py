# -*- coding: utf-8 -*-
'''
Created on Thu Jul  2 09:12:48 2020

@author: Dewald
'''

import pandas as pd
from pandas import DataFrame

ilist1 = ['Simba','Coke','Cadbury','Pepper Steak','Pear','Vanilla','Spinach']
ilist2 = ['Lays','Fanta','Tex','Chicken','Apple','Chocolate','Cabbage']
ilist3 = ['','','','','Orange','','']

df = pd.DataFrame([(ilist1),
                    (ilist2),
                    (ilist3)],
                  index=['1','2','3'],
                  columns=('Chips', 'Cooldrinks','Chocolates','Pies','Fruit','Cupcakes','Veggies'))
 
print(df)