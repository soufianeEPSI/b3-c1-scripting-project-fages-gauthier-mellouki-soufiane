#!/usr/bin/python3
import csv

#Cette fonction va ouvrir le fichier CSV
def csv_to_array(fichier_csv):
    with open('conso-annuelles_v1.csv',newline='', encoding='latin-1') as f:
        tableau=[]
        lire=csv.reader(f, delimiter=";")
        for ligne in lire:
            tableau.append(ligne)
    return tableau

print(csv_to_array('conso-annuelles_v1.csv'))