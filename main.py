from PIL import Image, ImageFilter, UnidentifiedImageError, ImageDraw
from logger import log
import cv2
import os
import numpy as np

# Charger l'image avec gestion des erreurs
currentmodifiedimg="img/currentmodifiedimg.jpg"

imagelist2=[]

# Fonction pour convertir une image en niveaux de gris
def convert_grey(image):
    image = Image.open(image)
    """
    convert an image with grey pigmentation

    arg:
    image, an image installed  

    return: converted image
    """
    try:
        if image is None:
            raise ValueError("Image non chargée. Conversion en niveaux de gris impossible.")
        image_nb = image.convert("L")
        savedfile = currentmodifiedimg
        
        image_nb.save(savedfile)
        #image = load_image(currentmodifiedimg)
        image_nb.show()
        log("L'image a été convertie en niveaux de gris et sauvegardée.")
        return image_nb
    except Exception as e:
        log(f"Erreur lors de la conversion en niveaux de gris : {e}")
        print(f"Erreur lors de la conversion en niveaux de gris : {e}")
        return None

# Fonction pour appliquer un flou à une image
def blur(image, intensity):
    """
    blur an image with an intensity

    args: 
    image, an image installed
    intensity, int used to intenfy blur
    
    return: blured image
    """
    try:
        if image is None:
            raise ValueError("Image non chargée. Application de flou impossible.")
        if not isinstance(intensity, int) or intensity < 1:
            raise ValueError("L'intensité doit être un entier positif.")
        for _ in range(intensity):
            image = image.filter(ImageFilter.BLUR)
        savedfile = currentmodifiedimg
        
        image.save(savedfile)
        #image = load_image(currentmodifiedimg)
        image.show()
        log("L'image a été floutée et sauvegardée.")
        return image
    except Exception as e:
        log(f"Erreur lors de l'application du flou : {e}")
        print(f"Erreur lors de l'application du flou : {e}")
        return None

# Fonction pour dilater une image
def expand(image, intensity):
    """
    expand colored pixel of an image with an intensity
    
    args:
    image, an image installed
    intensity, int used to intensify expand

    return: expanded image
    """
    try:
        if image is None:
            raise ValueError("Image non chargée. Dilatation impossible.")
        if not isinstance(intensity, int) or intensity < 1:
            raise ValueError("L'intensité doit être un entier positif.")
        for _ in range(intensity):
            image = image.filter(ImageFilter.MinFilter(3))
        #savedfile = "img/imagemodified_expand.jpg"
        
        savedfile = currentmodifiedimg
        image.save(savedfile)
        image.show()
        log("L'image a été dilatée et sauvegardée.")
        return image
    except Exception as e:
        log(f"Erreur lors de la dilatation de l'image : {e}")
        print(f"Erreur lors de la dilatation de l'image : {e}")
        return None

# Fonction pour faire pivoter une image
def rotate(image, degree):
    """
    rotate an image

    args:
    image, an image installed
    degree, int used to rotate

    return: rotated image
    """
    try:
        if image is None:
            raise ValueError("Image non chargée. Rotation impossible.")
        if not isinstance(degree, (int, float)):
            raise ValueError("Le degré de rotation doit être un entier ou un flottant.")
        image_rotated = image.rotate(degree)
        savedfile = currentmodifiedimg
        
        image_rotated.save(savedfile)
        image_rotated.show()
        log("L'image a été tournée et sauvegardée.")
        return image_rotated
    except Exception as e:
        log(f"Erreur lors de la rotation de l'image : {e}")
        print(f"Erreur lors de la rotation de l'image : {e}")
        return None
    
