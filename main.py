#!/usr/bin/python3
import csv

#Cette fonction va ouvrir le fichier CSV et le stocker dans un tableau et le retourner en résultat
def csv_to_array(fichier_csv):
    with open('conso-annuelles_v1.csv',newline='', encoding='latin-1') as f:
        tableau=[]
        lire=csv.reader(f, delimiter=";") #On crée un tableau unidimensionnel avec chaque champ de la ligne du CSV délimitée par ";"
        for ligne in lire:
            tableau.append(ligne) #On ajoute chaque tableau unidimensionnel (donc chaque ligne du CSV) dans un tableau global avec tout le contenu du fichier CSV
    return tableau

#Cette fonction supprime le second élément de chaque ligne du tableau bidimensionnel global, donc la 2nde colone "ID Logement" du tableau (index 1 car on compte de 0)
def suppr_col_IDlogement(tableau):
    for ligne in tableau:
        ligne.pop(1)

#Cette fonction parcourt le tableau en partant de l'index le plus grand du tableau vers 0.
# car en faisant l'inverse, comme la taille du tableau est reduite de 1 à chaque suppression de ligne, la boucle finirait en dehors des limites du tableau.
def suppr_ligne_champvide(tableau):
    i=len(tableau)-1
    while i > 0:
        j=3
        while j > 0:
            if tableau[i][j] == '':
                tableau.pop(i)
                break
            j-=1
        i-=1

#Cette fonction additionne les consommations des deux années et ajoute le résultat dans une colonne supplémentaire
def add_conso(tableau):
    i=len(tableau)-1
    while i > 0:
        # J'utilise un bloc try except pour repérer les erreur et les traiter.
        # Dans les deux colonnes, les valeurs numériques sont écrites sous la forme européennes, avec une virgule, et pas un point.
        try:
            a = tableau[i][1].replace(',','.') # Je remplace dans la chaine de caractères la virgule par un point
            b = tableau[i][2].replace(',','.')
            total=float(a)+float(b) # Je convertis les chaines de caractères en nombres réels à virgule flottante et les additionne
            tableau[i].append(total) # J'ajoute une nouvelle colonne au tableau où je stocke la somme obtenue
        except:
            tableau.pop(i) # Le bloc except m´a indiqué la ligne non conforme: ['Piscines', '5033,1', '-', 'SPA'], je supprime la ligne du tableau
        i-=1

tableau=csv_to_array('conso-annuelles_v1.csv')
suppr_col_IDlogement(tableau)
suppr_ligne_champvide(tableau)
add_conso(tableau)
print(tableau)