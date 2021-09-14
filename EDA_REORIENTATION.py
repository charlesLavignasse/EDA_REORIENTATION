import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
import streamlit as st
import matplotlib
from matplotlib.ticker import EngFormatter
import base64
from wordcloud import WordCloud
matplotlib.use('Agg')
sns.reset_orig()

chemin_Data = "/app/Data/"

sondage = pd.read_csv('Reorientation Professionnelle.csv',error_bad_lines=False)
#Ici, on drop les columns inutiles
sondage_clean = sondage.drop(columns=['Nom et Prénom','Métier actuel', 'Le métier pour lequel vous aimeriez changer'])
#Ici, on renomme les deux dernières colonnes pour plus de simplicité
sondage_clean.rename(columns={"Catégorie_Pro_Actuelle": "Actuel", "Catégorie_Pro_Souhaitée": "Souhait"},inplace=True)

#chemin_Data=

st.title("Analyse des souhaits de réorientation professionnelle d'un échantillon d'une trentaine de personne")

if st.checkbox('Voir les explications:'):
    st.write("Les résultats du sondage ont étés simplifiés, par exemple, les professions telles qu'infirmières, aides soignantes, kinésithérapeutes ont étés renomées en 'Auxiliaires de santé'")
    st.write('\n')
    st.write("Ces changements arbitraires servent à simplifier l'échantillon afin d'essayer d'y déceler des similitudes entre typologies")




if st.checkbox('Voir les données et leur transformation'):
    #Création du slider de selection du nombre de lignes
    nombre_lignes_a_visualiser = st.slider("Nombre de lignes à visualiser",0,28,5)
    #Affichage du dataset
    st.write(sondage.head(nombre_lignes_a_visualiser))
    #Commentaire sur la modification du dataset
    st.header("on ne conserve que la donnée pertinente")
    st.write(sondage_clean.head(nombre_lignes_a_visualiser))

selectbox_WD = st.selectbox('Situation Professionnelle : ',('Actuelle','Souhaitée'))

if selectbox_WD == 'Actuelle':
    st.write('Nuage de mots regroupant les situations professionnelles actuelles des participants')
    #Nuage de mots sur Actuel
    def wdcld_Actuel():
        text =  ' '.join(sondage_clean["Actuel"])
        exclure_mots = ['d', 'du', 'de', 'la', 'des', 'le', 'et', 'est', 'elle', 'une', 'en', 'que', 'aux', 'qui', 'ces', 'les', 'dans', 'sur', 'l', 'un', 'pour', 'par', 'il', 'ou', 'à', 'ce', 'a', 'sont', 'cas', 'plus', 'leur', 'se', 's', 'vous', 'au', 'c', 'aussi', 'toutes', 'autre', 'comme']
        wordcloud = WordCloud(background_color = 'white', stopwords = exclure_mots, max_words = 50).generate(text)
        plt.imshow(wordcloud)
        plt.axis("off")
    plot_wdcld_Actuel = wdcld_Actuel()
    st.pyplot(plot_wdcld_Actuel)

else :
    st.write('Nuage de mots qui regroupe les situations professionnelles actuelles des participants')
#Nuage de mots sur Actuel
    def wdcld_Souhait():
        text =  ' '.join(sondage_clean["Souhait"])
        exclure_mots = ['d', 'du', 'de', 'la', 'des', 'le', 'et', 'est', 'elle', 'une', 'en', 'que', 'aux', 'qui', 'ces', 'les', 'dans', 'sur', 'l', 'un', 'pour', 'par', 'il', 'ou', 'à', 'ce', 'a', 'sont', 'cas', 'plus', 'leur', 'se', 's', 'vous', 'au', 'c', 'aussi', 'toutes', 'autre', 'comme']
        wordcloud = WordCloud(background_color = 'white', stopwords = exclure_mots, max_words = 50).generate(text)
        plt.imshow(wordcloud)
        plt.axis("off")
    plot_wdcld_Souhait = wdcld_Souhait()
    st.pyplot(plot_wdcld_Souhait)

st.title('Exploration des différentes orientations professionnelles selon le sexe des participants')

