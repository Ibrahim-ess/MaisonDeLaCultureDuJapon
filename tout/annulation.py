#!/usr/bin/python
#-*-coding:utf-8 -*-
import mod_python
import psycopg2

def index(req):
	conn=psycopg2.connect("""host=aquabdd dbname=etudiants user=11700970 password=0110030744K""")
	cur=conn.cursor()
	activite=req.form["act"]
	activite=activite.lower()
	cur.execute("SELECT email, activite from inscription2 where email=%s and activite=%s", (req.form["mail"],activite))
	enregistrement=cur.fetchone()
	if not enregistrement==None:
		cur.execute("DELETE FROM inscription2 WHERE inscription2.email=%s AND inscription2.activite=%s",(req.form["mail"],req.form["act"]))
        	conn.commit()
        	conn.close()
		req.content_type = "text/html"
		req.write("""<!DOCTYPE html>
				<html>
					<head>
						<meta charset="utf-8"/>
						<title> Annulation</title>
						<link rel="stylesheet" type="text/css" href="annulation.css"/>
					</head>
					<body>
						<p id="suppr"><strong> Votre participation a bien été supprimé</strong></p>
						<div>
						<p><a href="accueil.html"> Retour à l'accueil</a></p>
						<p><a href="Formulaire_Inscription.html"> Retour au formulaire d'inscription</a></p>
						<p><a href="form-annulation.html"> Retour au formulaire d'annulation</a></p>
						</div>
					</body>
					<footer>
						<p id="image"><img src="large2.jpg" alt="bye"/></p>
					</footer>
	
				</html>""")
	else:
		req.content_type = "text/html"
		req.write("""<!DOCTYPE html>
				<html>
					<head>
						<meta charset="utf-8"/>
						<title> Erreur</title>
						<link rel="stylesheet" type="text/css" href="annulation.css"/>
					</head>
					<body>
						<p id="suppr">Désole ! Aucun utilisateur n'a cette adresse ou ne participe à cet évènement</p>
						<div>
						<p><a href="accueil.html"> Retour à l'accueil</a></p>
						<p><a href="Formulaire_Inscription.html"> Retour au formulaire d'inscription</a></p>
						<p><a href="form-annulation.html"> Retour au formulaire d'annulation</a></p><br/>
						</div>
					</body>
					<footer>
						<p id="image"><img src="sorry.jpg" alt="sorry"/></p>
					</footer>
			</html>""")


	
	
	
 
