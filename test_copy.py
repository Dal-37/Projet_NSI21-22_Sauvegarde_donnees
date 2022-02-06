# -*- coding: utf-8 -*-
"""
Created on Fri Feb  4 10:09:05 2022

@author: zakiharafa
"""

import shutil
import os 

#outil de copie 
commande = input(">>>")


reqst = commande.split("")
source=""
destination=""

if reqst[1] == "copy":
    #source
    
    for i in range(2 , len(reqst)):
        if "source" in reqst[i]:
            source = reqst[i].split("=")[1]
           #destination 
        elif "destination" in reqst[i]:
            destination = reqst[i].split("=")[2]
            
            
print(os.listdir(''))


shutil.copyfile(source,destination)
shutil.copy2(source,destination)
