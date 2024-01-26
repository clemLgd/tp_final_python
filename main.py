import pandas as pd
import matplotlib.pyplot as plt

df23 = pd.read_csv("./valeursfoncieres-2023.txt", sep='|')
df19 = pd.read_csv("./valeursfoncieres-2019.txt", sep='|')

def nettoyer_donnees(df):
    dflocal = df
    dflocal["Valeur fonciere"] = dflocal['Valeur fonciere'].str.replace(',', '.').astype(float)
    suppression_colonnes = ['Identifiant de document', 'Reference document', '1 Articles CGI',
       '2 Articles CGI', '3 Articles CGI', '4 Articles CGI', '5 Articles CGI']
    dflocal = dflocal.drop(columns=suppression_colonnes)
    return dflocal

df19 = nettoyer_donnees(df19)
df23 = nettoyer_donnees(df23)

# vérification
print(df23.columns)
print(df19.columns)

def pmpd(df):
    # prix moyen par département (pmpd)
    pmpd = df.groupby("Code departement")["Valeur fonciere"].mean()
    pmpd.plot(kind="bar", figsize=(12,6))
    plt.title("Valeur foncière par département")
    plt.xlabel("Département")
    plt.ylabel("Valeur foncière")
    plt.show()
def pmtb(df):
    # prix moyen par type de bien (pmtb)
    pmtb = df.groupby("Type local")["Valeur fonciere"].mean()
    pmtb.plot(kind="bar", figsize=(10,6))
    plt.title("Comparaison des prix maisons/appartements")
    plt.xlabel("Type du bien")
    plt.ylabel("Prix moyen par type de bien")
    plt.show()
def pmv(df):
    # prix moyen par ville (pmv)
    pmv = df.groupby("Commune")["Valeur fonciere"].mean()
    pmv.plot(figsize=(20,20))
    plt.title("Prix moyen par ville")
    plt.xlabel("Villes")
    plt.xticks(rotation=90) # pour la lisibilité on écrit les villes à la verticale
    plt.ylabel("Prix")
    plt.tight_layout() # améliore la lisibilité du graphe
    plt.show()
def smtb(df):
    # surface du terrain par type de bien (smtb)
    smtb = df.groupby("Type local")["Surface terrain"].mean()
    smtb.plot(kind="bar", figsize=(12,6))
    plt.title("Surface moyenne par type de bien")
    plt.xlabel("Type du bien")
    plt.ylabel("Surface en mètre carré")
    plt.show()
def vnp(df):
    # Valeur en fonction du nombre de pièce (vnp)
    vnp = df.groupby("Nombre pieces principales")["Valeur fonciere"].mean()
    vnp.plot(kind="bar", figsize=(12,6))
    plt.title("Valeur en fonction du nombre de pièce")
    plt.xlabel("Nombre de pièce")
    plt.ylabel("Prix")
    plt.show()
def vmtv(df):
    # Valeur moyenne en fonction du type de voie
    vmtv = df.groupby("Type de voie")["Valeur fonciere"].mean()
    vmtv.plot(kind="bar")
    plt.title("Valeur moyenne en fonction du type de voie")
    plt.xlabel("Type de voie")
    plt.ylabel("Prix")
    plt.show()

def nmfc(df):
    # n premières communes en termes de nombre de mutations
    top_communes = df['Commune'].value_counts().head(10).index
    df_top = df[df['Commune'].isin(top_communes)]

    # Nature mutation en fonction de la commune
    nmfc = df_top.groupby("Commune")["Nature mutation"].value_counts().unstack()
    nmfc.plot(kind="bar", stacked=True, figsize=(12, 6))
    plt.title("Nature mutation pour les 10 premières communes avec le plus grand nombre de mutations")
    plt.xlabel("Commune")
    plt.ylabel("Nombre de mutations")
    plt.show()

def vmnc(df):
    # Valeur moyenne en fonction de la nature culture
    vmtv = df.groupby("Nature culture")["Valeur fonciere"].mean()
    vmtv.plot(kind="bar")
    plt.title("Valeur moyenne en fonction de la nature culture")
    plt.xlabel("Type de nature")
    plt.ylabel("Prix")
    plt.show()
def vmncs(df):
    # Valeur moyenne en fonction de la nature culture spéciale
    vmtv = df.groupby("Nature culture speciale")["Valeur fonciere"].mean()
    vmtv.plot(kind="bar",figsize=(30,6))
    plt.title("Valeur moyenne en fonction de la nature culture spéciale")
    plt.xlabel("Type de nature spéciale")
    plt.ylabel("Prix")
    plt.show()   

def smnp(df):
    # Surface moyenne réelle bâtie en fonction du nombre de pièces principales
    smnp = df.groupby("Nombre pieces principales")["Surface reelle bati"].mean()
    smnp.plot(kind="bar")
    plt.title("Surface moyenne réelle en fonction du nombre de pièces principales")
    plt.xlabel("Nombre pieces principales")
    plt.ylabel("Surface réelle")
    plt.show()
