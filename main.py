from PIL import Image

# Charger l'image
image = Image.open("img/moto.jpg")

# Convertir l'image en niveaux de gris (mode 'L')
image_nb = image.convert("L")

# Sauvegarder ou afficher l'image en noir et blanc
image_nb.save("img/moto-noir-blanc.jpg")
image_nb.show()