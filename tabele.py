# coding: utf-8
import pandas as pd
import csv

datoteka = 'skupine.csv'
celotna_tabela = pd.read_csv(datoteka, sep = ',', index_col = 'ime')
celotna_tabela.str.encode('utf-8')
zvrsti = celotna_tabela['zvrst']
statusi = celotna_tabela['status']
drzave = celotna_tabela['drz']
osnovna_tabela = celotna_tabela['leto']

osn_slovarji = [
    {'ime': line['ime'], 'leto': line['leto']} for line in osnovna_tabela
    ]

with open('osnovno.csv', 'w') as csv_dat:
    writer = csv.DictWriter(csv_dat, fieldnames=['ime', 'leto'])
    writer.writeheader()
    for slovar in osnovna_tabela:
        writer.writerow(slovar)


