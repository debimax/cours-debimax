#!/usr/bin/python3
# -*- coding: utf-8 -*-
from flask import Flask, render_template, url_for, request
app = Flask(__name__) # Initialise l'application Flask

@app.route('/', methods=['GET','POST'])  # On doit indiquer que l'on utilise les deux méthodes
def accueil():
        lignes=['ligne {}'.format(i) for i in range(1,10)]
        try:
                nom=request.form['nom']
        except:
                nom=''
        try:
                prenom=request.form['prenom']
        except:
                prenom=''
        try:
                texte=request.form['texte']
        except:
                texte=''
        titre="Méthode {}".format(request.method)
        return render_template("accueil.html", titre=titre,lignes=lignes,nom=nom,prenom=prenom,texte=texte)

if __name__ == '__main__':
    app.run(debug=True)
