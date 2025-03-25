#--------------------------------------------------------
#                           Partie 1
#               Determiner si le rapport est sûr
#--------------------------------------------------------
def rapport_sur(sequence):
    differences = [sequence[i+1] - sequence[i] for i in range(len(sequence)-1)]
    
    # Vérifie si tous les pas sont entre 1 et 3 (en valeur absolue)
    if not all(1 <= abs(d) <= 3 for d in differences):
        return False
    
    # Vérifie si la séquence est strictement croissante ou décroissante
    if all(d > 0 for d in differences):  # Strictement croissante
        return True
    elif all(d < 0 for d in differences):  # Strictement décroissante
        return True
    else:
        return False

#--------------------------------------------------------
#                       Partie 2
#    Determiner si le rapport est sûr avec amortisseur
#--------------------------------------------------------
def rapport_sur_avec_amortisseur(sequence):
    # Si la séquence est déjà safe sans modification
    if rapport_sur(sequence):
        return True
    
    # Teste la suppression de chaque élément un par un
    for i in range(len(sequence)):
        nouvelle_sequence = sequence[:i] + sequence[i+1:]
        if rapport_sur(nouvelle_sequence):
            return True
    
    return False


def analyser_fichier(nom_fichier):
    nombre_sur = 0
    nombre_sur_amortisseur = 0
    nombre_total = 0  # Ajout d'un compteur pour le nombre total de lignes
    with open(nom_fichier, 'r') as f:
        for ligne in f:
            if ligne.strip():  # Ignore les lignes vides
                nombre_total += 1  # Incrémente pour chaque ligne non vide
                sequence = list(map(int, ligne.strip().split()))
                if rapport_sur(sequence):
                    nombre_sur += 1
                if rapport_sur_avec_amortisseur(sequence):
                    nombre_sur_amortisseur += 1
    return nombre_sur, nombre_sur_amortisseur, nombre_total

#--------------------------------------------------------
#                   Exemple pour "input_quiz2.txt"
#--------------------------------------------------------
# Nom du fichier
nom_fichier = "input_quiz2.txt"

# Analyse et résultat
try:
    nombre_sur, nombre_sur_amortisseur, nombre_total = analyser_fichier(nom_fichier)
    print(f"Nombre de rapports sûrs : {nombre_sur} / {nombre_total}")
    print(f"Nombre de rapports sûrs avec amortisseur : {nombre_sur_amortisseur} / {nombre_total}")

except FileNotFoundError:
    print("Erreur : Fichier non trouvé.")
except Exception as e:
    print(f"Erreur : {e}")