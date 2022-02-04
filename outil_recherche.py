import os
import time

#Outil de recherche

#commande de l'utilisateur
#commande = input(">>>")

#on decoupe la requete de l'utilisateur et on cherche à quelle fonction
#elle correspond
#reqst = commande.split(" ")
name = ""
size = ""
led = ""
ext = ""

if reqst[0] == "find":
    #parametre de la fonction find:
        #-name
        #-size
        #-led (last edit date)
        #-ext
    # en fonction de la longueur de la liste on cherche les parametres
    for i in range(2, len(reqst)):
        #on cherche tout les parametres
        #nom
        if "-name" in reqst[i]:
            name = reqst[i].split("=")[1]
        #taille
        elif "-size" in reqst[i]:
            size = reqst[i].split("=")[1]
        #date de modification
        elif "-date" in reqst[i]:
            led = reqst[i].split("=")[1]
        #extension 
        elif "-ext" in reqst[i]:
            ext = reqst[i].split("=")[1]

#découvrir le format de la date
print(os.listdir('C:/Users/AdemMADANI/OneDrive - Région Île-de-France/Bureau/NSI'))    

date_fichier = os.stat('C:/Users/AdemMADANI/OneDrive - Région Île-de-France/Bureau/NSI/conversion_bases.txt').st_mtime

print(time.gmtime(date_fichier))

