#!/usr/bin/python3
import csv

with open('conso-annuelles_v1.csv',newline='', encoding='latin1') as f:
    tableau=[]
    lire=csv.reader(f)
    print('',end='\n')
    print('Affichage des lignes du tableau',end='\n')
    for ligne in lire:
        print(ligne, end='\n')
        tableau.append(ligne)