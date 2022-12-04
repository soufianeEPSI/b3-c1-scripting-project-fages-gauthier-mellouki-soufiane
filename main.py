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

def suppr_col_IDlogement(tableau):
    for ligne in tableau:
        ligne.pop(1)
        print(ligne)

tableau=csv_to_array('conso-annuelles_v1.csv')
suppr_col_IDlogement(tableau)