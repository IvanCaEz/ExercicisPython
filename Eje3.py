# 3- Renaming files

import os
import glob
import re

def canviar_nom_fitxer(path: str):
    try:
        directori_carpeta = os.listdir(f"ExercicisUF1Basics\{path}")
        trobat = False
        for file in directori_carpeta:
            print(file)
        while trobat == False:
            seleccio = str(input("Selecciona el fitxer que vols editar\n"))
            if seleccio in directori_carpeta:
                extensio = seleccio.split(".")[1]
                nou_nom = str(input("Entra el nou nom sense la extensió: "))
                os.rename(f"ExercicisUF1Basics\{path}/{seleccio}", f"ExercicisUF1Basics\{path}/{nou_nom}.{extensio}")
                print(f"Has canviat el nom del fitxer {seleccio} a {nou_nom}.{extensio}")
                trobat = True
            else:
                print("No s'ha trobat cap fitxer amb aquest nom")
    except FileNotFoundError:
        print("El sistema no pot trobar la ruta")

def canviar_noms_fitxers(directory: str):
    if(os.path.exists(directory) & os.path.isdir(directory)):
        print("Directory exists")
        os.chdir(directory)
        pattern = input("Write your search string pattern: ")
        rename = input("Write your rename string: ")
        for file in glob.glob("*" + pattern + "*"):
            if(file):
                renamedFile = file.replace(pattern, rename)
                os.rename(file,renamedFile)
                print(f"{file} -> {renamedFile}")

path = str(input("Entra el nom del directori: "))
canviar_noms_fitxers(path)