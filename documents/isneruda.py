#!/usr/bin/python3.4
# -*- coding: utf-8 -*-
from flask import Flask, render_template, url_for, jsonify, request
from flask.ext import menu
#from flask.ext.moment import Moment
#from datetime import datetime
import os
import re

app = Flask(__name__) # Initialise l'application Flask
#moment = Moment(app)
menu.Menu(app=app)

@app.route('/')
@menu.register_menu(app, '.home', 'Home', order=0)
def accueil():
	return render_template("accueil.html", titre="Bienvenue !" )

@app.route('/gallerie')
@menu.register_menu(app, '.gallerie', 'Gallerie', order=1)
def gallerie():
	listeim=[i  for i in  os.listdir(url_for('static', filename = '/gallery')[1:])    if os.path.isfile( os.path.join('static/gallery',i)) and i.rsplit('.',1)[-1] in ['png','jpg']]
	return render_template("gallerie.html", titre="Gallerie", listeim=listeim)

@app.route('/localisation')
@menu.register_menu(app, '.localisation', 'Localisation', order=2)
def localisation():
	return render_template("localisation.html", titre="Localisation")


@app.route('/reservation')
@menu.register_menu(app, '.reservation', 'Reservation', order=3)
def reservation():
	return render_template("reservation.html", titre="Réservation")

@app.route('/conversion',methods=['GET','POST'])
@menu.register_menu(app, '.conversion', 'Conversion', order=4)
def conversion():
	if request.method == 'POST':
		AdresseDMS=request.form['AdresseDMS']
		Adresse2=convers(AdresseDMS)
		Adresse1=Adresse2[0]
		Adresse2=Adresse2[1]
		Zoom=request.form['Zoom']
	else:
		Adresse1=""
		Adresse2=""
		AdresseDMS=""
		Zoom=16
	return render_template("conversion.html", titre="Conversion",AdresseDMS=AdresseDMS, Adresse1=Adresse1, Adresse2=Adresse2,Zoom=Zoom)

def convers(adrDMS):
	#adrDMS=re.findall(r"[\w\.]+", adrDMS)
	adrDMS=re.findall(r"^\s*(.*)$", adrDMS)[0] # On enlève les espaces blanc en début
	adrDMS=re.findall(r"[A-Z]*[^A-Z]+", adrDMS)  # on coupe dans une liste 
	adrDD=[]  
	if adrDMS[0][0:3]=='GPS':  # s'il y a au debut GPS ou GPS: 
		adrDMS.pop(0)          # On enlève
	if len(adrDMS)==2 or 1:    # S'il y a bien une ou deux (latitude longitude)
		for i in adrDMS:
			if i[0] in ['N','E','n','e']:
				temp=1
			elif i[0] in ['S','W','s','w']:
				temp=-1
			else :
				return "adresse non conforme"
			i=re.findall(r"[\w\.]+", i)       # On enlève ° ' et "
			i.pop(0)                          # on enlève S N W ou E
			temp*=(float(i[0])+ float(i[1])/60+  float(i[2])/3600)
			adrDD.append(temp)
		return adrDD
	else:
		return "adresse non conforme"

if __name__ == '__main__':
	app.run(debug=True)

#def DecimaltoDMS(Decimal):
#d = int(Decimal)
#m = int((Decimal - d) * 60)
#s = (Decimal - d - m/60) * 3600.00
#z= round(s, 2)
#if d >= 0:
#    print ("N ", abs(d), "º ", abs(m), "' ", abs(z), '" ')
#else:
#    print ("S ", abs(d), "º ", abs(m), "' ", abs(z), '" ')
