#!/usr/bin/python
# -*- coding: utf8 -*-
# Soubor:  zelva.py
# Datum:   13.12.2012 08:22
# Autor:   Marek Nožka, nozka <@t> spseol <d.t> cz
# Licence: GNU/GPL 
# Úloha:   seznámení s želvou
############################################################################

import turtle as t
import random

def zub(kroky,hloubka):
    if hloubka>random.randint(1,3):
        zub(kroky/3.0, hloubka-1 )
    else:
        t.forward(kroky)
    t.left(60)
    if hloubka>random.randint(1,3):
        zub(kroky/3.0, hloubka-1 )
    else:
        t.forward(kroky)
    t.right(120)
    if hloubka>random.randint(1,3):
        zub(kroky/3.0, hloubka-1 )
    else:
        t.forward(kroky)
    t.left(60)
    if hloubka>random.randint(1,3):
        zub(kroky/3.0, hloubka-1 )
    else:
        t.forward(kroky)

def zubbbb(kroky):
    t.forward(kroky)
    t.left(60)
    t.forward(kroky)
    t.right(120)
    t.forward(kroky)
    t.left(60)
    t.forward(kroky)

############################################################################
t.speed(9)
t.up()
t.goto(-300,0)
t.down()

zub(200,5)

t.exitonclick()
