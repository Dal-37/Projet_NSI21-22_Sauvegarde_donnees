import time
import shutil

#Outil de recherche

#commande de l'utilisateur
commande = input(">>>")

#on decoupe la requete de l'utilisateur et on cherche à quelle fonction
#elle correspond
reqst = commande.split(" ")

if reqst[0] == "plan":
    chemins = input("Rentrez le chemin vers le fichier à copier et celui vers le dossier de sauvegarde")
    saved_file = chemins.split(" ")[0]
    save_dos = chemins.split(" ")[1]
 
    
    frequence = input("""Choisissez la fréquence de sauvegarde:\n
                      10min: -dix; 30min: -trente; 1h: -une; 6h: -quart; 12h: -demi; 24h: -jour
                      """)
                      
    delay = 0.0
    if frequence == "-dix":
        delay = 10.0*60.0
    elif frequence == "-trente":
        delay = 30.0*60.0
    elif frequence == "-une":
        delay = 3600.0
    elif frequence == "-quart":
        delay = 6.0*3600.0
    elif frequence == "-demi":
        delay = 12.0*3600.0
    elif frequence == "-jour":
        delay = 24.0*3600.0
    
    #fonction à appeler par le module threading
    def copie_plan():
        global saved_file, save_dos
        shutil.copyfile(saved_file, save_dos)
        print("Copie effectuée")
        
        time.sleep(delay)
        copie_plan()
        
    copie_plan()

        delay = 24.0*3600.0
    
    #délai factice pour les tests
    delay = 10.0
    #fonction à appeler par le module threading
    def copie_plan():
        global saved_file, save_dos, n
        shutil.copyfile(saved_file, save_dos)
        print("Copie effectuée")
        
    timer = threading.Timer(interval=delay, function=copie_plan)
    timer.daemon = True
    timer.start()
