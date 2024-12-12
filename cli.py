import sys
from PIL import Image
from logger import log
from main import *

def print_help():
    print("Usage : cli.py <commande> <chemin_image> [options]")
    print("Commandes disponibles :")
    print("-grey                  : Convertit l'image en niveaux de gris")
    print("-blur <intensité>      : Applique un flou à l'image")
    print("-expand <intensité>    : Dilate les pixels de l'image")
    print("-rotate <angle>        : Fait pivoter l'image de l'angle spécifié")
    print("-resize <largeur> <hauteur> : Redimensionne l'image")
    print("-write <texte> <x> <y> : Ajoute du texte à l'image")
    print("-showlist              : Ajoute toute les modifications à une liste d'images")
    print("-help, -h              : Affiche l'aide")

def process_command(args):
    if len(args) < 3:
        print("Erreur : Nombre d'arguments insuffisant.")
        print_help()
        return

    command = args[1]
    image_path = args[2]

    try:

        if command not in ["-write", "-help", "-h"]:
            image = Image.open(image_path)

        if command == "-grey":
            convert_grey(image_path)
        elif command == "-watercolor":
            watercolor(image_path)
            
        elif command == "-showlist":
            image_paths = args[2:]
            allfilterslist(image_paths)
            
        elif command == "-watercolor":
            watercolor(image_path)

        elif command == "-blur":
            if len(args) < 4:
                raise ValueError("Spécifiez une intensité pour le flou.")
            intensity = int(args[3])
            blur(image, intensity)

        elif command == "-expand":
            if len(args) < 4:
                raise ValueError("Spécifiez une intensité pour la dilatation.")
            intensity = int(args[3])
            expand(image, intensity)
        

        elif command == "-rotate":
            if len(args) < 4:
                raise ValueError("Spécifiez un angle pour la rotation.")
            angle = int(args[3])
            rotate(image, angle)

        elif command == "-resize":
            if len(args) < 5:
                raise ValueError("Spécifiez la largeur et la hauteur pour le redimensionnement.")
            width = int(args[3])
            height = int(args[4])
            resize(image, width, height)

        elif command == "-write":
            if len(args) < 6:
                raise ValueError("Spécifiez le texte et ses coordonnées (x, y).")
            text = args[3]
            x = int(args[4])
            y = int(args[5])
            write(image_path, text, x, y)
            print("Texte ajouté à l'image avec succès.")

        elif command in ["-help", "-h"]:
            print_help()
#
        else:
            print(f"Commande inconnue : {command}")
            print_help()

    except FileNotFoundError:
        print(f"Erreur : L'image '{image_path}' est introuvable.")
    except ValueError as ve:
        print(f"Erreur : {ve}")
    except Exception as e:
        print(f"Erreur inattendue : {e}")

# Appel direct de la fonction
process_command(sys.argv)
