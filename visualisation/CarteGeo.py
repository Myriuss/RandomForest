import pandas as pd
import geopandas as gpd
import cartopy.crs as ccrs
import matplotlib.pyplot as plt
import cartopy.feature as cfeature

# Charger les données depuis le CSV
data = pd.read_csv("../Data/probabilities.csv")

# Charger les géométries des départements français
departements = gpd.read_file("departements.geojson")

# Trouver le parti politique gagnant pour chaque département en 2027
# Nous supprimons la colonne 'Libelle_departement' pour effectuer la recherche du parti gagnant
# car elle ne fait pas partie des partis politiques
partis = ['La France insoumise', 'Les Republicains', 'Rassemblement National', 'Renaissance', 'Union populaire republicaine']
data['winner'] = data[partis].idxmax(axis=1)

# Remplacer les valeurs NaN dans la colonne 'winner' par 'Unknown'
data['winner'] = data['winner'].fillna('Unknown')

# Fusionner les données avec les géométries des départements
merged_data = departements.merge(data, how='left', left_on='nom', right_on='Libelle_departement')

# Créer une carte de la France
fig = plt.figure(figsize=(10, 8))
ax = fig.add_subplot(1, 1, 1, projection=ccrs.PlateCarree())
ax.set_extent([-5, 10, 41, 52])  # Coordonnées pour encadrer la France

# Afficher les frontières des départements
ax.add_feature(cfeature.BORDERS, linestyle=':', linewidth=1)

# Créer une liste de couleurs pour chaque parti politique
colors = {'La France insoumise': 'blue', 'Les Republicains': 'green', 'Rassemblement National': 'red', 'Renaissance': 'orange', 'Union populaire republicaine': 'purple', 'Unknown': 'gray'}

# Afficher les départements colorés en fonction du parti politique gagnant
for index, row in merged_data.iterrows():
    winner = row['winner']
    # Vérifier si winner est dans le dictionnaire colors
    couleur = colors.get(winner, 'gray')  # Si winner n'est pas dans le dictionnaire, utiliser 'gray' par défaut
    ax.add_geometries([row['geometry']], ccrs.PlateCarree(), facecolor=couleur, edgecolor='black')

# Ajouter un titre
plt.title('Parti politique gagnant pour les élections présidentielles 2027 par département')

# Afficher la carte
plt.show()
