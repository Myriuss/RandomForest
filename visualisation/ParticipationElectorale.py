import pandas as pd
import matplotlib.pyplot as plt

# Charger le fichier CSV dans un DataFrame
df = pd.read_csv('../Data/resultat_jointure.csv')

# Liste des départements à sélectionner
departements_selectionnes = ['paris', 'seine-et-marne', 'yvelines', 'essonne', 'hauts-de-seine', 'seine-saint-denis', 'val-de-marne', "val-d'oise"]

# Filtrer les données pour les départements sélectionnés
filtered_df = df[df['Libelle_departement'].isin(departements_selectionnes)]

# Participation électorale pour les départements filtrés
departements = filtered_df['Libelle_departement']
votants_2017 = filtered_df['votants2017']
votants_2022 = filtered_df['votants2022']

x = range(len(departements))
width = 0.35

fig, ax = plt.subplots(figsize=(12, 8))
ax.bar(x, votants_2017, width, label='2017')
ax.bar([p + width for p in x], votants_2022, width, label='2022')

ax.set_xlabel('Département')
ax.set_ylabel('Nombre de Votants')
ax.set_title('Participation Électorale par Département')
ax.set_xticks([p + width / 2 for p in x])
ax.set_xticklabels(departements, rotation=45, ha='right')
ax.legend()
plt.tight_layout()  # Pour ajuster les labels correctement
plt.show()