# Fonction pour redimensionner une image
def resize(image, x, y):
    """
    resize an image

    args:
    image, an image installed
    x, int wich is new width of the image.
    y, int wich is new height of the image.

    return:resized image
    """
    try:
        if image is None:
            raise ValueError("Image non chargée. Redimensionnement impossible.")
        if not isinstance(x, int) or not isinstance(y, int) or x <= 0 or y <= 0:
            raise ValueError("Les dimensions de redimensionnement doivent être des entiers positifs.")
        image_resized = image.resize((x, y))
        savedfile = currentmodifiedimg
        image_resized.save(savedfile)
        #image_resized.show()
        log("L'image a été redimensionnée et sauvegardée.")
        return image_resized
    except Exception as e:
        log(f"Erreur lors du redimensionnement de l'image : {e}")
        print(f"Erreur lors du redimensionnement de l'image : {e}")
        return None

# Fonction pour ajouter du texte à une image avec OpenCV
def write(image_path, text, x, y):
    """
    Add text to an image and save it.

    Args:
        image_path: The path to the image file.
        text: The text to add to the image.
        x: The x-coordinate for the text position.
        y: The y-coordinate for the text position.
    """
    try:
        if not os.path.exists(image_path):
            raise FileNotFoundError(f"L'image '{image_path}' est introuvable.")
        if not isinstance(text, str) or not text.strip():
            raise ValueError("Le texte à ajouter doit être une chaîne non vide.")
        if not isinstance(x, int) or not isinstance(y, int) or x < 0 or y < 0:
            raise ValueError("Les coordonnées x et y doivent être des entiers positifs.")
        
        image = cv2.imread(image_path)
        if image is None:
            raise ValueError(f"Impossible de lire l'image '{image_path}' avec OpenCV.")
        
        image = cv2.putText(
            img=image,
            text=text,
            org=(x, y),
            fontFace=cv2.FONT_HERSHEY_DUPLEX,
            fontScale=3.0,
            color=(0, 0, 0),
            thickness=3
        )
        savedfile = currentmodifiedimg
        cv2.imwrite(savedfile, image)
        log(f"L'image avec texte a été sauvegardée sous '{savedfile}'.")
        
        Image.open(savedfile).show()
    except Exception as e:
        log(f"Erreur lors de l'ajout de texte à l'image : {e}")
        print(f"Erreur lors de l'ajout de texte à l'image : {e}")

# def multiple_choises(image):
#     try:
#         image.save()
#         image.show()
#         return image
# # Exemple d'utilisation



# def gif(image_paths, output_gif_path, duration=500):
#     images = [Image.open(image_path) for image_path in image_paths]
#     # Save as GIF
#     images[0].save(output_gif_path, save_all=True, append_images=images[1:], duration=duration, loop=0 
#     )

#     if __name__ == "__main__":
#     # List of image file paths
#         image_paths = ["image1.jpg", "image2.jpg", "image3.jpg"] # Add your file paths
#     # Output GIF path
#         output_gif_path = "output.gif"
#     # Create GIF
#         #create_gif(image_paths, output_gif_path)

#         print(f"GIF created and saved at {output_gif_path}")
#     return


def detect_faces(image):

    face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml') # pour détecter l'image
    open_cv_image = cv2.cvtColor(np.array(image), cv2.COLOR_RGB2BGR) # Converti l'image pil en tableau NumPy pour OpenCV
    gray = cv2.cvtColor(open_cv_image, cv2.COLOR_BGR2GRAY) # converti l'image en niveaux de gris

    # Détecter les visages dans l'image
    face = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5) # détecte les visage

    # vérifier si des visages ont été détectés
    if len(face) == 0:
        print("Aucun visage détecté.")
    else:
        print(f"{len(face)} visage(s) détecté(s).")

    draw = ImageDraw.Draw(image) # permet de pouvoir dessiner sur l'image
    for (x, y, w, h) in face:
        draw.rectangle([x, y, x + w, y + h], outline="red", width=3) # dessine les carré sur les tetes détectées

    image.save(currentmodifiedimg)

    return


