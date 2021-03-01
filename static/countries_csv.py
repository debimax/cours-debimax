#-------------------------------------------------------------------------------
# Nom: countries_csv
# Auteur:        J. Rivet
# maj:     30/12/2019
# Licence:     CC BY NC
#-------------------------------------------------------------------------------
# Dictreader est une classe qui mémorise une table csv
# la table a des noms pour chaque champ (clé)
# attribut fieldnames : renvoie la liste des noms de champ
# peut être lu comme une collection (ne supporte pas d'indice mais un parcours par item)
# chaque item est une orderedDict de tuples (fieldname, valeur)
# pour une exploitation aisée, on crée une liste où chaque item est un dictionnaire
# les clés sont fieldnames

# tri : sorted est une fonction qui renvoie une liste triée suivant une clé donnée
# comme une fonction
# liste = sorted(iterable, key=fonction, reverse=True|False)
#la fonction renvoie la ou les champs de tri

# exemple de table  :fichier countries.csv
# ------------------------------------------------------------------------------

import csv
import matplotlib.pyplot as plt

def cle_densite(dico_p):
    return dico_p['density']

def afficher_pays(pays):
    print("Il y a ", len(pays), "pays")
    for pa in pays:
        print(pa['countryName'], end='|**|')


def afficher_europe(pays):
    n = 0
    for pa in pays:
        if pa['continent'] == 'EU':
            n += 1
            print(pa['countryName'], end='|**|')

    print("Il y a ", n, "pays européens")

def afficher_europe_population(pays):
    n = 0
    for pa in pays:
        if pa['continent'] == 'EU':
            n += 1
            print(pa['countryName'],  ":", pa['population'])

    print("Il y a ", n, "pays européens")

def afficher_europe_population_trie(pays):
    # pays_tries = sorted(pays, key=cle_population, reverse=True)
    pays_tries = sorted(pays, key = lambda pays : pays['population'], reverse=True)
    n = 0
    for pa in pays_tries:
        if pa['continent'] == 'EU':
            n += 1
            print(pa['countryName'],  ":", end='')
            print( '{:,}'.format(pa['population']))

    print("Il y a ", n, "pays européens")

def afficher_sup10M(pays):
    pays_tries = sorted(pays, key = lambda pays : pays['population'], reverse=True)
    n = 0
    for pa in pays_tries:
        if pa['population'] > 50000000:
            n += 1
            print(pa['countryName'],  ":", end='')
            print( '{:,}'.format(pa['population']))

    print("Il y a ", n, "pays")

def afficher_top20_area(pays):
    pays_tries = sorted(pays, key = lambda pays : pays['area'], reverse=True)
    names = []
    areas = []
    for i in range(10):
        print(str(i+1), "-", pays_tries[i]['countryName'],  ":", '{:,}'.format(pays_tries[i]['area']))
        names.append(pays_tries[i]['countryName'])
        areas.append(pays_tries[i]['area'])

    plt.bar(names, areas)
    plt.xlabel('pays')
    plt.ylabel('superficie(km²)')
    plt.show()

def afficher_densite(pays):
    #création d'un champ density
    for pa in pays:
        pop = float(pa['population'])
        area = float(pa['area'])
        if area != 0:
            pa['density'] = int(pop / area)
        else:
            pa['density'] = 0

    pays_tries = sorted(pays, key=lambda  pays : pays['density'], reverse=True)

    names = []
    dens = []
    for p in pays_tries:
        if int(p['population']) > 50000000:
            names.append(p['countryName'][0:4])
            dens.append(p['density'])


    plt.barh(names, dens)
    plt.show()

# début -----------------------------------------------------
# création de pays
pays = []
with open('countries.csv', newline='') as csvfile:
    reader = csv.DictReader(csvfile, delimiter=";")

    for ligne in reader:
        pays.append(dict(ligne))

# conversion des champ numériques chaines en nombres
for p in pays:
    p['area'] = int(float(p['area']))
    p['population'] = int(p['population'])


# exercice sélectionner les pays de plus de 10 millions d'habitant qui ont la plus forte densité

# afficher_pays(pays)
# afficher_europe(pays)
# afficher_europe_population(pays)
# afficher_europe_population_trie(pays)
# afficher_sup10M(pays)
# afficher_top20_area(pays)
afficher_densite(pays)
