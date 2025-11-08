import os
import joblib
import numpy as np
import secrets

from fastapi import FastAPI, HTTPException, Depends
from fastapi.security import HTTPBasic, HTTPBasicCredentials
from pydantic import BaseModel

#MODEL_PATH = os.path.join(os.path.dirname(__file__), '../../model/model.joblib')
MODEL_PATH = "model/model.joblib"

# Chargement du modèle entraîné
try:
    model = joblib.load(MODEL_PATH)
except FileNotFoundError:
    raise RuntimeError(f"Model file not found at {MODEL_PATH}.")
except Exception as e:
    raise RuntimeError(f"Error loading model: {e}")

app = FastAPI(
    title="CoherentText? API",
    description="A simple API to predict if a text is coherent or just gibberish.",
    version="1.6.42",
)

# Authentification HTTP Basic
security = HTTPBasic()

def verify_credentials(credentials: HTTPBasicCredentials = Depends(security)):
    correct_username = secrets.compare_digest(credentials.username, "admin")
    correct_password = secrets.compare_digest(credentials.password, "admin")
    if not (correct_username and correct_password):
        raise HTTPException(status_code=401, detail="Unauthorized")
    return credentials

# modèle de données pour la requête d'entrée
class Sentence(BaseModel):
    sentence: str

    model_config = {
        "json_schema_extra": {
            "examples": [
                {
                    "sentence": "fshf kjsfhsjkd",
                }
            ]
        }
    }

# endpoint de prédiction
@app.post("/predict")
def predict(features: Sentence, credentials: HTTPBasicCredentials = Depends(verify_credentials)):
    try:
        prediction = model.predict([features.sentence])
        prediction_proba = model.predict_proba([features.sentence])
        classes = ['anger', 'boredom', 'empty', 'enthusiasm', 'fun', 'happiness', 'hate', 'love',
                   'neutral', 'relief', 'sadness', 'surprise', 'worry']

        return {
            "prediction value": prediction[0],
            "prediction_proba_dict": dict(zip(classes, prediction_proba.tolist()[0]))
        }

    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Prediction error: {e}")
