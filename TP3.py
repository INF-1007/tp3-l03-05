
"""
TP3 : Système de gestion de livres pour une bibliothèque

IMPORTANT :
- Suivre attentivement les directives dans le fichier README.md.
- Chaque partie du TP doit être réalisée à l'intérieur d'une fonction que vous devez créer.
- Vous devez ensuite appeler chacune des fonctions dans la fonction principale "main()"

"""

import csv
from datetime import datetime


##########################################################################################################
# PARTIE 1 : Création du système de gestion et ajout de la collection actuelle
##########################################################################################################

"""
Créer une fonction `charger_collection` qui permet de : 
    - Lire le fichier collection_bibliotheque.csv
    - Créer un dictionnaire nommé 'bibliotheque'
        - La cote doit être la clé principale
        - Chaque clé principale doit contenir :
            - titre
            - auteur
            - date_publication

Cette partie doit être faite dans une fonction qui s'appelle "charger_collection". 
"""

# Écrire votre code ici

# Fonction 1
def charger_collection(fichier_csv):
    bibliotheque = {}
    with open(fichier_csv, 'r') as csv_file:
        csv_reader = csv.reader(csv_file)
        next(csv_reader) 
        for ligne in csv_reader:
            cote, titre, auteur, date = ligne[3], ligne[0], ligne[1], ligne[2]
            bibliotheque[cote] = {
                'titre': titre, 'auteur': auteur, 'date_publication': date,
                'emprunt': False, 'date_emprunt': None, 'frais_retard': 0, 'livre_perdu': False
            }
    return bibliotheque









##########################################################################################################
# PARTIE 2 : Ajout d'une nouvelle collection à la bibliothèque
##########################################################################################################

"""
Exigences :
- Lire nouvelle_collection.csv
- Ajouter seulement les livres dont la cote n'existe pas déjà
- Afficher les messages demandés dans l'énoncé
- Retourner ou mettre à jour la bibliothèque

Cette partie doit être faite dans une fonction qui s'appelle "ajouter_nouvelle_collection". 
"""

# Fonction 2
def ajouter_nouvelle_collection(bibliotheque, fichier_csv):
    with open (fichier_csv,'r') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter = ',')
        
        for ligne in csv_reader:
            cote = ligne[3]
            titre = ligne[0]
            auteur = ligne[1]
            date_publication = ligne[2]

            if cote in bibliotheque:
                print(f"Le livre '{titre}' existe déjà dans la bibliothèque. Cote : {cote}")
            else:
                bibliotheque[cote] = {
                    'titre': titre,
                    'auteur': auteur,
                    'date_publication': date_publication
                }
                print(f"Le livre '{titre}' a été ajouté à la bibliothèque. Cote : {cote}")
        
        return bibliotheque









##########################################################################################################
# PARTIE 3 : Modification de la cote de rangement d'une sélection de livres
##########################################################################################################

"""
Exigences :
- Modifier les cotes des livres de William Shakespeare
- Exemple : S028 → WS028
- Modifier correctement les clés du dictionnaire

Cette partie doit être faite dans une fonction qui s'appelle "modifier_cote_shakespeare". 
"""

# Écrire votre code ici
# Fonction 3
def modifier_cote_shakespeare(bibliotheque):
    for cote in list(bibliotheque.keys()):
        if bibliotheque[cote]['auteur'] == 'William Shakespeare':
            nouvelle_cote = 'WS' + cote[1:]
            bibliotheque[nouvelle_cote] = bibliotheque[cote]
            del bibliotheque[cote]
    return bibliotheque





##########################################################################################################
# PARTIE 4 : Emprunts et retours de livres
##########################################################################################################

"""
Exigences :
- Ajouter les clés :
    - emprunt
    - date_emprunt
- Lire emprunts.csv
- Mettre à jour l'état des livres

Cette partie doit être faite dans une fonction qui s'appelle "ajouter_emprunts". 
"""

# Écrire votre code ici
# Fonction 4
def ajouter_emprunts(bibliotheque, fichier_csv):
    with open (fichier_csv,'r') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter = ',')
        next(csv_reader)
        
        for ligne in csv_reader:
            cote = ligne[0]
            date_emprunt = ligne[1]
            if cote in bibliotheque:
                bibliotheque[cote]['emprunt'] = True
                bibliotheque[cote]['date_emprunt'] = date_emprunt

        













##########################################################################################################
# PARTIE 5 : Livres en retard
##########################################################################################################

