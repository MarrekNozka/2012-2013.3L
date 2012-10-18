# -*- coding: utf8 -*-

""" 
ukázka cyklu while
"""

print "Násobíme 4x"

cislo = 1
while cislo <= 10 :
    print "4 x", cislo, "=", cislo*4
    cislo = cislo + 1
print "To je KONEC"


print "== Malá násobilka =="

a = 1
while a <= 10:
    b = 1
    while b <= 10:
        print a, "x", b, "=", a*b
        b = b+1
    a = a+1
    print '-------------------------'