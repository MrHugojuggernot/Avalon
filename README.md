# Avalon

Un bot Discord privé en Python pour gérer (trouver et envoyer) les images de fond d'écran. Les fond d'écrans sont matérialisés par des fichiers .png dans un dossier précis et dans une base de donnée en tableau numpy à 2 dimensions. Les commandes de gestion de la base de donnée se trouve dans manager.py

## Commandes Disponibles
```bash
?search(arg) --> Recherche dans la base de donnée si le terme arg existe dans celle-ci, si c'est vrai, renvoie le/les titre(s) complet(s) ainsi que le/les identifiant(s)
```
```bash
?get(ID) --> Recherche dans la base de donnée si l'identifiant existe, si c'est le cas, renvoie l'image correspondante avec son titre complet
```
```bash
?add (nom,attachement) --> Ajoute une nouvelle ligne dans la base de donnée et télécharge l'image attachée au message dans le dossier pour
```


Par Hugojuggernot, Bot Privée