#on réalise un subset du jeu de données en fonction du sexe
sondage_F = sondage_clean.loc[sondage_clean['Sexe']=='F']
sondage_M = sondage_clean.loc[sondage_clean['Sexe']=='M']

selectbox_S = st.selectbox('',('Femmes','Hommes'))
if selectbox_S == 'Femmes':
        def Actuel_Hist():
            fig, ax = plt.subplots(figsize= (50, 50))
            plt.xticks(fontsize=40,rotation=90)
            plt.yticks(fontsize=40)
            sns.histplot(data = sondage_F, x='Actuel',bins=1,hue='Actuel')
            plt.xlabel("Actuel", fontsize=60)
            plt.ylabel("Nombre de personnes", fontsize=26)
            plt.tight_layout(True)
        plot_Actuel_Hist = Actuel_Hist()
        st.pyplot(plot_Actuel_Hist)
        def Souhaite_Hist():
            fig, ax = plt.subplots(figsize= (50, 50))
            plt.xticks(fontsize=40,rotation=90)
            plt.yticks(fontsize=40)
            sns.histplot(data = sondage_F, x='Souhait',bins=1,hue='Souhait')
            plt.xlabel("Souhait", fontsize=60)
            plt.ylabel("Nombre de personnes", fontsize=26)
            plt.tight_layout(True)
        plot_Actuel_Hist = Souhaite_Hist()
        st.pyplot(plot_Actuel_Hist)
else :
        def Actuel_Hist():
            fig, ax = plt.subplots(figsize= (30, 20))
            plt.xticks(fontsize=40,rotation=90)
            plt.yticks(fontsize=40)
            sns.histplot(data = sondage_M, x='Actuel',bins=1,hue='Actuel')
            plt.xlabel("Actuel", fontsize=60)
            plt.ylabel("Nombre de personnes", fontsize=26)
            plt.tight_layout(True)
        plot_Actuel_Hist = Actuel_Hist()
        st.pyplot(plot_Actuel_Hist)
        def Souhaite_Hist():
            fig, ax = plt.subplots(figsize= (30, 20))
            plt.xticks(fontsize=40,rotation=90)
            plt.yticks(fontsize=40)
            sns.histplot(data = sondage_M, x='Actuel',bins=1,hue='Souhait')
            plt.xlabel("Souhait", fontsize=60)
            plt.ylabel("Nombre de personnes", fontsize=26)
            plt.tight_layout(True)
        plot_Actuel_Hist = Souhaite_Hist()
        st.pyplot(plot_Actuel_Hist)



st.title("Exploration des différentes orientations professionnelles selon l'âge des participants")

#on réalise un subset du jeu de données en fonction du sexe
age_slider = st.slider("Age de séparation de l'échantillon",25,60,35)
sondage_J = sondage_clean.loc[sondage_clean['Age']<age_slider]
sondage_MJ = sondage_clean.loc[sondage_clean['Age']>age_slider]

selectbox_S = st.selectbox('',('Avant la sélection','après la sélection'))
if selectbox_S == 'Avant la sélection':
        def Actuel_Hist():
            fig, ax = plt.subplots(figsize= (50, 50))
            plt.xticks(fontsize=40,rotation=90)
            plt.yticks(fontsize=40)
            sns.histplot(data = sondage_J, x='Actuel',bins=1,hue='Actuel')
            plt.xlabel("Actuel", fontsize=60)
            plt.ylabel("Nombre de personnes", fontsize=26)
            plt.tight_layout(True)
        plot_Actuel_Hist = Actuel_Hist()
        st.pyplot(plot_Actuel_Hist)
        def Souhaite_Hist():
            fig, ax = plt.subplots(figsize= (50, 50))
            plt.xticks(fontsize=40,rotation=90)
            plt.yticks(fontsize=40)
            sns.histplot(data = sondage_J, x='Souhait',bins=1,hue='Souhait')
            plt.xlabel("Souhait", fontsize=60)
            plt.ylabel("Nombre de personnes", fontsize=26)
            plt.tight_layout(True)
        plot_Actuel_Hist = Souhaite_Hist()
        st.pyplot(plot_Actuel_Hist)
