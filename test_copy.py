
import shutil
import os 

#outil de copie 
commande = input(">>>")


reqst = commande.split(" ")
source=""
destination=""

if reqst[0] == "copy":
    #source
    source = reqst[1]
    #destination
    destination = reqst[2]
            
            


shutil.copyfile(source,destination)
