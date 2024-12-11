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
        print("-write <texte> <x> <y> : Ajoute du texte à l'image")
        return

    command = args[1]
    image_path = args[2]

    try:
        # Vérifier si l'image est accessible pour les commandes autres que -write
        if command != "-write":
            image = Image.open(image)

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

        elif command == "-write":
            if len(args) < 6:
                print("Erreur : spécifiez le texte et ses coordonnées (x, y).")
                return
            text = args[3]
            x = int(args[4])
            y = int(args[5])
            # Passez le chemin de l'image directement à la fonction write
            write(image_path, text, x, y)
            print("Texte ajouté à l'image avec succès.")
            return

        elif command == "-help" or command == "-h":
            print("Usage : cli.py <commande> <chemin_image> [options]")
            print("Commandes disponibles :")
            print("-grey                  : Convertit l'image en niveaux de gris")
            print("-blur <intensité>      : Applique un flou à l'image")
            print("-expand <intensité>    : Dilate les pixels de l'image")
            print("-rotate <angle>        : Fait pivoter l'image de l'angle spécifié")
            print("-resize <largeur> <hauteur> : Redimensionne l'image")
            print("-write <texte> <x> <y> : Ajoute du texte à l'image")
            return

        else:
            print(f"Commande inconnue : {command}")
            print("Utilisez -h pour voir les commandes disponibles.")

    except FileNotFoundError:
        print(f"Erreur : L'image '{image_path}' est introuvable.")
    except Exception as e:
        print(f"Erreur : {e}")


# Appeler la fonction principale directement
if __name__ == "__main__":
    process_command(sys.argv)
