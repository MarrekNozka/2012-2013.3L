#!/usr/bin/python
# -*- coding: utf8 -*-
# Soubor:  vypocet-pi.py
# Datum:   15.11.2012 09:16
# Autor:   Marek Nožka, nozka <@t> spseol <d.t> cz
# Licence: GNU/GPL 
# Úloha:   vypočet čísla pi
#          http://cs.wikipedia.org/wiki/Pí_(číslo)#Odhad_.CF.80
########################################################## 


jmenovatel = 1.
znamenko = 1.
cisloPI  = 0.

while jmenovatel < 1e9 :
    cisloPI = cisloPI + znamenko*4/jmenovatel
    jmenovatel += 2  #jmenovatel = jmenovatel + 2 
    znamenko *= -1   # znamenko = znamenko * -1

print cisloPI
import math
print math.pi
