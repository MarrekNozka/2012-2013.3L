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


t = lab.linspace(0,10,100)
u = lab.zeros(100) 

hodnota=0
prirustek=0.1
j=0 # index vzorku

while j<len(u):
    while hodnota<2 and j<len(u):
        u[j] = hodnota
        j+=1
        hodnota += prirustek
    while hodnota>0 and j<len(u):
        u[j] = hodnota
        j+=1
        hodnota -= prirustek


lab.plot(t,u)
lab.grid()

lab.show()


