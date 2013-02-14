#!/usr/bin/env python
# -*- coding: utf8 -*-
# Soubor:  easyGraph.py
# Datum:   14.02.2013 08:19
# Autor:   Marek Nožka, nozka <@t> spseol <d.t> cz
# Licence: GNU/GPL 
# Úloha:   vykreslí jednoduchý graf ze souboru
###################################################3 

import pylab as lab
from pylab import pi

# zeptám se na jméno souboru
#otevře soubor
try:
#    soubor=raw_input('zadej vstupní soubor: ')
#    f=open(soubor, 'r')
    f=open('graf.txt', 'r')
except IOError:
    print "soubor se nepodařilo otevřít"
    exit(1)
except:
    print "stalo se něco nehezkého"
    exit(2)

# načtu řádek
x = f.readline()
# rozdělím řádek
x = x.split()
# načtu a rodělím druhý řádek
y = f.readline().split()

# převedu řádek na čísla
for i in range( len(x) ):
    x[i] = float( x[i] )
    y[i] = float( y[i] )

#### výpočet hladké křivky
# vytvořím novou osu x
newX = lab.linspace(min(x), max(x),300)
from scipy.interpolate import spline
newY = spline(x,y,newX)

lab.plot(x,y,'rx')
lab.plot(newX,newY,'b-')
lab.grid()
lab.show()

f.close()
exit(0)
