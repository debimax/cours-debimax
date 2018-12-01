#!/usr/bin/python3
# -∗- coding: utf-8 -∗-

import http.server # importe un ensemble d'instructions pour servir les requêtes http.
import socketserver # importe un ensemble d'instructions pour connecter le programme.
# Serveur http de base delivrant le contenu du repertoire courant via le port indique.
PORT = 5432
Handler = http.server.SimpleHTTPRequestHandler
httpd = socketserver.TCPServer(("", PORT), Handler)
print("à l'écoute sur le port :", PORT)

httpd.serve_forever()
