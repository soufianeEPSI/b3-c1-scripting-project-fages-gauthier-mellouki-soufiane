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

tableau=csv_to_array('conso-annuelles_v1.csv')
suppr_col_IDlogement(tableau)
suppr_ligne_champvide(tableau)
print(tableau)