"""
Exigences :
- Ajouter les clés :
    - frais_retard
    - livre_perdu
- 30 jours autorisés
- 2$ par jour de retard (max 100$)
- Livre perdu après 365 jours
- Utiliser datetime

Cette partie doit être faite dans une fonction qui s'appelle "ajouter_retards". 
"""

# Fonction 5
def calculer_retards(bibliotheque):
    maintenant = datetime.now()
    
    for cote in list(bibliotheque.keys()):
        if bibliotheque[cote].get('emprunt') == True and bibliotheque[cote].get('date_emprunt'):
           
            date_emprunt = datetime.strptime(bibliotheque[cote]['date_emprunt'], '%Y-%m-%d')
            
            jours_ecoules = (maintenant - date_emprunt).days
            
            if jours_ecoules <= 30:
                bibliotheque[cote]['frais_retard'] = 0
                bibliotheque[cote]['livre_perdu'] = False
            elif jours_ecoules <= 365:
                retard = (jours_ecoules - 30) * 2
                bibliotheque[cote]['frais_retard'] = min(retard, 100)
                bibliotheque[cote]['livre_perdu'] = False
            else:
                bibliotheque[cote]['frais_retard'] = 100
                bibliotheque[cote]['livre_perdu'] = True
    return bibliotheque









##########################################################################################################
# PARTIE 6 : Sauvegarde de la bibliothèque
##########################################################################################################

"""
Exigences :
- Créer le fichier bibliotheque_mise_a_jour.csv
- Colonnes obligatoires :
    cote, titre, auteur, date_publication,
    emprunt, date_emprunt, frais_retard, livre_perdu
- Utiliser le module csv pour écrire le fichier

Cette partie doit être faite dans une fonction qui s'appelle "sauvegarder_bibliotheque". 
"""

# Fonction 6
def sauvegarder_bibliotheque(bibliotheque, fichier_sortie):
    #creation du fichier de mise à jour
    with open(fichier_sortie, 'w', newline='') as csvfile:
        csv_writer = csv.writer(csvfile)
        # Écrire l'en-tête
        csv_writer.writerow(['cote', 'titre', 'auteur', 'date_publication', 'emprunt', 'date_emprunt', 'frais_retard', 'livre_perdu'])
        # Écrire les données
        for cote, livre in bibliotheque.items():
            csv_writer.writerow([
                cote, 
                livre['titre'],
                livre['auteur'],
                livre['date_publication'],
                livre.get('emprunt', False),
                livre.get('date_emprunt', ""),
                livre.get('frais_retard', 0),
                livre.get('livre_perdu', False)
            ])









##########################################################################################################
# PROGRAMME PRINCIPAL
##########################################################################################################

"""
Exigences :
- Appeler toutes vos fonctions dans le bon ordre
- Vérifier que le programme fonctionne sans erreur
- Afficher les résultats demandés
"""

def main():

    ############################################################
    # Partie 1 : Appel de la fonction charger_collection 
    ############################################################
    
    # Écrire votre code ici 
    ma_bibli = charger_collection('collection_bibliotheque.csv')
    print(f"Collection chargée : {len(ma_bibli)} livres.")




    ############################################################
    # Partie 2 : Appel de la fonction ajouter_nouvelle_collection
    ############################################################
    
    ma_bibli = ajouter_nouvelle_collection(ma_bibli, 'nouvelle_collection.csv')
    print(f"Collection mise à jour : {len(ma_bibli)} livres.")

    ############################################################
    # Partie 3 : Appel de la fonction modifier_cote_shakespeare
    ############################################################

    ma_bibli = modifier_cote_shakespeare(ma_bibli)
    print("Cotes de Shakespeare mises à jour.")


    ############################################################
    # Partie 4 : Appel de la fonction ajouter_emprunts
    ############################################################

    ajouter_emprunts(ma_bibli, 'emprunts.csv')
    


    ############################################################
    # Partie 5 : Appel de la fonction calculer_retards
    ############################################################

    ma_bibli = calculer_retards(ma_bibli)
    print("Retards calculés.")

    ############################################################
    # Partie 6 : Appel de la fonction sauvegarder_bibliotheque
    ############################################################
    
    sauvegarder_bibliotheque(ma_bibli, 'bibliotheque_mise_a_jour.csv')
    print("Fichier de sauvegarde généré avec succès.")
    

if __name__ == "__main__":
    main()