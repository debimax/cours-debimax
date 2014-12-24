#!/usr/bin/python3.4
# -*- coding: utf-8 -*-
from flask import Flask, render_template, url_for
app = Flask(__name__) # Initialise l'application Flask

@app.route('/')
def accueil():
	lignes=['ligne {}'.format(i) for i in range(1,10)]
	return render_template("accueil.html", titre="Bienvenue !",lignes=lignes)

if __name__ == '__main__':
	app.run(debug=True)
