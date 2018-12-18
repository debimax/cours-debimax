#! python3
# -*- coding: utf-8 -*-

lienpy="C:\\ProgramData\\Miniconda3\\python.exe"

import subprocess
import os
user= os.environ["USERNAME"]
diruser=os.path.join('U:\\', user)
# Now change the directory
os.chdir(diruser)

subprocess.run([lienpy, "-m",  "http.server","8080"]) 

