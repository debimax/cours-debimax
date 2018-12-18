#!python3
# -*- coding: utf-8 -*-

lienpy="C:\\ProgramData\\Miniconda3\\python.exe"
dirflask="test-flask\isnflask"
file_python_flask="isnflask.py"

#  on  importe
import subprocess
import os

user= os.environ["USERNAME"]
diruser=os.path.join('U:\\', user)
dirflask=os.path.join(diruser,dirflask)

# On  créer lme dossier  s'il n'existe pas
if not os.path.exists(dirflask):
    print("Attention il y a une erreur de nom de dossier")
    #os.makedirs(dirflask)

# Now change the directory
os.chdir(dirflask)

subprocess.run([lienpy, "isnflask.py"]) 

