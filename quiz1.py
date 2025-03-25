#--------------------------------------------------------
#                           Partie 1
#                   Calculer la distance totale
#--------------------------------------------------------
def calculer_distance_totale(liste_gauche, liste_droite):
    # Trier les deux listes
    liste_gauche_triee = sorted(liste_gauche)
    liste_droite_triee = sorted(liste_droite)
    
    # Vérifier que les listes ont la même longueur
    if len(liste_gauche_triee) != len(liste_droite_triee):
        raise ValueError("Les listes doivent avoir la même longueur")
    
    # Calculer la distance pour chaque paire et faire la somme
    distance_totale = 0
    for gauche, droite in zip(liste_gauche_triee, liste_droite_triee):
        distance_totale += abs(gauche - droite)
    
    return distance_totale

#--------------------------------------------------------
#                         Partie 2
#                   Calculer similarité
#--------------------------------------------------------
def calculer_score_similarite(liste_gauche, liste_droite):
    # Compter les occurrences de chaque nombre dans la liste de droite
    occurrences_droite = {}
    for nombre in liste_droite:
        occurrences_droite[nombre] = occurrences_droite.get(nombre, 0) + 1
    
    # Calculer le score de similarité
    score = 0
    for nombre in liste_gauche:
        score += nombre * occurrences_droite.get(nombre, 0)
    
    return score

#--------------------------------------------------------
#                   Lire le fichier input
#--------------------------------------------------------
def lire_fichier(nom_fichier):
    liste_gauche = []
    liste_droite = []
    
    with open(nom_fichier, 'r') as fichier:
        for ligne in fichier:
            # Supprimer les espaces/tabulations en trop et diviser la ligne
            valeurs = ligne.strip().split()
            if len(valeurs) == 2:  # S'assurer qu'il y a bien deux nombres
                gauche, droite = map(int, valeurs)
                liste_gauche.append(gauche)
                liste_droite.append(droite)
    
    return liste_gauche, liste_droite

#--------------------------------------------------------
#                   Exemple pour "input_quiz1.txt"
#--------------------------------------------------------
# Nom du fichier d'entrée
nom_fichier = "input_quiz1.txt"

# Calculer et afficher la distance totale
try:
    liste_gauche, liste_droite = lire_fichier(nom_fichier)
    distance_totale = calculer_distance_totale(liste_gauche, liste_droite)
    print(f"La distance totale entre les listes est : {distance_totale}")

    score = calculer_score_similarite(liste_gauche, liste_droite)
    print(f"Score de similarité total : {score}")
    
except FileNotFoundError:
    print(f"Erreur : Le fichier {nom_fichier} n'a pas été trouvé.")
except ValueError as e:
    print(f"Erreur : {e}")
except Exception as e:
    print(f"Une erreur inattendue s'est produite : {e}")