def mcd(df):
   # Nombre de mutations comportant des dépendances
    mutations_dep = df[df["Type local"] == "Dépendance"]
    mutations_dep_nb = mutations_dep.shape[0]
    mutations_sans_dep = df[df["Type local"] != "Dépendance"]
    mutations_sans_dep_nb = mutations_sans_dep.shape[0]
    labels = ['Avec dépendances', 'Sans dépendances']
    sizes = [mutations_dep_nb, mutations_sans_dep_nb]
    colors = ['#ff9999', '#66b3ff']
    fig1, ax1 = plt.subplots()
    ax1.pie(sizes, labels=labels, autopct='%1.1f%%', startangle=90, colors=colors)
    ax1.axis('equal') 
    plt.title("Répartition des mutations avec/sans dépendances")
    plt.show()
def nlm(df):
    # Nombre de lots dans les mutations
    mutations_with_lots = df[df["Nombre de lots"] > 0]
    lots_count_distribution = mutations_with_lots["Nombre de lots"].value_counts()
    lots_count_distribution.plot(kind="bar")
    plt.title("Nombre de Lots en fonction du nombre de mutations")
    plt.xlabel("Nombre de Lots")
    plt.ylabel("Nombre de Mutations")
    plt.show()
def stv(df):
    # Surface réelle bâtie moyenne pour différents types de voies
    average_surface_by_voie = df.groupby("Type de voie")["Surface reelle bati"].mean()
    average_surface_by_voie.plot(kind="bar")
    plt.title("Surface réelle bâtie moyenne par type de voie")
    plt.xlabel("Type de Voie")
    plt.ylabel("Surface Réelle Bâtie Moyenne")
    plt.show()

def mctl(df):
    # Mutations en fonction du code type local
    code_type_local_distribution = df["Code type local"].value_counts()
    code_type_local_distribution.plot(kind="bar")
    plt.title("Mutations en fonction du type local")
    plt.xlabel("Code Type Local")
    plt.ylabel("Nombre de Mutations")
    plt.show()
def nppp(df):
    # Nombre de pièces principales dans les propriétés
    pieces_principales_distribution = df["Nombre pieces principales"].value_counts()
    pieces_principales_distribution.plot(kind="bar")
    plt.title("Nombre de pièces principales par mutation")
    plt.xlabel("Nombre de Pièces Principales")
    plt.ylabel("Nombre de Mutations")
    plt.show()
def mtt(df):
    # Mutations en fonction du type de terrain
    type_terrain_distribution = df["Nature culture"].value_counts()
    type_terrain_distribution.plot(kind="bar")
    plt.title("Distribution des Mutations par Type de Terrain")
    plt.xlabel("Type de Terrain")
    plt.ylabel("Nombre de Mutations")
    plt.show()
def dvpm(df):
   #Identifier les départements/villes au mètre carré différents de la norme
    pmv_commune = df.groupby("Commune")["Valeur fonciere"].mean()
    pmv_commune.plot(figsize=(20, 10), kind='bar', title='Prix moyen au mètre carré par Commune') 
    plt.figure(figsize=(20, 10))
    grouped_data = [df[df['departement'] == dept]['prix_m2'].dropna().tolist() for dept in df['departement'].unique()]
    plt.boxplot(grouped_data, labels=df['departement'].unique(), vert=False)
   
    plt.title('Variation des Prix au mètre carré par Département')
    plt.xlabel('Département')
    plt.ylabel('Prix au mètre carré')
    
    plt.show()
  
def rgmd(df):
    # Répartition géographique des mutations par département
    nb_departements = df["Code departement"].value_counts().head(10)
    nb_departements.plot(kind="bar")
    plt.title("10 premières mutations par département")
    plt.xlabel("Code du département")
    plt.ylabel("Nombre de mutations")
    plt.show()
def smtl(df):
    # Surface moyenne par type local
    smtl = df.groupby("Type local")["Surface reelle bati"].mean().sort_values(ascending=False)
    smtl.plot(kind="bar")
    plt.title("Surface moyenne par type local")
    plt.xlabel("Type local")
    plt.ylabel("Surface moyenne")
    plt.show()
def mpc(df):
    # Mutations par commune
    mutations_par_commune = df["Commune"].value_counts().sort_values(ascending=False).head(10)
    plt.figure(figsize=(12, 6))
    mutations_par_commune.plot(kind="bar")
    plt.title("Top 10 des communes avec le plus grand nombre de mutations")
    plt.xlabel("Commune")
    plt.ylabel("Nombre de mutations")
    plt.xticks(rotation=45, ha='right')
    plt.show()

