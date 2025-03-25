import re # Expression régulière
#--------------------------------------------------------
#                           Partie 1
#               Analyser et repérer les mul(.,.)
#--------------------------------------------------------
def analyser_memoire(memoire):
    # Expression régulière pour trouver les instructions mul valides
    pattern = r'mul\((\d{1,3}),(\d{1,3})\)'
    matches = re.findall(pattern, memoire) # Recherche de toutes les occurrences du motif dans la mémoire
    
    total = 0  # Initialisation du total des multiplications
    
    for x, y in matches:
        try:
            num1 = int(x)
            num2 = int(y)
            
            # Vérification que les nombres sont dans la plage valide (1-999)
            if 1 <= num1 <= 999 and 1 <= num2 <= 999:
                total += num1 * num2 # Calcul de la multiplication et ajout au total
                
        except ValueError:
           continue
    
    return total

#--------------------------------------------------------
#                       Partie 2
#     Analyser et repérer les mul(.,.) avec do/don't()
#--------------------------------------------------------

def analyser_memoire_do_dont(memoire):
    pattern = r'(mul\((\d{1,3}),(\d{1,3})\)|do\(\)|don\'t\(\))'
    matches = re.finditer(pattern, memoire)
    
    total = 0
    active = True  # Par défaut activé
    
    for match in matches:
        instruction = match.group()
        
        if instruction == "do()":
            active = True
        elif instruction == "don't()":
            active = False
        elif instruction.startswith("mul(") and active:
            x = int(match.group(2))
            y = int(match.group(3))
            if 1 <= x <= 999 and 1 <= y <= 999:
                total += x * y
    return total
#--------------------------------------------------------
#                   Lire le fichier input
#--------------------------------------------------------
def lire_fichier(nom_fichier):
    with open(nom_fichier, 'r') as f:
        return f.read()

#--------------------------------------------------------
#                   Exemple pour "input_quiz3.txt"
#--------------------------------------------------------
# Nom du fichier
nom_fichier = "input_quiz3.txt"

try:
    memoire = lire_fichier(nom_fichier)
    
    resultat1 = analyser_memoire(memoire)
    print(f"Somme totale des multiplications valides : {resultat1}")

    resultat2 = analyser_memoire_do_dont(memoire)
    print(f"Somme des multiplications (avec gestion do/don't): {resultat2}")

except FileNotFoundError:
    print("Erreur : Fichier non trouvé.")
except Exception as e:
    print(f"Erreur : {e}")