from PIL import Image, ImageFilter
from logger import log
import cv2

# Charger l'image
path = "img/moto.jpg"
image = Image.open("img/moto.jpg")  # Remplacez par le chemin de votre image

# Fonction pour convertir une image en niveaux de gris
def convert_grey(image):
    """
    convert an image with grey pigmentation

    arg:
    image, an image installed 

    return: converted image
    """
    image_nb = image.convert("L")  # Convertir en niveaux de gris
    savedfile="imagemodified.jpg"
    image.save(f"img/{savedfile}")
    image_nb.show()  # Afficher l'image
    log(f"L'image a été mis en noir et blanc. ")
    return image_nb


# Fonction pour appliquer un flou intensifié à une image
def blur(image, intensity):
    """
    blur an image with an intensity

    args: 
    image, an image installed
    intensity, int used to intenfy blur
    
    return: blured image
    """
    for _ in range(intensity):  # Appliquer le flou plusieurs fois
        image = image.filter(ImageFilter.BLUR)
    savedfile="imagemodified.jpg"
    image.save(f"img/{savedfile}")
    image.show()  # Afficher l'image
    log(f"L'image a été floutée")
    return image

def expand(image, intensity):
    """
    expand colored pixel of an image with an intensity
    
    args:
    image, an image installed
    intensity, int used to intensify expand

    return: expanded image
    """
    for _ in range(intensity):
        image = image.filter(ImageFilter.MinFilter(3))
    savedfile="imagemodified.jpg"
    image.save(f"img/{savedfile}")
    image.show()
    log(f"L'image a été dilatée")
    return image

def rotate(image, degree):
    """
    rotate an image

    args:
    image, an image installed
    degree, int used to rotate

    return: rotated image
    """
    image = image.rotate(degree)
    savedfile="imagemodified.jpg"
    image.save(f"img/{savedfile}")
    image.show()
    log(f"L'image a été tournée")
    return image

def resize(image, x, y):
    """
    resize an image

    args:
    image, an image installed
    x, int wich is new width of the image.
    y, int wich is new height of the image.

    return:resized image
    """
    image = image.resize((x,y))
    savedfile="imagemodified.jpg"
    image.save(f"img/{savedfile}")
    image.show()
    log(f"L'image a été redimensionnée")
    return image


def write(image, text, x, y):
    """
    Add text to an image and save it.

    Args:
        image_path: The path to the image file.
        text: The text to add to the image.
        x: The x-coordinate for the text position.
        y: The y-coordinate for the text position.
    """
    # Charger l'image
    image = cv2.imread(image)
    if image is None:
        log(f"Erreur : L'image '{image}' est introuvable.")
        return

    # Ajouter le texte sur l'image
    image = cv2.putText(
        img=image,
        text=text,
        org=(x, y),
        fontFace=cv2.FONT_HERSHEY_DUPLEX,
        fontScale=3.0,
        color=(0, 0, 0),  # Couleur noire pour le texte
        thickness=3
    )

    # Enregistrer l'image avec le texte
    savedfile = "img/image_with_text.jpg"
    cv2.imwrite(savedfile, image)
    log(f"L'image avec texte a été sauvegardée sous '{savedfile}'.")

    # Afficher l'image jusqu'à ce qu'une touche soit pressée
    cv2.imshow("Image avec texte", image)
    print("Appuyez sur une touche pour fermer l'image.")
    cv2.waitKey(0)  # Attend une touche pour fermer la fenêtre
    cv2.destroyAllWindows()



# Étape 1 : Conversion en niveaux de gris
# image_nb = convert_grey(image)

# Étape 2 : Appliquer un flou sur l'image originale
# blurred_image = blur(image, 40)  # Ajustez l'intensité selon vos besoins

# Étape 3 : Dilate l'image
#image_dilate = expand(image,20)

# Étape 4 : Rotation de l'image de 20°
# image_rotate = rotate(image, 20)

# Étape 5 : Redimentionnement de l'image de 60x60
# image_resize = resize(image, 60, 60)

