# Importer la bibliothèque pandas pour manipuler les données
# Importer matplotlib pour les graphiques
import pandas as pd
import matplotlib.pyplot as plt

# Lire le fichier CSV contenant les données des voiture
df = pd.read_csv("car_prices.csv")

# Afficher les 5 premières lignes du DataFrame pour un aperçu des données
print(df.head())

# Supprimer certaines colonnes inutiles
df = df.drop(columns=["saledate"])        # Supprimer la colonne 'saledate'
df = df.drop(columns=["seller"])          # Supprimer la colonne 'seller'
df = df.drop(columns=["vin"])             # Supprimer la colonne 'vin' (numero d'identification du vehicule)
df = df.drop(columns=["transmission"])    # Supprimer la colonne 'transmission'
print(df.head())                          # Vérifier le DataFrame après suppression

# Ne garder que les 100 premières lignes pour simplifier l'analyse
df = df.head(100)
print(df)

# Afficher des informations générales sur les données (types, nombre de valeurs non nulles, etc.)
df.info()

# Remplacer les valeurs manquantes (NaN) par 0
df = df.fillna(0)

# Afficher un résumé statistique : count, mean, std, min, max, etc.
print(df.describe())

# Vérifier le nombre de valeurs manquantes par colonne
valeurs_manquantes = df.isnull().sum()
print("Nombre de valeurs manquantes par colonne :")
print(valeurs_manquantes)

# Créer un sous-ensemble du DataFrame avec des colonnes pertinentes
df_subset = df[["year", "make", "model", "odometer", "sellingprice"]]
df_subset.head()  # (ligne inutile ici sans print, on pourrait la retirer ou ajouter print)


# Filtrer les voiture avec un prix de vente supérieur à 50 000
voitures_chères = df_subset[df_subset["sellingprice"] > 50000]
print(voitures_chères)

# Filtrer les voitures de la marque BMW uniquement
df_filtered = df_subset[df_subset['make'] == 'BMW']
print(df_filtered)

# Créer une nouvelle colonne calculant le prix par kilomètre parcouru
df_subset['price_per_km'] = df_subset['sellingprice'] / df_subset['odometer']
print(df_subset)

# Trier les voitures par prix de vente décroissant
df_sorted = df_subset.sort_values(by='sellingprice', ascending=False)
print(df_sorted)

# Calcul de quelques statistiques sur les prix de vente
print("Moyenne prix :", df_subset['sellingprice'].mean())
print("Médiane prix :", df_subset['sellingprice'].median())
print("Écart-type prix :", df_subset['sellingprice'].std())

# Calculer le prix moyen par marque
grouped = df.groupby('make')['sellingprice'].mean().sort_values(ascending=False)
print(grouped)


# Afficher un histogramme des prix de vente
df_subset['sellingprice'].hist(bins=30)
plt.title('Répartition des prix de vente')
plt.xlabel('Prix')
plt.ylabel('Nombre de voitures')
plt.show()

# Tracer une courbe du prix moyen par marque
grouped.plot(kind='line')
plt.title('Prix moyen par marque')
plt.ylabel('Prix')
plt.show()
