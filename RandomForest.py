import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier

# 1. Charger le DataFrame depuis le fichier CSV
df = pd.read_csv("resultat_jointure.csv")

# 2. Sélectionner les fonctionnalités pertinentes
features = df[['2017', '2018', '2019', '2020', '2021', '2022', 'Hommes_0-19', 'Hommes_20-39', 'Hommes_40-59', 'Hommes_60-74', 'Hommes_75plus', 'Femmes_0-19', 'Femmes_20-39', 'Femmes_40-59', 'Femmes_60-74', 'Femmes_75plus']]

# La cible de notre modèle sera le parti politique vainqueur en 2022
target = df['parti_politique_vainq2022']

# 3. Diviser les données en ensembles de formation et de test
X_train, X_test, y_train, y_test = train_test_split(features, target, test_size=0.2, random_state=42)

# 4. Entraîner un modèle de Random Forest
rf_model = RandomForestClassifier(n_estimators=100, random_state=42)
rf_model.fit(X_train, y_train)

# 5. Effectuer des prédictions sur toutes les données
all_predictions = rf_model.predict(features)

# 6. Stocker les prédictions dans un nouveau fichier CSV
predictions_df = pd.DataFrame({'Libelle_departement': df['Libelle_departement'], 'Prediction': all_predictions})
predictions_df.to_csv('prediction.csv', index=False)
