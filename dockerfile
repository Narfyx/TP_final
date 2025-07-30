# Étape 1: Utiliser une image Python officielle comme base
FROM python:3.9-slim

# Définir le répertoire de travail dans le conteneur
WORKDIR /app

# Copier les dépendances et les installer
# Copier requirements.txt d'abord pour profiter du cache de Docker
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copier le reste du code de l'application
COPY . .

# Exposer le port sur lequel l'application va tourner
EXPOSE 5000

# Commande pour lancer l'application avec Gunicorn
# Gunicorn est un serveur WSGI de production
# --bind 0.0.0.0:5000 : écoute sur toutes les interfaces sur le port 5000
# --workers 3 : nombre de processus pour gérer les requêtes
# app:app : fait référence à l'objet 'app' dans le fichier 'app.py'
CMD ["gunicorn", "--bind", "0.0.0.0:5000", "--workers", "3", "app:app"]
