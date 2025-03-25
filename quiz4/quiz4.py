import re
#--------------------------------------------------------
#                         Partie 1
#               Compter les occurences de XMAS
#--------------------------------------------------------
def compter_XMAS(grille, mot):
    rows = len(grille)
    cols = len(grille[0]) if rows > 0 else 0
    mot_len = len(mot)
    count = 0
    
    # Directions: (delta_row, delta_col)
    directions = [
        (0, 1),   # Horizontal droite
        (1, 0),    # Vertical bas
        (1, 1),    # Diagonal droite-bas
        (1, -1),   # Diagonal gauche-bas
        (0, -1),   # Horizontal gauche
        (-1, 0),   # Vertical haut
        (-1, -1),  # Diagonal gauche-haut
        (-1, 1)    # Diagonal droite-haut
    ]
    
    for i in range(rows):
        for j in range(cols):
            if grille[i][j] == mot[0]:  # Premier caractère trouvé
                for di, dj in directions:
                    match = True
                    for k in range(1, mot_len):
                        ni, nj = i + di*k, j + dj*k
                        if ni < 0 or ni >= rows or nj < 0 or nj >= cols:
                            match = False
                            break
                        if grille[ni][nj] != mot[k]:
                            match = False
                            break
                    if match:
                        count += 1
    return count

#--------------------------------------------------------
#                       Partie 2
# Compter les motifs en forme de X avec les lettres M, A, S
#--------------------------------------------------------
def count_xmas(i):
   # Recherche 'MAS' dans la chaîne normale OU dans la chaîne inversée
    if len(re.findall('MAS', i)) != 0 or len(re.findall('MAS', i[::-1])) != 0:
        return True
    
def compter_X_MAS(grille):
    somme = 0
# Parcours de chaque ligne de la grille avec son index
    for index, value in enumerate(grille):
        if index == 0: 
            continue  # On ignore la première ligne car on a besoin des lignes précédente et suivante
        
        # Trouver toutes les positions de 'A' dans la ligne courante
        all_occ = re.finditer('A', value)

        # Pour chaque occurrence de 'A' trouvée
        for match in all_occ:
            if match.start() == 0: 
                continue  # Ignorer si 'A' est en première position (pas de caractère à gauche)
            
            try:
                # Obtenir les lignes adjacentes (au-dessus et en-dessous)
                prev_row = grille[index - 1]  # Ligne précédente
                next_row = grille[index + 1]  # Ligne suivante
                
                # Construction des deux diagonales en forme de X:
                # 1. Diagonale gauche-haut -> droite-bas (\)
                string_leftup = (prev_row[match.start() - 1] +  # Caractère en haut à gauche
                                grille[index][match.start()] +   # 'A' au centre
                                next_row[match.start() + 1])     # Caractère en bas à droite
                
                # 2. Diagonale gauche-bas -> droite-haut (/)
                string_rightup = (next_row[match.start() - 1] +  # Caractère en bas à gauche
                                 grille[index][match.start()] +  # 'A' au centre
                                 prev_row[match.start() + 1])    # Caractère en haut à droite

                # Incrémenter le compteur si les deux diagonales contiennent 'MAS' (dans un sens ou l'autre)
                somme = somme + 1 if count_xmas(string_leftup) == True and count_xmas(string_rightup) == True else somme
            
            except:
                continue
    
    return somme
#--------------------------------------------------------
#                   Lire le fichier input
#--------------------------------------------------------
def lire_grille(nom_fichier):
    with open(nom_fichier, 'r') as f:
        return [line.strip() for line in f if line.strip()]

#--------------------------------------------------------
#                   Exemple pour "input_quiz4.txt"
#--------------------------------------------------------
fichier = "input_quiz4.txt"
mot = "XMAS"

try:
    grille = lire_grille(fichier)
    occurrences = compter_XMAS(grille, mot)
    print(f"Le mot '{mot}' apparaît {occurrences} fois dans la grille.")
    
    occurrences2 = compter_X_MAS(grille)
    print(f"Le mot X-MAS apparaît {occurrences2} fois dans la grille.")

except FileNotFoundError:
    print(f"Erreur: Fichier {fichier} non trouvé.")
except Exception as e:
    print(f"Erreur inattendue: {e}")