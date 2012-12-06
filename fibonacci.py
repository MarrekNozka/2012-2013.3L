#!/usr/bin/python
# -*- coding: utf8 -*-
# Soubor:  fibonacci.py
# Datum:   06.12.2012 08:45
# Autor:   Marek Nožka, nozka <@t> spseol <d.t> cz
# Licence: GNU/GPL 
# Úloha:   Fibonacciho posloupnost
#          http://cs.wikipedia.org/wiki/Fibonacciho_posloupnost
############################################################################

def Fib(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else: 
        (F_2, F_1 ) =( 0, 1 )
        i = 2 
        while i<=n :
            i +=  1
            Fn= F_2 + F_1
            ( F_2 , F_1 ) = ( F_1, Fn )
        return Fn

# rekurzivní definice
def FibR(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else: 
        return FibR(n-2) + FibR(n-1)

############################################################################
mIndex = input("zadej maximální index > ")

print Fib(mIndex)
print FibR(mIndex)
