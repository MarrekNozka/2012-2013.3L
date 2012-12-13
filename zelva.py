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

def presun(x,y):
    t.up()
    t.goto(x,y)
    t.down()

###########################################################################

kvetCtverec()

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
