#!/usr/bin/python
# -*- coding: utf8 -*-
# Soubor:  cifry.py
# Datum:   07.03.2013 09:00
# Autor:   Marek Nožka, nozka <@t> spseol <d.t> cz
# Licence: GNU/GPL 
# Úloha:   všechna dvouciferná čísla
############################################################################


x=21
print x,
print 20,30,
print 20,30,
print 20,30,
print 20,30,

cifSoucet=raw_input('zadej ciferný součet > ')

for i in range(1,10):
    for j in range(10):
        if i+j == int(cifSoucet) :
            print "{0}{1}".format(i,j)


x = -20
x = x if x>=0 else -x
x=abs(x)
print '\n',x



cisla =[-129, 598, 496, 568, 59, -125, 48312, 5893, 12, 34569, 4521]

#for c in cisla:
#    prac = abs(c)
#    retezec = str(prac)
#    i=0
#    Tisk = False
#    while i<len(retezec)-1:
#        if int(retezec[i]) < int(retezec[i+1]):

#        else:
#            break
#        
#        i+=1
#    if Tisk :
#        print c