# Fonction pour ajouter du texte à une image avec OpenCV
def watercolor(image):
    """
    add watercolor filter to an image

    arg:
    image, an image installed
    """
    try:
        if not os.path.exists(image):
            raise FileNotFoundError(f"L'image '{image}' est introuvable.")
        
        image = cv2.imread(image)
        if image is None:
            raise ValueError(f"Impossible de lire l'image '{image}' avec OpenCV.")
        
        scale = float(3000)/(image.shape[0]+image.shape[1])
        image = cv2.resize(image,(int(image.shape[1]*scale),int(image.shape[0]*scale)))

        img_hsv=cv2.cvtColor(image,cv2.COLOR_BGR2HSV)
        adjust_v=(img_hsv[:,:,2].astype("uint")+5)*3
        adjust_v=((adjust_v>255)*255+(adjust_v<=255)*adjust_v).astype("uint8")

        img_hsv[:,:,2]=adjust_v
        img_soft=cv2.cvtColor(img_hsv,cv2.COLOR_BGR2HSV)
        img_soft=cv2.GaussianBlur(img_soft,(51,51),0)

        img_gray=cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
        img_gray=cv2.equalizeHist(img_gray)
        invert=cv2.bitwise_not(img_gray)
        blur=cv2.GaussianBlur(invert,(21,21),0)
        invertedblur = cv2.bitwise_not(blur)
        sketch = cv2.divide(img_gray,invertedblur,scale=265.0)
        sketch=cv2.merge([sketch,sketch,sketch])

        img_water=((sketch/255.0)*img_soft).astype("uint8")
        
        savedfile = currentmodifiedimg
        
        cv2.imwrite(savedfile, img_water)
        
        Image.open(savedfile).show()

        log(f"L'image avec texte a été sauvegardée sous '{savedfile}'.")
        #Image.open(savedfile).show()
    except Exception as e:
        log(f"Erreur lors de l'ajout de texte à l'image : {e}")
        print(f"Erreur lors de l'ajout de texte à l'image : {e}")

# # Exemple d'utilisation
path = "img/moto.jpg"

image = Image.open(path)

image=Image.open(path)

def allfilters(image99,i):
    image = Image.open(image99)

    savedfile = currentmodifiedimg
        
    image.save(savedfile)

    
    convert_grey(currentmodifiedimg)
    image = Image.open(currentmodifiedimg)
    blur(image,10)
    image = Image.open(currentmodifiedimg)
    expand(image, 5)
    image = Image.open(currentmodifiedimg)
    rotate(image, 45)
    image = Image.open(currentmodifiedimg)
    write(currentmodifiedimg, "Hello", 50, 50)
    image = Image.open(currentmodifiedimg)
    watercolor(currentmodifiedimg)
    image = Image.open(currentmodifiedimg)
    
    resize(image, 100, 100)
    imageaftertext=currentmodifiedimg
    #imageafter = Image.open(imageaftertext)
    
    image = Image.open(currentmodifiedimg)
    image.save(f"img/modified{i}.jpg")

#allfilters("villa.jpeg")


def allfilterslist(imagelist4):
    imagelist3=imagelist4
    for i in range(len(imagelist3)):
        print(imagelist3[i])
        allfilters(imagelist3[i],i)






def addfilterlist(currentimage):
    imagelist2.append(currentimage)
     
    #allfilters(currentimage,0)
    
    print(len(imagelist2))
     


#addfilterlist("img/meuf.jpg") img/meuf.jpg
#addfilterlist("img/moto.jpg") "img/moto.jpg" "img/meuf.jpg"
#allfilterslist()

#allfilters("img/moto.jpg")
    
# Exemple de conversion en niveaux de gris
#convert_grey("img/moto.jpg")
# Exemple d'application de flou
#blur(image, 10)

# Exemple de dilatation
#expand(image, 5)

# Exemple de rotation
#rotate(image, 45)

# Exemple de redimensionnement
#resize(image, 100, 100)

# Exemple d'ajout de texte
#write(path, "Hello", 50, 50)

# Exemple de mise en pastel de l'image.
# watercolor(path)

# gif(image)

image2 = Image.open("img/meuf.jpg")
#blur(image2,50)
#convert_grey("img/meuf.jpg")
#write("img/meuf.jpg", "Hello", 50, 50)

#rotate(image2,90)

detect_faces(image2)