# entre 2023 et 2019 --------------------------------------------------------
def evmd(df,df19):
    # Calcul du prix moyen par département pour chaque année
    pmv_2023 = df.groupby("Code departement")["Valeur fonciere"].mean()
    pmv_2019 = df19.groupby("Code departement")["Valeur fonciere"].mean()
    # Fusion des données de 2019 et 2023
    pmv_combined = pd.concat([pmv_2019, pmv_2023], axis=1)
    pmv_combined.columns = ['2019', '2023']
    # Ajouter une colonne représentant l'écart des prix entre 2019 et 2023
    pmv_combined['Écart des prix'] = pmv_combined['2023'] - pmv_combined['2019']
    plt.figure(figsize=(30, 15))
    # Affichage de l'écart des prix sur un autre graphique
    plt.subplot(2, 1, 2)
    pmv_combined['Écart des prix'].plot(kind='bar', color='green')
    plt.title("Écart de la valeur moyenne entre 2019 et 2023 par département")
    plt.xlabel("Département")
    plt.ylabel("Écart des prix")
    plt.xticks(range(len(pmv_combined.index)), pmv_combined.index, rotation=90)
    plt.tight_layout()
    plt.show()  

def evmtb(df,df19):
    # Calcul du prix moyen par type de bien pour chaque année
    pmv_2023 = df.groupby("Type local")["Valeur fonciere"].mean()
    pmv_2019 = df19.groupby("Type local")["Valeur fonciere"].mean()
    # Fusion des données de 2019 et 2023
    pmv_combined = pd.concat([pmv_2019, pmv_2023], axis=1)
    pmv_combined.columns = ['2019', '2023']
    # Ajouter une colonne représentant l'écart des prix entre 2019 et 2023
    pmv_combined['Écart des prix'] = pmv_combined['2023'] - pmv_combined['2019']
    plt.figure(figsize=(30, 15))
    # Affichage de l'écart des prix sur un autre graphique
    plt.subplot(2, 1, 2)
    pmv_combined['Écart des prix'].plot(kind='bar', color='green')
    plt.title("Écart de la valeur moyenne entre 2019 et 2023 par type de bien")
    plt.xlabel("Type du bien")
    plt.ylabel("Écart des prix")
    plt.xticks(range(len(pmv_combined.index)), pmv_combined.index, rotation=90)
    plt.tight_layout()
    plt.show()
    
def nlpd(df,df19):
    # Calcul du nombre de lots par département pour 2019 et 2023
    lots_2019 = df19.groupby("Code departement")["Nombre de lots"].sum()
    lots_2023 = df.groupby("Code departement")["Nombre de lots"].sum()
    # Convertir l'index en chaînes de caractères pour la compatibilité avec le diagramme en barres
    lots_2019.index = lots_2019.index.astype(str)
    lots_2023.index = lots_2023.index.astype(str)
    # Comparaison visuelle
    plt.figure(figsize=(30, 6))
    plt.bar(lots_2019.index, lots_2019, color='blue', label='2019')
    plt.bar(lots_2023.index, lots_2023, color='orange', label='2023')
    plt.title("Comparaison du nombre de lots par département en 2019 et 2023")
    plt.xlabel("Code département")
    plt.ylabel("Nombre de lots")
    plt.legend()
    plt.xticks(rotation=45)
    plt.show()

def pmtvd(df23, df19):
    # Prix moyen par type de voie entre deux années
    pmtv_2023 = df23.groupby("Type de voie")["Valeur fonciere"].mean()
    pmtv_2019 = df19.groupby("Type de voie")["Valeur fonciere"].mean()
    
    plt.figure(figsize=(30, 15))
    plt.bar(pmtv_2019.index, pmtv_2019, color="blue")
    plt.bar(pmtv_2023.index, pmtv_2023, color="orange")

    plt.title("Prix moyen par type de voie entre deux années")
    plt.xlabel("Prix moyen")
    plt.ylabel("Type de voie")
    plt.legend()
    plt.tight_layout()
    plt.show()


def stpd(df,df19):
    # Calcul de la surface de terrain par département pour 2019 et 2023
    lots_2019 = df19.groupby("Code departement")["Surface terrain"].sum()
    lots_2023 = df.groupby("Code departement")["Surface terrain"].sum()
    # Convertir l'index en chaînes de caractères pour la compatibilité avec le diagramme en barres
    lots_2019.index = lots_2019.index.astype(str)
    lots_2023.index = lots_2023.index.astype(str)
    # Comparaison visuelle
    plt.figure(figsize=(30, 6))
    plt.bar(lots_2019.index, lots_2019, color='blue', label='2019')
    plt.bar(lots_2023.index, lots_2023, color='orange', label='2023')
    plt.xlabel("Code département")
    plt.ylabel("Surface de terrain")
    plt.legend()
    plt.xticks(rotation=45)
    plt.show()