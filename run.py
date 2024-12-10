import os

try:
    os.system("robot --outputdir results src/main.robot") 
except Exception as error:
    print(error)