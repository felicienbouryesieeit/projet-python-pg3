from PIL import Image, ImageFilter, UnidentifiedImageError
from logger import log
import cv2
import os

# Charger l'image avec gestion des erreurs
list_img = []

def load_image(path):
    try:
        image = Image.open(path)
        log(f"L'image '{path}' a été chargée avec succès.")
        print(f"L'image '{path}' a été chargée avec succès.")
        return image
    except FileNotFoundError:
        log(f"Erreur : L'image '{path}' est introuvable.")
        print(f"Erreur : L'image '{path}' est introuvable.")
    except UnidentifiedImageError:
        log(f"Erreur : Le fichier '{path}' n'est pas une image valide.")
        print(f"Erreur : Le fichier '{path}' n'est pas une image valide.")
    except Exception as e:
        log(f"Erreur inattendue lors du chargement de l'image : {e}")
        print(f"Erreur inattendue lors du chargement de l'image : {e}")
    return None

# Fonction pour convertir une image en niveaux de gris
def convert_grey(image):
    try:
        if image is None:
            raise ValueError("Image non chargée. Conversion en niveaux de gris impossible.")
        image_nb = image.convert("L")
        savedfile = "img/imagemodified_grey.jpg"
        image_nb.save(savedfile)
        image_nb.show()
        log("L'image a été convertie en niveaux de gris et sauvegardée.")
        return image_nb
    except Exception as e:
        log(f"Erreur lors de la conversion en niveaux de gris : {e}")
        print(f"Erreur lors de la conversion en niveaux de gris : {e}")
        return None

# Fonction pour appliquer un flou à une image
def blur(image, intensity):
    try:
        if image is None:
            raise ValueError("Image non chargée. Application de flou impossible.")
        if not isinstance(intensity, int) or intensity < 1:
            raise ValueError("L'intensité doit être un entier positif.")
        for _ in range(intensity):
            image = image.filter(ImageFilter.BLUR)
        savedfile = "img/imagemodified_blur.jpg"
        image.save(savedfile)
        image.show()
        log("L'image a été floutée et sauvegardée.")
        return image
    except Exception as e:
        log(f"Erreur lors de l'application du flou : {e}")
        print(f"Erreur lors de l'application du flou : {e}")
        return None

# Fonction pour dilater une image
def expand(image, intensity):
    try:
        if image is None:
            raise ValueError("Image non chargée. Dilatation impossible.")
        if not isinstance(intensity, int) or intensity < 1:
            raise ValueError("L'intensité doit être un entier positif.")
        for _ in range(intensity):
            image = image.filter(ImageFilter.MinFilter(3))
        savedfile = "img/imagemodified_expand.jpg"
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
    try:
        if image is None:
            raise ValueError("Image non chargée. Rotation impossible.")
        if not isinstance(degree, (int, float)):
            raise ValueError("Le degré de rotation doit être un entier ou un flottant.")
        image_rotated = image.rotate(degree)
        savedfile = "img/imagemodified_rotate.jpg"
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
    try:
        if image is None:
            raise ValueError("Image non chargée. Redimensionnement impossible.")
        if not isinstance(x, int) or not isinstance(y, int) or x <= 0 or y <= 0:
            raise ValueError("Les dimensions de redimensionnement doivent être des entiers positifs.")
        image_resized = image.resize((x, y))
        savedfile = "img/imagemodified_resize.jpg"
        image_resized.save(savedfile)
        image_resized.show()
        log("L'image a été redimensionnée et sauvegardée.")
        return image_resized
    except Exception as e:
        log(f"Erreur lors du redimensionnement de l'image : {e}")
        print(f"Erreur lors du redimensionnement de l'image : {e}")
        return None

# Fonction pour ajouter du texte à une image avec OpenCV
def write(image_path, text, x, y):
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
        savedfile = "img/image_with_text.jpg"
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

def gif(image):
    image_paths = ['image1.png', 'image2.png', 'image3.png']
    image = [Image.open(image) for image in image_paths]
    gif = image('animation.gif', save_all=True, append_images=image, duration=500, loop=0)
    gif.save()
    gif.show()
    return
    
# Fonction pour ajouter du texte à une image avec OpenCV
def watercolor(image):
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
        
        savedfile = "img/image_watercolor.jpg"
        cv2.imwrite(savedfile, img_water)
        log(f"L'image avec texte a été sauvegardée sous '{savedfile}'.")
        Image.open(savedfile).show()
    except Exception as e:
        log(f"Erreur lors de l'ajout de texte à l'image : {e}")
        print(f"Erreur lors de l'ajout de texte à l'image : {e}")

def tab_add(img): 
    img2 =  "img/"+img#+".jpg"
    list_img.append(img2)


def multifilter(tab):
    intensity_blur = int(input("intensité du floutage"))
    intensity_expand = int(input("intensité de la dilatation"))
    degree_rotate = int(input("degré d'inclinaison"))
    resize_x = int(input("taille x"))
    resize_y = int(input("taille y"))
    write_text = str(input("texte à intégrer dans l'image"))
    write_x = int(input("allignement x du texte"))
    write_y = int(input("allignement y du texte"))
    for _ in tab:
        convert_grey(tab[_])
        blur(tab[_], intensity_blur)
        expand(tab[_], intensity_expand)
        rotate(tab[_], degree_rotate)
        resize(tab[_], resize_x, resize_y)
        write(tab[_], write_text, write_x, write_y)
    return None

# # Exemple d'utilisation
path = "img/moto.jpg"

image = load_image(path)

tab_add()
# Exemple de conversion en niveaux de gris
#convert_grey(image)

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