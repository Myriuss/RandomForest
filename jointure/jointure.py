import pandas as pd

# Charger les fichiers CSV dans des DataFrames
pred2024_df = pd.read_csv("../Data/proba_2024.csv", sep=",", encoding='ISO-8859-1')
pred2025_df = pd.read_csv("../Data/proba_2025.csv", sep=",", encoding='ISO-8859-1')
pred2026_df = pd.read_csv("../Data/proba_2026.csv", sep=",", encoding='ISO-8859-1')
pred2027_df = pd.read_csv("../Data/proba_2027.csv", sep=",", encoding='ISO-8859-1')

# Renommer les colonnes des DataFrames sources en ajoutant le préfixe correspondant à l'année
pred2024_df.columns = [col + "_pred2024" if col != "Libelle_departement" else col for col in pred2024_df.columns]
pred2025_df.columns = [col + "_pred2025" if col != "Libelle_departement" else col for col in pred2025_df.columns]
pred2026_df.columns = [col + "_pred2026" if col != "Libelle_departement" else col for col in pred2026_df.columns]
pred2027_df.columns = [col + "_pred2027" if col != "Libelle_departement" else col for col in pred2027_df.columns]

# Effectuer la jointure entre les DataFrames
result = pred2027_df.merge(pred2024_df, on=["Libelle_departement"], how="inner") \
                   .merge(pred2025_df, on=["Libelle_departement"], how="inner") \
                   .merge(pred2026_df, on=["Libelle_departement"], how="inner")

# Afficher un aperçu du résultat
print(result.head())

# Enregistrer le résultat dans un nouveau fichier CSV
result.to_csv("../Data/jointure_prediction.csv", index=False)
