from PIL import Image, ImageFilter

# Fonction pour convertir une image en niveaux de gris
def convert_grey(image):
    """
    convert an image with grey pigmentation

    arg:
    image, an image installed 

    return:converted image
    """
    image_nb = image.convert("L")  # Convertir en niveaux de gris
    image_nb.save("img/moto-noir-blanc.jpg")  # Sauvegarder l'image en noir et blanc
    image_nb.show()  # Afficher l'image
    return image_nb

# Fonction pour appliquer un flou intensifié à une image
def blur(image, intensity):
    """
    blur an image
    """
    for _ in range(intensity):  # Appliquer le flou plusieurs fois
        image = image.filter(ImageFilter.BLUR)
    image.save("img/imagemodified.jpg")  # Sauvegarder l'image modifiée
    image.show()  # Afficher l'image
    return image

def dilater(image, intensity):
    for _ in range(intensity):
        image = image.filter(filter=ImageFilter.BLUR)
        image = image.filter(ImageFilter.MinFilter(3))
    image.save("img/imagemodified.jpg")
    image.show()
    return image

# Charger l'image
image = Image.open("img/moto.jpg")  # Remplacez par le chemin de votre image

# Étape 1 : Conversion en niveaux de gris
# image_nb = convert_grey(image)

# Étape 2 : Appliquer un flou sur l'image originale
# blurred_image = blur(image, 40)  # Ajustez l'intensité selon vos besoins

# Étape 3 : dilate l'image
image_dilate = dilater(image,20)

