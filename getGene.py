import pandas as pd
import tkinter as tk


df = pd.read_csv('GeneTable.csv', sep=';'  , engine='python')

print("Insert gene Symbol to find possible affymetrix formats")

gene = input()

df = df.loc[df['Gene Symbol'] == gene]

print(df[['ID', 'Sequence Type']]);

