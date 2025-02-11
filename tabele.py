# coding: utf-8
import pandas as pd
import csv
import os
import orodja

pot = 'csv/'
datoteka = pot + 'metal_skupine_id.csv'
celotna_tabela = pd.read_csv(datoteka)


def csv_iz_tabele(pot, tabela, stolpci=None):
    if not os.path.isfile(datoteka):
        os.makedirs(pot)
        tabela.to_csv(pot, stolpci)

temp = {1: 'Active', 2: 'On hold', 3: 'Split-up', 4: 'Unknown', 5: 'Changed name', 6: 'Disputed'}
status = []
for oznaka, pomen in temp.items():
    status += [{'status': oznaka, 'pomen': pomen}]
orodja.zapisi_tabelo(status, ['status', 'pomen'], pot + 'statusi.csv')
statusi = pd.read_csv(pot + 'statusi.csv')
statusi_skupin = pd.concat([celotna_tabela['status'], statusi], axis=1)['status', 'pomen']

csv_iz_tabele(pot + 'metal_skupine_id.csv', celotna_tabela[['ime', 'leto']], stolpci=['ime', 'leto'])
csv_iz_tabele(pot + 'zvrsti_skupin.csv', celotna_tabela['zvrst'], stolpci='zvrst')
csv_iz_tabele(pot + 'statusi_skupin.csv', statusi_skupin, stolpci='status')



'''
osnovna_tabela = celotna_tabela['ime', 'leto']
osnovna_tabela = pd.DataFrame.to_csv(pot + 'metal_skupine.csv', columns=['ime', 'leto'])

zvrsti_skupin = celotna_tabela['zvrst'].split(',').apply(pd.Series, 1).stack()
zvrsti_skupin.to_csv(pot + 'zvrsti_skupin.csv', columns=['', ''])

status = {1: 'Active', 2: 'On hold', 3: 'Split-up', 4: 'Unknown', 5: 'Changed name', 6: 'Disputed'}
statusi = pd.DataFrame.from_dict(status)
statusi.to_csv(pot + 'statusi.csv', columns=['pomen'])

statusi_skupin = pd.concat([celotna_tabela['status'], status], axis=1)['status', 'pomen']
statusi_skupin.to_csv(pot + 'statusi_skupin.csv', columns=['status', 'pomen'])
'''
