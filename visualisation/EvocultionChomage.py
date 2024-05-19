import pandas as pd
import matplotlib.pyplot as plt

# Charger le fichier CSV dans un DataFrame
df = pd.read_csv('../Data/resultat_jointure.csv')

# Filtrer les données pour le département 'Ain' (ou un autre)
paris = df[df['Libelle_departement'] == 'paris']

# Années et taux de chômage
annees = [2017, 2018, 2019, 2020, 2021, 2022]
taux_chomage = paris[['2017', '2018', '2019', '2020', '2021', '2022']].values.flatten()

plt.plot(annees, taux_chomage, marker='o')
plt.title("Évolution du Taux de Chômage à Paris")
plt.xlabel("Année")
plt.ylabel("Taux de Chômage (%)")
plt.grid(True)
plt.show()