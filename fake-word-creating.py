# -*- coding: utf-8 -*-
"""
Created on Wed Jul 13 21:30:24 2022

@author: W10
"""

consonants = ['b','c','d']
vowel = ['a','e','i']

lexical_units = [b + a + c for b in consonants for a in vowel for c in consonants]


withoutb_lexical_units = []

for i in lexical_units:
    if  not i[0] == 'b':
        withoutb_lexical_units.append(i)
    else:
        pass

with open('withoutb.txt',"a") as f:
    for i in withoutb_lexical_units:
        f.write(i + "\n")
        