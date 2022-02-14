import os
import time
import shutil

#Outil de recherche

#commande de l'utilisateur
commande = input(">>>")

#on decoupe la requete de l'utilisateur et on cherche à quelle fonction
#elle correspond
reqst = commande.split(" ")
#outil de recherche
name = ""
size = ""
led = ""
ext = ""

#outil de copie
source=""
destination=""

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
    resultat = []
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
            if size == os.stat(chemin+file).st_size:
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
            
            rch_mois = led.split("-")[1].replace("-", "")
            
            rch_jour = led.split("-")[2].replace("-", "")
            

            if str(annee) == rch_annee and str(jour) ==rch_jour and str(mois)==rch_mois:
                bon_date.append(file)
                
        
    if ext != "":
        for file in repertoire:
            if ext in file:
                bon_ext.append(file)
                
    #écriture du programme qui repère les similitudes dans les listes
    
    #on crée un tableau avec les listes pleines
    list_pas_vide = []
    if bon_nom != []:
        list_pas_vide.append(bon_nom)
    if bon_taille != []:
        list_pas_vide.append(bon_taille)
    if bon_date != []:
        list_pas_vide.append(bon_date)
    if bon_ext != []:
        list_pas_vide.append(bon_ext)
    
    resultat_inter = []
    #on recherchce chaque élément commun si les listes ne sont pas vides
    if len(list_pas_vide) > 1:
        for i in range(0, len(list_pas_vide)):
            for file in list_pas_vide[0]:
                if file in list_pas_vide[i]:
                    resultat_inter.append(file)
    else:
        resultat = list_pas_vide[0]
        
    #on cherche le nombre de fois où un élément apparait dans la liste interédiaire, 
    #s'il est égal à la longeur de la liste, c'est le fichier que l'on cherche
    n = 0
    for file in resultat_inter:
        for o_file in resultat_inter:
            if file == o_file:
                n += 1
        
        if n == len(list_pas_vide):
            resultat.append(file)
            
    #on afine avec une suppression des doublons car le fichiers se compte deux fois
    set(resultat)
    
    print(resultat)
    



elif reqst[0] == "copy":
    #source
    source = reqst[1]
    #destination
    destination = reqst[2]
            
            
    shutil.copyfile(source,destination)
