from PIL import Image, ImageFilter
from logger import log

# Fonction pour convertir une image en niveaux de gris
def convert_grey(image):
    """
    convert an image with grey pigmentation

    arg:
    image, an image installed 

    return: converted image
    """
    image_nb = image.convert("L")  # Convertir en niveaux de gris
    image_nb.save("img/moto-noir-blanc.jpg")  # Sauvegarder l'image en noir et blanc
    image_nb.show()  # Afficher l'image
    log(f"Mise en noir et blanc de l'image : '{image}'.")
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
    image.save("img/imagemodified.jpg")  # Sauvegarder l'image modifiée
    image.show()  # Afficher l'image
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
        image = image.filter(filter=ImageFilter.BLUR)
        image = image.filter(ImageFilter.MinFilter(3))
    image.save("img/imagemodified.jpg")
    image.show()
    return image

def rotate(image, degree):
    """
    rotate an image

    arrgs:
    image, an image installed
    degree, int used to rotate

    return: rotated image
    """
    image = image.rotate(degree)
    image.save("img/imagemodified.jpg")
    image.show()
    return image

def resize(image, x, y):
    
    image = image.resize((x,y))
    image.save("img/imagemodified.jpg")
    image.show()
    return image

# Charger l'image
image = Image.open("img/moto.jpg")  # Remplacez par le chemin de votre image

# Étape 1 : Conversion en niveaux de gris
image_nb = convert_grey(image)

# Étape 2 : Appliquer un flou sur l'image originale
# blurred_image = blur(image, 40)  # Ajustez l'intensité selon vos besoins

# Étape 3 : dilate l'image
# image_dilate = expand(image,20)

# Étape 4 :
image_rotate = rotate(image, 20)

# Étape 5 :
image_resize = resize(image)

