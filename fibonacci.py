#!/usr/bin/python
# -*- coding: utf8 -*-
# Soubor:  fibonacci.py
# Datum:   06.12.2012 08:45
# Autor:   Marek Nožka, nozka <@t> spseol <d.t> cz
# Licence: GNU/GPL 
# Úloha:   Fibonacciho posloupnost
#          http://cs.wikipedia.org/wiki/Fibonacciho_posloupnost
############################################################################

mIndex = input("zadej maximální index > ")

if mIndex<0:
    print "Chyba: číslo nesmí být záporné"
elif mIndex == 0:
    print 0
elif mIndex == 1:
    print 0,1
else: 
    print 0,1,
    F_2 = 0
    F_1 = 1
    i = 2 
    while i<=mIndex :
        i=i + 1
        Fn= F_2 + F_1
        print Fn,
        F_2 = F_1
        F_1 = Fn
