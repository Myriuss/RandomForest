import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.svm import SVC
from sklearn.neighbors import KNeighborsClassifier
from sklearn.preprocessing import StandardScaler
from sklearn.preprocessing import LabelEncoder
import warnings

# Ignorer les avertissements de non-convergence pour la régression logistique
warnings.filterwarnings("ignore")

# Lecture des données à partir d'un fichier CSV
df = pd.read_csv('Data/resultat_jointure.csv')

# Préparation des données
label_encoder = LabelEncoder()
df['parti_politique_vainq2017'] = label_encoder.fit_transform(df['parti_politique_vainq2017'])
df['parti_politique_vainq2022'] = label_encoder.transform(df['parti_politique_vainq2022'])

features = df[['2017', '2018', '2019', '2020', '2021', '2022',
               'Hommes_0-19', 'Hommes_20-39', 'Hommes_40-59',
               'Hommes_60-74', 'Hommes_75plus', 'Femmes_0-19',
               'Femmes_20-39', 'Femmes_40-59', 'Femmes_60-74',
               'Femmes_75plus', 'Population_Total',
               'emploi_2007', 'emploi_2008', 'emploi_2009',
               'emploi_2010', 'emploi_2011', 'emploi_2012',
               'emploi_2013', 'emploi_2014', 'emploi_2015',
               'emploi_2016', 'emploi_2017', 'emploi_2018',
               'emploi_2019', 'emploi_2020', 'emploi_2021',
               'emploi_2022']]

df_2017 = features.copy()
df_2017['target'] = df['parti_politique_vainq2017']
df_2017['year'] = 2017

df_2022 = features.copy()
df_2022['target'] = df['parti_politique_vainq2022']
df_2022['year'] = 2022

combined_df = pd.concat([df_2017, df_2022], ignore_index=True)

combined_features = combined_df.drop('target', axis=1)
combined_target = combined_df['target']

X_train, X_test, y_train, y_test = train_test_split(combined_features, combined_target, test_size=0.2, random_state=42)

# Mise à l'échelle des données
scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)

# Définition des modèles à évaluer
models = {
    "Random Forest": RandomForestClassifier(n_estimators=100, random_state=42),
    "Logistic Regression": LogisticRegression(max_iter=1000, solver='saga', random_state=42),
    "Support Vector Classifier": SVC(kernel='linear', random_state=42),
    "K-Nearest Neighbors": KNeighborsClassifier()
}

# Entraînement et évaluation des modèles
for model_name, model in models.items():
    if model_name == "Logistic Regression":
        model.fit(X_train_scaled, y_train)
        accuracy = model.score(X_test_scaled, y_test)
    else:
        model.fit(X_train, y_train)
        accuracy = model.score(X_test, y_test)
    print(f"Accuracy of {model_name}: {accuracy}")
