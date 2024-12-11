# Projet Python PG3

## Une application simple et puissante pour modifier des images à l'aide de commandes spécifiques.

Les fonctionnalités incluent la conversion en niveaux de gris, l'ajout de texte, le redimensionnement et bien plus.
Découvrez les détails ci-dessous !

Structure du projet
| Commande      | Description       |
|------------------|----------------|
| -grey	 | Convertit l'image en niveaux de gris |
| -blur <intensité> | Applique un flou à l'image |
| -expand <intensité> | Dilate les pixels de l'image |
| -rotate <angle> | Fait pivoter l'image de l'angle spécifié |
| -resize <largeur> <hauteur> | Redimensionne l'image |
| -write <texte> <x> <y>	 | Ajoute du texte à l'image à une position spécifique |


**Fichiers de log :** Tous les journaux d'exécution sont enregistrés dans image.log.
**Images modifiées :** Les images traitées sont enregistrées dans le dossier img.
**Images à modifier :** Placez vos images à traiter dans le dossier img.
**Dépendances :** Les packages nécessaires sont listés dans requirements.txt.
**Paramètres :** Modifiez les paramètres de l'application directement dans main.py.

## Commandes principales

### Utilisez la commande suivante pour exécuter l'application :

```bash
Usage: cli.py <commande> <chemin_image> [options]
Commandes disponibles
Commande	Description
-grey	Convertit l'image en niveaux de gris
-blur <intensité>	Applique un flou à l'image
-expand <intensité>	Dilate les pixels de l'image
-rotate <angle>	Fait pivoter l'image de l'angle spécifié
-resize <largeur> <hauteur>	Redimensionne l'image
-write <texte> <x> <y>	Ajoute du texte à l'image à une position spécifique
```

## Installation et utilisation


### Installer les dépendances :

```bash
pip install -r requirements.txt
```

Placer vos images : Déposez les images à traiter dans le dossier img.

### Lancer une commande : Exécutez une commande avec l'exemple ci-dessous :

```bash
python cli.py -grey img/mon_image.jpg
```

Vérifiez les résultats : Retrouvez les images modifiées dans le dossier img.

Exemples d'utilisation
### Convertir une image en niveaux de gris :

```bash
python cli.py -grey img/image.jpg
```

### Ajouter du texte à une image :

```bash
python cli.py -write "Bonjour" 50 100 img/image.jpg
```

### Redimensionner une image en 800x600 pixels :

```bash
python cli.py -resize 800 600 img/image.jpg
```

Faites-nous part de vos suggestions pour améliorer ce projet ! 😊
