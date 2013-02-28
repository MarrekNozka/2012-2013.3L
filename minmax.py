#!/usr/bin/python
# -*- coding: utf8 -*-
# Soubor:  minmax.py
# Datum:   28.02.2013 08:40
# Autor:   Marek Nožka, nozka <@t> spseol <d.t> cz
# Licence: GNU/GPL 
# Úloha:   nejmenší a největší prvek v seznamu
############################################################################

import random

def maximum(sezn):
    m=0
    for i in range(len(sezn)):
        if sezn[i]>sezn[m]:
            m=i
    return sezn[m]

def minimum(sezn):
    m=sezn[0]
    for prvek in sezn:
        if prvek < m:
            m=prvek
    return m

############################################################################
seznam = [random.randint(1,100) for _ in range(10)]

print maximum(seznam), max(seznam)
print minimum(seznam), min(seznam)


#############################################################################
# co nabízí Python


def srovnani(a,b):
    """
    srovnávací funkce:
        vrací záprnou hodnotu pokud a<b
        vrací 0 pro a==b
        vrací kladnou hodnotu pro a>b
    """
    if len(a)<len(b):
        return -1
    elif len(a)==len(b):
        return 0
    elif len(a)>len(b):
        return 1


seznam =[ 'ahoj', 'kkkkkkk' ,'cau', 'cus', 'neco dlouheho' ,'ab' ]

print seznam
print sorted(seznam, cmp=srovnani)

