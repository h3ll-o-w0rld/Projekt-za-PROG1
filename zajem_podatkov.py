# coding: utf-8
import sys
import os
import requests
import re

naslov = 'http://www.metal-archives.com/band/view/id/'

start = 130091 #10 ** 5
end = 250000 #10 ** 6

for id in range(start, end):
    url = naslov + str(id)
    ime_datoteke = '../data1/{:07}'.format(id)
    try:
        print('Shranjujem {}...'.format(url))
        sys.stdout.flush()
        if os.path.isfile(ime_datoteke):
            print('shranjeno že od prej!')
            continue
        r = requests.get(url)
    except requests.exceptions.ConnectionError:
        print('stran ne obstaja!')

    if r.status_code == 404:
        print('stran ne obstaja!')
    else:
        with open(ime_datoteke, 'w') as datoteka:
            datoteka.write(r.text.encode('utf-8'))
            print('shranjeno!')



