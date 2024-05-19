import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


# Charger le fichier CSV dans un DataFrame
df = pd.read_csv('../Data/resultat_jointure.csv')

# Sélectionner les colonnes pertinentes pour la corrélation
cols = ['2017', '2018', '2019', '2020', '2021', '2022', 'votants2017', 'voix_vainqueur2017', 'votants2022', 'voix_vainqueur2022', 'Hommes_0-19', 'Hommes_20-39', 'Hommes_40-59', 'Hommes_60-74', 'Hommes_75plus', 'Femmes_0-19', 'Femmes_20-39', 'Femmes_40-59', 'Femmes_60-74', 'Femmes_75plus']
corr = df[cols].corr()

plt.figure(figsize=(12, 10))
sns.heatmap(corr, annot=True, cmap='coolwarm', fmt='.2f')
plt.title('Heatmap des Corrélations')
plt.show()
