import pandas as pd
import matplotlib.pyplot as plt

# Charger le fichier CSV dans un DataFrame
df = pd.read_csv('../Data/resultat_jointure.csv')

# Sélectionner uniquement les données pour Paris
paris_data = df[df['Libelle_departement'] == 'paris']

# Créer une figure et des sous-graphiques
fig, ax = plt.subplots(figsize=(10, 6))

# Données pour hommes et femmes par tranche d'âge
labels = ['0-19', '20-39', '40-59', '60-74', '75plus']

# Largeur des barres
width = 0.35

# Position initiale des barres sur l'axe x
x = range(len(labels))

# Couleurs pour les hommes et les femmes
colors = ['#1f77b4', '#ff7f0e', '#2ca02c', '#d62728', '#9467bd']

# Boucle pour tracer les barres pour Paris uniquement
for i, label in enumerate(labels):
    # Données pour les hommes et les femmes
    hommes = paris_data[f'Hommes_{label}'].values[0]
    femmes = paris_data[f'Femmes_{label}'].values[0]

    # Tracer les barres pour les hommes
    ax.bar(x[i], hommes, width, label=f'Hommes - {label}', color=colors[i], alpha=0.7)

    # Tracer les barres pour les femmes
    ax.bar(x[i], femmes, width, bottom=hommes, label=f'Femmes - {label}', color=colors[i], alpha=0.7)

# Personnaliser le graphique
ax.set_xlabel('Tranche d\'Âge')
ax.set_ylabel('Population')
ax.set_title('Répartition de la Population par Tranche d\'Âge et Sexe pour Paris')
ax.set_xticks(x)
ax.set_xticklabels(labels)
ax.legend()
plt.xticks(rotation=45, ha='right')
plt.tight_layout()

# Afficher le graphique
plt.show()
