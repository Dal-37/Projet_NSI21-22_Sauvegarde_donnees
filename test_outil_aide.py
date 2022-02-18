commande = input(">>>")

#on decoupe la requete de l'utilisateur et on cherche à quelle fonction
#elle correspond
reqst = commande.split(" ")

if reqst[0] == "help":
    print("Bienvenue dans le système de sauvegarde de fichier\n")
    print("-"*60)
    print("""\n\nOutil de recherche:\n
          Commande: find
              Premier argument: chemin du dossier où la recherche doit être effectué\n
              Paramètres de recherches: -name pour le nom du fichier\n
                                        -size pour la taille du fichier\n
                                        -led pour la date de modification du fichier\
                                        -ext pour l'extension du fichier\n
              
          """)
    print("-"*60)
    print("""\n\nOutil de copie:\n
         Commande: copy
         Donnez le chemin du fichier d'origine puis celui du chemin destination\n
              """)
    print("-"*60)
    print("""\n\nOutil de planification:\n
          Commande: plan
          Suivez les instructions données par la commannde.""")
          
          
