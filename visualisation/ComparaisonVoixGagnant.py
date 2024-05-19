import pandas as pd
import matplotlib.pyplot as plt

# Charger le fichier CSV dans un DataFrame
df = pd.read_csv('../Data/resultat_jointure.csv')

# Liste des départements à sélectionner
departements_selectionnes = ['paris', 'seine-et-marne', 'yvelines', 'essonne', 'hauts-de-seine', 'seine-saint-denis', 'val-de-marne', "val-d'oise"]

# Filtrer les données pour les départements sélectionnés
filtered_df = df[df['Libelle_departement'].isin(departements_selectionnes)]

# Voix des vainqueurs pour les départements filtrés
departements = filtered_df['Libelle_departement']
voix_vainqueur_2017 = filtered_df['voix_vainqueur2017']
voix_vainqueur_2022 = filtered_df['voix_vainqueur2022']

# Créer une figure et des sous-graphiques
fig, ax = plt.subplots(figsize=(12, 8))

# Largeur des barres
width = 0.35

# Position des barres sur l'axe x
x = range(len(departements))

# Tracer les barres pour les voix des vainqueurs en 2017
ax.bar(x, voix_vainqueur_2017, width, label='2017')

# Tracer les barres pour les voix des vainqueurs en 2022
ax.bar([p + width for p in x], voix_vainqueur_2022, width, label='2022')

# Personnaliser le graphique
ax.set_xlabel('Département')
ax.set_ylabel('Voix du Vainqueur')
ax.set_title('Comparaison des Voix des Gagnants par Département')
ax.set_xticks([p + width / 2 for p in x])
ax.set_xticklabels(departements, rotation=45, ha='right')
ax.legend()

# Afficher le graphique
plt.tight_layout()  # Pour ajuster les labels correctement
plt.show()
