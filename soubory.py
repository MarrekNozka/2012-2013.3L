#!/usr/bin/python
# -*- coding: utf8 -*-
# Soubor:  soubory.py
# Datum:   07.02.2013 08:56
# Autor:   Marek Nožka, nozka <@t> spseol <d.t> cz
# Licence: GNU/GPL 
# Úloha:   Práce se soubory
############################################################################

# otevření souboru
#   r - otevřu pro čtení -- soubor musí existovat
#   w - otevřu pro zápis -- soubor bude vždy přepsán nebo vytvořen
#   a - (append) přidání na konec souboru
#   r+, w+ - oteveřní pro čtení a zápis nebo zápis a čtení.
#   pridám b - binární režim => na Windows znamená \r \r a \n \n
#   v textovém režumu na Windows \n znamená \r\n

import sys

f = open("soubor.txt","r")

# f je tzv. ovladač -- handler

#čtu zadaný potet bytů
znak = f.read(1)
print znak
znak = f.read(1)
print znak
znak = f.read(1)
print znak 
f.seek(0)  # přesune na začátek souboru
while True:
    znak = f.read(1)
    if znak == '':  # pokud dojdu na konec souboru .read() vrátí prázdný řetězec
        break       # vyskočím z cyklu
#    print znak,    # print nechci protože tisne mezeru nebo '\n' navíc
    sys.stdout.write(znak)

f.seek(0)  # přesune na začátek souboru
cislo =1
while True:
    radek = f.readline()
    if radek == '':  # pokud dojdu na konec souboru .read() vrátí prázdný řetězec
        break       # vyskočím z cyklu
    print cislo,':', radek,
    cislo +=1

f.close() # zavře soubor
###########################################################################
# zápis do souboru
f = open("souborW.txt","w")

f.write("ahoj jak to jde\n")
f.write("je to tu fakt fakt moc moc\n")
f.write("SUPER\n")
f.write("tady nebude")
f.write("konec radku")

f.close() # zavře soubor
