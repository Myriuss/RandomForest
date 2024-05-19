from sqlalchemy import create_engine
import pandas as pd

# connexion à la base de données
engine = create_engine('sqlite:///DatabaseFinal.db')

# Charger les fichiers CSV dans des DataFrames
pred2027_df = pd.read_csv("../Data/jointure_prediction.csv", sep=",", encoding='ISO-8859-1')
#pred2024_df = pd.read_csv("../Data/proba_2024.csv", sep=",", encoding='ISO-8859-1')
#pred2025_df = pd.read_csv("../Data/proba_2025.csv", sep=",", encoding='ISO-8859-1')
#pred2026_df = pd.read_csv("../Data/proba_2026.csv", sep=",", encoding='ISO-8859-1')

# Charger les DataFrames dans la base de données
pred2027_df.to_sql('DatabasePrediction', con=engine, if_exists='replace', index=False)
#pred2024_df.to_sql('pred2024_table', con=engine, if_exists='replace', index=False)
#pred2025_df.to_sql('pred2025_table', con=engine, if_exists='replace', index=False)
#pred2026_df.to_sql('pred2026_table', con=engine, if_exists='replace', index=False)
