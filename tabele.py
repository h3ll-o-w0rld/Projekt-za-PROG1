# coding: utf-8
import pandas as pd


datoteka = 'skupine.csv'
celotna_tabela = pd.read_csv(datoteka, sep = ',', index_col = 'ime')
celotna_tabela.str.encode('utf-8')
zvrsti = celotna_tabela['zvrst']
statusi = celotna_tabela['status']
drzave = celotna_tabela['drz']
osnovna_tabela = celotna_tabela[['ime', 'leto']]
print(osnovna_tabela)
