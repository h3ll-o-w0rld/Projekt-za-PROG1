# coding = utf-8
import os
import requests
import re
import sys
import orodja

naslov = 'http://www.metal-archives.com/band/view/id/'
koliko_dt = 100

vzorec = r'"band_name">.*?<.*?>(?P<ime>.+?)<\/a>(.|\s)*?'  + \
         r'Country of origin.*?\s.*?<a.*?>(?P<drz>.+?)<(.|\s)*?' + \
         r'Status(.|\s)*?<dd.*?>(?P<status>.+?)<(.|\s)*?' + \
         r'Formed in(.|\s)*?<dd.*>(?P<leto>.+?)<(.|\s)*?' + \
         r'Genre(.|\s)*?<dd>(?P<zvrst>.+?)<'      
regex = re.compile(vzorec)

stolpci = ['id', 'ime', 'država', 'zvrst', 'leto', 'status']


for dtisoc in range(koliko_dt):
    ogromen_seznam = []
    for n in range(10000):
        id = dtisoc * 10000 + n
        # Vsaka spletna stran z informacijami o skupini ima svoj ID,
        # ki je največ 10-mestno število.
        url = naslov + str(id)
        r = requests.get(url)
        if r.status_code == 404:
            continue
        else:
            skupina = re.finditer(regex, r.text)
            for s in skupina: 
                ogromen_seznam += [{'id': id,
                             'ime': (s.group('ime')).encode('utf-8') ,
	                         'država': s.group('drz'),
	                         'zvrst': s.group('zvrst'),
	                         'leto': pocisti_leto(s.group('leto')),
	                         'status': s.group('status')
	                         }]
    izpis = 'csv/{:03}.csv'.format(dtisoc)
    orodja.zapisi_tabelo(ogromen_seznam, stolpci, izpis)
    print('{}% opravljeno'.format((dtisoc + 1)*100/koliko_dt))



