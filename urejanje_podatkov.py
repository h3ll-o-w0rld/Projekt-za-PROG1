# coding: utf-8
import re
import os
import orodja
import re

# preverjeno deluje:
#"band_name">.*?>(.+?)<.*?(.|\s)*?Country of origin.*?\s.*?<a.*?>(.+?)
#Country of origin.*?\s.*?<a.*?>(.+?)<(.|\s)*?Status(.|\s)*?<dd.*>(.+?)<
#Status(.|\s)*?<dd.*?>(.+?)<(.|\s)*?Formed in(.|\s)*?<dd>(.+?)
#Formed in(.|\s)*?<dd>(.+?)<(.|\s)*?Genre(.|\s)*?<dd>(.+?)

vzorec = r'"band_name">.*?<.*?>(?P<ime>.+?)<\/a>(.|\s)*?'  + \
         r'Country of origin.*?\s.*?<a.*?>(?P<drz>.+?)<(.|\s)*?' + \
         r'Status(.|\s)*?<dd.*?>(?P<status>.+?)<(.|\s)*?' + \
         r'Formed in(.|\s)*?<dd.*>(?P<leto>.+?)<(.|\s)*?' + \
         r'Genre(.|\s)*?<dd>(?P<zvrst>.+?)<'      
regex = re.compile(vzorec)

status = {1: 'Active', 2: 'On hold', 3: 'Split-up', 4: 'Unknown', 5: 'Changed name', 6: 'Disputed'}
nazaj_status = {'Active': 1, 'On hold': 2, 'Split-up': 3, 'Unknown': 4, 'Changed name': 5, 'Disputed': 6}

ostali_bandi = [
                ['Hatebreed', 'United States', 'Metalcore', 1994, 1],
                ['Slipknot', 'United States', 'Nu', 1995, 1],
                ['Korn', 'United States', 'Nu,Groove,Industrial', 1993, 1],
                ['Biohazard', 'United States', 'Crossover,Thrash', 1987, 1],
                ['Limp Bizkit', 'United States', 'Nu', 1994, 1],
                ['Between the Buried and Me', 'United States', 'Progressive', 2000, 1],
                ['Rammstein', 'Germany', 'Industrial', 1994, 1],
                ['Bullet for My Valentine', 'United Kingdom', 'Metalcore', 1993, 1],
                ['Converge', 'United States', 'Mathcore', 1990, 1],
                ['Skindred', 'United Kingdom', 'Reggae,Nu', 1998, 1],
                ['Five Finger Death Punch', 'United States', 'Groove', 2005, 1],
                ['System of a Down', 'Armenia', 'Nu,Progressive,Art Rock', 1994, 1],
                ['Drowning Pool', 'United States', 'Alternative,Post-Grunge', 1996, 1],
                ['TesseracT', 'United States', 'Progressive,Djent', 2003, 1],
                ['Jeff Killed John', 'United Kingdom', 'Nu', 1998, 5],
                ['Brawl', 'United States', 'Nu', 1994, 5]
]

sezn_skupin = [{'ime': o[0], 'država': o[1], 'zvrst': o[2], 'leto': o[3],
                'status': o[4]} for o in ostali_bandi]


def pocisti_leto(vnos):
    '''Iz niza, ki predstavlja leto ustanovitve, pobere prvo letnico.'''
    if vnos in 'N/A':
        return float('nan')
    leto = vnos[:4]
    if unicode(leto, 'utf-8').isnumeric:
        return int(leto)
    else:
        return float('nan')

vzorec_zvrsti = re.compile(r"\b([A-Z]|[a-z]).*?\b|[A-Z].*? ?'?n'? ?Roll|[A-Z].*?( |-)+?Rock|Bossa Nova|Middle Eastern|" + \
                          r"Post-.*?\b|Avant-(g|G)arde|Oi!|A Cappella|(Tr|H)ip-?Hop|Harsh Noise Wall|Post-Metal")
izjeme = ['Metal', 'metal', 'Raw', 'Post', 'Influences', 'Avant', 'Elements', 'Roll', 'present',
          'with', 'influences', 'elements', 'of', 'influence', 'early', 'later', 'garde', 'after', 'With'
          'demo', 'first', 's', 'n', 'and', 'mid', 'until', 'on', 'Satanavoid', 'Screaming', 'Machines']

def pocisti_zvrst(niz, vzorec, izjeme):
    '''Poišče besede in jih pretvori v zaporedje, ločeno z vejicami.'''
    vse_zvrsti = []
    seznam_zvrsti = [zvrst.group() for zvrst in re.finditer(vzorec, niz) if zvrst.group() not in izjeme]
    seznam_zvrsti = list(set(seznam_zvrsti))
    izjema1, izjema2 = 'Rautalanka', 'Jazzy'
    zam1, zam2 = 'Folk', 'Jazz'
    if izjema1 in seznam_zvrsti:
        mesto1 = seznam_zvrsti.index(izjema1)
        seznam_zvrsti[mesto1] = zam1
    if izjema2 in seznam_zvrsti:
        mesto2 = seznam_zvrsti.index(izjema2)
        seznam_zvrsti[mesto2] = zam2
    return ','.join(seznam_zvrsti)


for n in range(14):
    file = '../proj_csv/dtisoc/dtisoc{:04}.txt'.format(n)
    with open(file, 'r') as d:
	    vsebina = d.read()
	    nove_skupine = re.finditer(regex, vsebina)
	    for s in nove_skupine:
	        sezn_skupin += [{'ime': s.group('ime') ,
	                         'država': s.group('drz'),
	                         'zvrst': pocisti_zvrst(s.group('zvrst'), vzorec_zvrsti, izjeme),
	                         'leto': pocisti_leto(s.group('leto')),
	                         'status': nazaj_status[s.group('status')]
	                         }]

stolpci = ['ime', 'država', 'zvrst', 'leto', 'status']
izpis = 'metal_skupine1.csv'

orodja.zapisi_tabelo(sezn_skupin, stolpci, izpis)


