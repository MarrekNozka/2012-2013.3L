#!/usr/bin/python
# -*- coding: utf8 -*-
# Soubor:  prerovnani-cisel.py
# Datum:   22.11.2012 08:51
# Autor:   Marek Nožka, nozka <@t> spseol <d.t> cz
# Licence: GNU/GPL 
# Úloha:   Přerovnejte čísla tak, aby na začátku posloupnosti byla všechna
#          záporná čísla v původním pořadí a za nimi všechna nezáporná 
#          čísla opět se zachováním jejich původního pořadí.  
############################################################################

radek = raw_input('zadej čísla >> ')
cisla = radek.split()

# udělám si dvě hromádky
kladnaCisla = [ ] # prázdný seznam
zapornaCisla = [ ]

i = 0
while i<len(cisla):
    polozka = cisla[i]     # vyříznu jednu položku seznamu
    cisilko = float(polozka) # převedu řetězec na číslo
    if cisilko < 0:
        zapornaCisla = zapornaCisla + [ cisilko ]
    else:
        kladnaCisla.append(cisilko)
    i += 1

# vypíšu čísla, co mám na hromádkách
i = 0
while i<len(zapornaCisla):
    print (zapornaCisla[i])
    i += 1

i = len(kladnaCisla)-1
while i>=0:
    print (kladnaCisla[i])
    i -= 1

# a teď se naučíme cyklus FOR
print "############### FOR ################"

for j in 1,2,3,'ahoj',"konc":
    print j

print "############### FOR ################"

kladnaCisla.reverse() # převrátím pořadí
for c in kladnaCisla:
    print c

print "############### FOR ################"

#http://docs.python.org/2.7/library/functions.html?highlight=range#range
for i in range(100,538):
    if i % 29 == 0:
        print i

