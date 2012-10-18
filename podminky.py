# -*- coding: utf8 -*-

# poznámka se píše za dvojkříž

"daší zbůsob jak napsat poznámku je řetězec"

""" toto je víceřádkový řetěze


tady 

ještě 

řádek

ukončím 3x uvozovka"""

a = input(u"zadej číslo prosím : ") 

if a<10:
    print "zadal jsi číslo menší než 10".decode("UTF-8")
    print "chyba"
else:
    print "toto čílo je VĚTŠÍ než 10"    
    
print "teto print se provede vždy"