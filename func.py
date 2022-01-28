# -*- coding: utf-8 -*-
"""
Created on Fri Jan 28 22:20:49 2022

@author: Botir
"""

from baza import krill, lot

def asosiy(shart,text):
    if shart.lower() == "krill":
        lotin_to_krill(text)
            
    elif shart.lower() == "lotin":
        krill_to_lotin(text)
            
            
    else:
        print("Bizda unaqa format yo'q qayta urinib ko'ring ")
            
def lotin_to_krill(text):
    new_text = ''
    for harf in text:
        n = 0
        while True:
            if lot[n] == harf:
                new_text = f"{new_text}{krill[n]}"
                break
            else: n+=1
    print(new_text)
    
def krill_to_lotin(text):
    new_text = ''
    for harf in text:
        n = 0
        while True:
            if krill[n] == harf:
                new_text = f"{new_text}{lot[n]}"
                break
            else: n+=1
    print(new_text)
   