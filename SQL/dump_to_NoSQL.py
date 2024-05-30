import pandas as pd
from pymongo import MongoClient

# Étape 1: Lire le fichier CSV avec pandas
df = pd.read_csv('../Data/resultat_jointure.csv')

# Étape 2: Préparer la connexion MongoDB
client = MongoClient('mongodb://localhost:27017/')  # Changez l'URL si nécessaire
db = client['Prediction']  # Remplacez par le nom de votre base de données
collection = db['CollectionData']  # Remplacez par le nom de votre collection

# Étape 3: Convertir le DataFrame en une liste de dictionnaires
data = df.to_dict(orient='records')

# Étape 4: Insérer les données dans MongoDB
collection.insert_many(data)

print("Données insérées avec succès dans MongoDB!")
