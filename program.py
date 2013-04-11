#!/usr/bin/env python
# -*- coding: utf8 -*-
# Soubor:  program.py
# Datum:   11.04.2013 08:35
# Autor:   Marek Nožka, nozka <@t> spseol <d.t> cz
# Licence: GNU/GPL 
# Úloha:   Program pro demonstraci práce s moduly
###################################################3 

import veVyuce

# funkce obsah má proměný počet parametrů
print veVyuce.obsah(1,3,8)
print veVyuce.obsah(4,8)


# rozbalení seznamu
# hvězdička zajistí, že seznam se rozbalí
seznam = [5,7,12]
print veVyuce.obsah( *seznam )


print veVyuce.cisloPi
print veVyuce.pi()
veVyuce.cisloPi = 12345
print veVyuce.cisloPi
print veVyuce.pi()

print '###################################################'
# provede se KOPÍROVÁNÍ modulu do aktuálního jmenného prostoru
from veVyuce import * 

print cisloPi
print pi()
cisloPi = 654
print cisloPi
print pi()

print obsah(9,8,7)


# kde hledá python moduly
import sys

sys.path += ['muj/adresar/s/modulama']

print sys.path
