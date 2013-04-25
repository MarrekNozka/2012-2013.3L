#!/usr/bin/python
# -*- coding: utf8 -*-
# Soubor:  loterie.py
# Datum:   25.04.2013 08:33
# Autor:   Marek Nožka, nozka <@t> spseol <d.t> cz
# Licence: GNU/GPL 
# Úloha: 
############################################################################

import random

def losovani(x, minimum=1, maximum=49 ):
    """funkce vrací senzam náhodných čísel
       x ... počet čísel
       minimum ... minimální číslo
       maximum ... maximální číslo
    """
    cisla = []
    while len(cisla) < x :
        a = random.randint( minimum, maximum )
        if (a in cisla) :
            continue 
        else:
            cisla.append(a)
    return cisla    

#s = losovani(20)
#print sorted(s)
#print s

def nacitiData(x, minimum=1, maximum=49 ):
    """
    funkce načte od uživatele x celých čísel
    """
    seznam = []
    while len(seznam)<x :
        try: 
            c = raw_input(' zadej celé číslo > ')
            c = int(c)  # převedu řetězec na číslo
            if c in seznam : 
                print "CHYBA: toto číslo už bylo zadáno!!!"
            elif c < minimum or c > maximum :
                print "CHYBA: číslo musí být v rozsahu <{0},{1}>".format(minimum, maximum)
            else:
                seznam.append(c)
        except:
            print "CHYBA: musíš zadávat jen celá čísla"
    return seznam


"""
Program vyžádá od uživatele 6 čísel jako sázku do leterie, 
provede losování a vypíše kolik čísel uživatel uhodl.
"""

sazka = nacitiData(6)

loterie = losovani(6)

print sazka
print loterie

