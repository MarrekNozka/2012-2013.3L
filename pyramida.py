#!/usr/bin/python
# -*- coding: utf8 -*-
# Soubor:  pyramida.py
# Datum:   29.11.2012 08:18
# Autor:   Marek Nožka, nozka <@t> spseol <d.t> cz
# Licence: GNU/GPL 
# Úloha:   tiskne pyramidu ze znaků
############################################################################

import random
############################################################################
pRadku = input('zadej počet řádků > ')

pMezer = pRadku - 1
pZnaku = 1

# znaky z kterých bude pyramida
znaky = tuple(u'@#$%^&*+μωχκΧνε!\\/?><,.')

for i in range( pRadku ) :
    radek = ''
    for j in range( pZnaku ):
        #radek += znaky[ random.randint(0, len(znaky) -1 ) ]
        # nahodne číslo v rozsahu indexů proměnné 'znaky'
        nahoda = random.randint(0,len(znaky)-1)
        # nahodny znak
        znak = znaky[ nahoda ]
        # přidám do řádku náhodný znak
        radek = radek + znak
    print pMezer*' ' + radek
    pZnaku += 2
    pMezer -= 1

