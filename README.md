# API de Papillon

## Utilisation du Dockerfile
Si vous préférez exécuter l'API dans un conteneur Docker, suivez ces étapes :

Assurez-vous d'avoir Docker installé sur votre système.
Clonez ce référentiel et accédez au répertoire du projet.
Construisez l'image Docker en exécutant la commande suivante :
```bash
docker build -t papillon-api .
```
Lancez le conteneur Docker :
```bash
docker run -p 5000:5000 papillon-api
```
## Utilisation de Flask
Si vous préférez exécuter l'API directement sans Docker, suivez ces étapes :

Clonez ce référentiel et accédez au répertoire du projet.
Installez les dépendances avec la commande :
```bash
pip install -r requirements.txt
```
Lancez l'API en exécutant le fichier app.py :

```bash
python app.py
```


## Les différents endpoints
- GET /api : Version de l'api
- GET /staff : Liste des membres de l'équipe
- GET /warning : Message d'avertissement
- GET /disclaimerIE : Message d'avertissement concernant la non-affilitation à Index Éducation
- GET /latestVersion/plateforme : Dernière version de l'application pour la plateforme en question

