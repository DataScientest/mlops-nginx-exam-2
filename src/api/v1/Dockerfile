# Utilise l'image officielle Python
FROM python:3.11-slim

# Définir le répertoire de travail
WORKDIR /app

# Copier les fichiers requirements.txt et installer les dépendances
COPY ../requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt uvicorn fastapi joblib

# Copier le code de l'API
COPY . .

# Exposer le port FastAPI
EXPOSE 8000

# Commande pour lancer l'API
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
