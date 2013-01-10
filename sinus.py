#!/usr/bin/env python
# -*- coding: utf8 -*-
# Soubor:  sinus.py
# Datum:   10.01.2013 08:58
# Autor:   Marek Nožka, nozka <@t> spseol <d.t> cz
# Licence: GNU/GPL 
# Úloha:   kreslím sinus
# Popis:   Tutoriál k PyLab
###################################################3 

import pylab as lab
import numpy
from numpy import pi


cisla = lab.zeros(10)
print "\nzeros(10)\n", cisla

cisla = lab.ones(10)
print "\nones(10)\n", cisla

bagr = lab.linspace(0,5,10)
print "\nlinspace(0,5,10)\n", bagr

kybl = lab.arange(0,10,2)
print "\narange(0,10,2)\n", kybl

print numpy.array([0,1,2,3]) + \
      numpy.array([5,6,7,8])
############################################################
#   sinus

t = lab.linspace(0,1,100)
f=3
u = lab.sin(2*pi*f*t)
lab.plot(t,u)


u2 = lab.sin(2*pi*f*t)
for i in range(len(u2)):
    u2[i] =  abs(u2[i])

lab.plot(t,u2)

lab.show()
