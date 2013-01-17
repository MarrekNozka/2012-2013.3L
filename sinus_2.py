#!/usr/bin/env python
# -*- coding: utf8 -*-
# Soubor:  sinus.py
# Datum:   17.01.2013 08:24
# Autor:   Marek Nožka, nozka <@t> spseol <d.t> cz
# Licence: GNU/GPL 
# Úloha: 
###################################################3 

import pylab as lab

t = [ 0.1, 0.2, 0.25, 0.46 ]
u = [   1,  3 ,  3.5, 3.8  ]


lab.figure(1)
lab.plot(t,u,'g--o', markeredgecolor='blue')     # kreslení

lab.xlim(0,0.6)   # nastavím začátek a konec os
lab.ylim(-1,5)

lab.title(u'Můj první graf $x_{12} = \\frac{-b\\pm\\sqrt{D}}{2a}$')
lab.xlabel('t[s]')  # popisek os
lab.ylabel('$u_1[V]$')

lab.grid()  # mřížka

##################################################
# teď už fakt nakreslím ten sinus

from pylab import pi

f =  3 # frakvence
fi = lab.deg2rad(60) # počáteční fáce

# vytvořím časovou osu
t = lab.linspace(0,1,1000)

# vypočítám napětí pro všechny časy
u = 3*lab.sin(2*pi*f*t+fi)


lab.figure() # nový obrázek
lab.plot(t,u,':')
lab.title('Funkce sinus')
lab.xlabel('t[s]')
lab.ylabel('u[V]')
lab.grid()

lab.ylim(1.1*min(u), 1.1*max(u))

lab.text(0.1, 2.5, u'Toto je můj duchaplný text')

################################################
# ještě jeden graf do stejného obrázku

for i in range( len(u) ):
    if u[i]>2 :
        u[i] = 2
    elif u[i]<-2:
        u[i] = -2

for i in range( len(u) ):
    if u[i]<0 :
        u[i] = -u[i] 

import numpy
numpy.abs(u)        

lab.plot(t,u,'-')



lab.show()

