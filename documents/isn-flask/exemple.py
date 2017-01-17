#!/usr/bin/python3
# -*- coding: utf-8 -*-
from flask import Flask, render_template, url_for
app = Flask(__name__) # Initialise l'application Flask

@app.route('/')   # C'est un décorateur, on donne la route ici "/"  l'adresse sera donc localhost:5000/
def accueil():
        Lignes=['ligne {}'.format(i) for i in range(1,10)] # Que fait cette ligne?
        return render_template("accueil.html", titre="Bienvenue !",lignes=Lignes) # On utilise le template accueil.html, avec les variables titre et lignes

if __name__ == '__main__':
        app.run(debug=True)