else :
        def Actuel_Hist():
            fig, ax = plt.subplots(figsize= (30, 20))
            plt.xticks(fontsize=40,rotation=90)
            plt.yticks(fontsize=40)
            sns.histplot(data = sondage_M, x='Actuel',bins=1,hue='Actuel')
            plt.xlabel("Actuel", fontsize=60)
            plt.ylabel("Nombre de personnes", fontsize=26)
            plt.tight_layout(True)
        plot_Actuel_Hist = Actuel_Hist()
        st.pyplot(plot_Actuel_Hist)
        def Souhaite_Hist():
            fig, ax = plt.subplots(figsize= (30, 20))
            plt.xticks(fontsize=40,rotation=90)
            plt.yticks(fontsize=40)
            sns.histplot(data = sondage_M, x='Actuel',bins=1,hue='Souhait')
            plt.xlabel("Souhait", fontsize=60)
            plt.ylabel("Nombre de personnes", fontsize=26)
            plt.tight_layout(True)
        plot_Actuel_Hist = Souhaite_Hist()
        st.pyplot(plot_Actuel_Hist)
# def Actuel_Hist():
#     fig, ax = plt.subplots(figsize= (30, 20))
#     plt.xticks(fontsize=40,rotation=90)
#     plt.yticks(fontsize=40)
#     sns.histplot(data = sondage_clean, x='Actuel',bins=2,hue = 'Actuel')
#     plt.xlabel("Actuel", fontsize=60)
#     plt.ylabel("Nombre de personnes", fontsize=26)
#     plt.tight_layout(True)
# plot_Actuel_Hist = Actuel_Hist()
# st.pyplot(plot_Actuel_Hist)

# def Age_Hist():
#     fig, ax = plt.subplots(figsize= (30, 20))
#
#     sns.histplot(data = sondage_clean, x='Age',bins=50,kde=True)
#     plt.xlabel("Age", fontsize=60)
#     plt.ylabel("Nombre de personnes", fontsize=60)
#     plt.xticks(fontsize=15,rotation=60,ticks=(np.arange(25,60, step = 1)))
#     plt.xticks(fontsize=40)
# plot_Age_Hist = Age_Hist()
# st.pyplot(plot_Age_Hist)
# st.write("La majorité de l'échantillon se situe autour de 30 ans")

# def Sexe_Hist():
#     fig, ax = plt.subplots(figsize= (30, 20))
#     plt.xticks(fontsize=40)
#     plt.yticks(fontsize=40)
#     sns.histplot(data = sondage_clean, x='Sexe',bins=2,hue = 'Sexe')
#     plt.xlabel("Sexe", fontsize=60)
#     plt.ylabel("Nombre de personnes", fontsize=26)
# plot_Sexe_Hist = Sexe_Hist()
# st.pyplot(plot_Sexe_Hist)







# def Age_Actuel():
#     fig, ax = plt.subplots(figsize= (30, 20))
#     sns.barplot(x = 'Actuel', y = "Age", data = sondage_clean,hue='Actuel', dodge = False)
#     plt.xticks(fontsize=19,rotation=90)
#     plt.yticks(fontsize=17)
#     plt.xlabel("Actuel", fontsize=24)
#     plt.ylabel("Age", fontsize=26)
#     plt.title("Représentation du Actuel pro en fonction de l'age", fontsize=28)
#     plt.show()
# plot_Age_Actuel = Age_Actuel()
# st.pyplot(plot_Age_Actuel)

# def Age_Souhait():
#     fig, ax = plt.subplots(figsize= (30, 20))
#     sns.barplot(x = 'Souhait', y = "Age", data = sondage_clean,hue='Souhait', dodge = False)
#     plt.xticks(fontsize=19,rotation=90)
#     plt.yticks(fontsize=17)
#     plt.xlabel("Souhait", fontsize=24)
#     plt.ylabel("Age", fontsize=26)
#     plt.title("Représentation du souhait pro en fonction de l'age", fontsize=28)
#     plt.show()
# plot_Age_Souhait = Age_Souhait()
# st.pyplot(plot_Age_Souhait)
