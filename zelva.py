#!/usr/bin/python
# -*- coding: utf8 -*-
# Soubor:  zelva.py
# Datum:   13.12.2012 08:22
# Autor:   Marek Nožka, nozka <@t> spseol <d.t> cz
# Licence: GNU/GPL 
# Úloha:   seznámení s želvou
############################################################################

import turtle as t

# počáteční nastavení
#t.shape("turtle")
t.speed(6)

# podprogram kreslí čtverec
def ctverec(kroky=100):
    t.left(90)
    t.forward(kroky)
    t.left(90)
    t.forward(kroky)
    t.left(90)
    t.forward(kroky)
    t.left(90)
    t.forward(kroky)

# kytka
def kvetCtverec(strana=100, pocet=9):
    for _ in range(pocet):
        ctverec(strana)
        t.left(360./pocet)

# n-úhelník
def nUhelnik(strana=100, n=6, barva="#000000"):
    aktual = t.pencolor()
    t.pencolor(barva)
    uhel = 360./n
    for _ in range(n):
        t.forward(strana)
        t.right(uhel)
    t.pencolor(aktual)

def presun(x,y):
    t.up()
    t.goto(x,y)
    t.down()

###########################################################################

nUhelnik(n=9,barva='#12ea45')

kvetCtverec(pocet=5,strana=288)

presun(-200,-200)
t.pencolor('#c18fab')
kvetCtverec(80,18)

presun(200,-200)
t.pencolor('#328fef')
kvetCtverec(50)

presun(-200,200)
t.pencolor('#32c18f')
kvetCtverec(pocet=20)


t.exitonclick()
