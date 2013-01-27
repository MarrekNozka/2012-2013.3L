#!/usr/bin/python
# -*- coding: utf8 -*-
# Soubor:  pila.py
# Datum:   24.01.2013 09:01
# Autor:   Marek Nožka, nozka <@t> spseol <d.t> cz
# Licence: GNU/GPL 
# Úloha:   časový průběh pila ( trojuhelník) 
############################################################################
import matplotlib as mpl
mpl.use('GTKAgg')
mpl.use('Qt4Agg')
#mpl.rc('font',**{'family':'sans-serif','sans-serif':['Helvetica']})
## for Palatino and other serif fonts use:
#mpl.rc('font',**{'family':'serif','serif':['Palatino']})
#mpl.rc('lines', linewidth=2, color='r')
mpl.rc('font', family = 'serif', serif = 'cmr10') 
mpl.rcParams['text.usetex']=True
mpl.rcParams['text.latex.unicode']=True

import numpy as num
import scipy as sci
import pylab as lab
from pylab import pi

############################################################################


x = lab.linspace(0,10,100)
y = lab.zeros(100) 

H=0
D=0.1
i=0
while i<len(y):
    while H<2 and i<len(y):
        y[i] = H
        i += 1
        H += D
    while H>0 and i<len(y):
        y[i] = H
        i += 1
        H -= D

lab.plot(x,y)
lab.grid()

lab.show()


