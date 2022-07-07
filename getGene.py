import pandas as pd
import tkinter as tk


df = pd.read_csv('GeneTable.csv', sep=';'  , engine='python') #read csv

print("Insert gene Symbol to find possible affymetrix formats")

gene = input()

df = df.loc[df['Gene Symbol'] == gene] #find Affymetrix format

print(df[['ID', 'Sequence Type']]); 

