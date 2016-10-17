# coding: utf-8
import pandas as pd
import csv

status = {1: 'Active', 2: 'On hold', 3: 'Split-up', 4: 'Unknown', 5: 'Changed name', 6: 'Disputed'}

datoteka = 'skupine.csv'
celotna_tabela = pd.read_csv(datoteka, sep = ',', index_col = 'ime')
celotna_tabela.str.encode('utf-8')
zvrsti = celotna_tabela['zvrst']
statusi = celotna_tabela['status']
drzave = celotna_tabela['drz']
osnovna_tabela = celotna_tabela['leto']

s = ['ime', 'leto']
osnovna_tabela.to_csv('osnovno.csv', cols=2, header=s)


