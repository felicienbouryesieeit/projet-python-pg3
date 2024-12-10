import sys
from PIL import Image
from logger import log
from main import *  # Importez vos fonctions existantes

def process_command(args):
    # Vérifiez que suffisamment d'arguments sont fournis
    if len(args) < 3:
        print("Usage : cli.py <commande> <chemin_image> [options]")
        print("Commandes disponibles :")
        print("-grey                  : Convertit l'image en niveaux de gris")
        print("-blur <intensité>      : Applique un flou à l'image")
        print("-expand <intensité>    : Dilate les pixels de l'image")
        print("-rotate <angle>        : Fait pivoter l'image de l'angle spécifié")
        print("-resize <largeur> <hauteur> : Redimensionne l'image")
        return

    command = args[1]
    image_path = args[2]

    try:
        image = Image.open(image_path)
    except FileNotFoundError:
        print(f"Erreur : l'image '{image_path}' est introuvable.")
        return

    if command == "-grey":
        convert_grey(image)

    elif command == "-blur":
        if len(args) < 4:
            print("Erreur : spécifiez une intensité pour le flou.")
            return
        intensity = int(args[3])
        blur(image, intensity)

    elif command == "-expand":
        if len(args) < 4:
            print("Erreur : spécifiez une intensité pour la dilatation.")
            return
        intensity = int(args[3])
        expand(image, intensity)

    elif command == "-rotate":
        if len(args) < 4:
            print("Erreur : spécifiez un angle pour la rotation.")
            return
        angle = int(args[3])
        rotate(image, angle)

    elif command == "-resize":
        if len(args) < 5:
            print("Erreur : spécifiez la largeur et la hauteur pour le redimensionnement.")
            return
        width = int(args[3])
        height = int(args[4])
        resize(image, width, height)

    else:
        print(f"Commande inconnue : {command}")
        print("Utilisez -h pour voir les commandes disponibles.")

# Appeler la fonction principale directement
process_command(sys.argv)
