import os
import time

#Outil de recherche

#commande de l'utilisateur
commande = input(">>>")

#on decoupe la requete de l'utilisateur et on cherche à quelle fonction
#elle correspond
reqst = commande.split(" ")
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
    
    #recuperer le chemin du dossier
    chemin = reqst[1]
            
    repertoire = os.listdir(chemin)
    #resultat de la recherche
    arborescence = []
    #liste de fichier qui correspondent aux critères
    
    bon_nom = []
    bon_taille = []
    bon_date = []
    bon_ext = []
    
    #on prend chaque critère s'il n'est pas vide
    if name != "":
        for file in repertoire:
            if name in file:
                #ajouter le fichier à la liste de nom correct
                bon_nom.append(file)
    
    if size != "":
        for file in repertoire:
            if size in os.stat(chemin + file).st_size:
                bon_taille.append(file)
    if led != "":
        for file in repertoire:
            date_fichier = os.stat(chemin + file).st_mtime
            date_fichier = time.gmtime(date_fichier)
            jour = date_fichier.tm_mday
            mois = date_fichier.tm_mon
            annee = date_fichier.tm_year
            #format de la date AAAA-MM-JJ
            rch_annee = led.split("-")[0]
            rch_mois = led.split("-")[1]
            rch_jour = led.split("-")[2]
            
            if annee == rch_annee and jour ==rch_jour and mois==rch_mois:
                bon_date.append(file)
    if ext != "":
        for file in repertoire:
            if ext in file:
                bon_ext.append(file)


