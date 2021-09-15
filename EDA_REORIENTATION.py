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



sondage = pd.read_csv('Reorientation Professionnelle.csv',error_bad_lines=False)
#Ici, on drop les columns inutiles
sondage_clean = sondage.drop(columns=['Nom et Prénom','Métier actuel', 'Le métier pour lequel vous aimeriez changer'])
#Ici, on renomme les deux dernières colonnes pour plus de simplicité
sondage_clean.rename(columns={"Catégorie_Pro_Actuelle": "Actuel", "Catégorie_Pro_Souhaitée": "Souhait"},inplace=True)



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
    def Actuel_Hist_F():
        fig, ax = plt.subplots(figsize= (15, 15))
        plt.xticks(fontsize=40,rotation=90)
        plt.yticks(fontsize=40)
        sns.histplot(data = sondage_F, x='Actuel',bins=1,hue='Actuel')
        plt.xlabel("Actuel", fontsize=60)
        plt.ylabel("Nombre de personnes", fontsize=26)
        plt.tight_layout(True)
    plot_Actuel_Hist_F = Actuel_Hist_F()
    st.pyplot(plot_Actuel_Hist_F)
    def Souhaite_Hist_F():
        fig, ax = plt.subplots(figsize= (15, 15))
        plt.xticks(fontsize=40,rotation=90)
        plt.yticks(fontsize=40)
        sns.histplot(data = sondage_F, x='Souhait',bins=1,hue='Souhait')
        plt.xlabel("Souhait", fontsize=60)
        plt.ylabel("Nombre de personnes", fontsize=26)
        plt.tight_layout(True)
    plot_Souhaite_Hist_F = Souhaite_Hist_F()
    st.pyplot(plot_Souhaite_Hist_F)
else :
    def Actuel_Hist_M():
        fig, ax = plt.subplots(figsize= (15, 15))
        plt.xticks(fontsize=40,rotation=90)
        plt.yticks(fontsize=40)
        sns.histplot(data = sondage_M, x='Actuel',bins=1,hue='Actuel')
        plt.xlabel("Actuel", fontsize=60)
        plt.ylabel("Nombre de personnes", fontsize=26)
        plt.tight_layout(True)
    plot_Actuel_Hist_M = Actuel_Hist_M()
    st.pyplot(plot_Actuel_Hist_M)
    def Souhaite_Hist_M():
        fig, ax = plt.subplots(figsize= (15, 15))
        plt.xticks(fontsize=40,rotation=90)
        plt.yticks(fontsize=40)
        sns.histplot(data = sondage_M, x='Actuel',bins=1,hue='Souhait')
        plt.xlabel("Souhait", fontsize=60)
        plt.ylabel("Nombre de personnes", fontsize=26)
        plt.tight_layout(True)
    plot_Souhaite_Hist_M = Souhaite_Hist_M()
    st.pyplot(plot_Souhaite_Hist_M)



st.title("Exploration des différentes orientations professionnelles selon l'âge des participants")

# if st.checkbox('Voir le graphe'):
# on réalise un subset du jeu de données en fonction du sexe
# age_slider = st.slider("Age de séparation de l'échantillon",25,60,35)
# sondage_J = sondage_clean.loc[sondage_clean['Age']<age_slider]
# sondage_MJ = sondage_clean.loc[sondage_clean['Age']>age_slider]

sondage_J = sondage_clean.loc[sondage_clean['Age']<35]
sondage_MJ = sondage_clean.loc[sondage_clean['Age']>35]







selectbox_S = st.selectbox('',('Avant la sélection','après la sélection'))
if selectbox_S == 'Avant la sélection':
    def Actuel_Hist_J():
        fig, ax = plt.subplots(figsize= (15, 15))
        plt.xticks(fontsize=40,rotation=90)
        plt.yticks(fontsize=40)
        sns.histplot(data = sondage_J, x='Actuel',bins=1,hue='Actuel')
        plt.xlabel("Actuel", fontsize=60)
        plt.ylabel("Nombre de personnes", fontsize=26)
        plt.tight_layout(True)
    plot_Actuel_Hist_J = Actuel_Hist_J()
    st.pyplot(plot_Actuel_Hist_J)
    def Souhaite_Hist_J():
        fig, ax = plt.subplots(figsize= (15, 15))
        plt.xticks(fontsize=40,rotation=90)
        plt.yticks(fontsize=40)
        sns.histplot(data = sondage_J, x='Souhait',bins=1,hue='Souhait')
        plt.xlabel("Souhait", fontsize=60)
        plt.ylabel("Nombre de personnes", fontsize=26)
        plt.tight_layout(True)
    plot_Souhaite_Hist_J = Souhaite_Hist_J()
    st.pyplot(plot_Souhaite_Hist_J)
else :
    def Actuel_Hist_MJ():
        fig, ax = plt.subplots(figsize= (15, 15))
        plt.xticks(fontsize=40,rotation=90)
        plt.yticks(fontsize=40)
        sns.histplot(data = sondage_MJ, x='Actuel',bins=1,hue='Actuel')
        plt.xlabel("Actuel", fontsize=60)
        plt.ylabel("Nombre de personnes", fontsize=26)
        plt.tight_layout(True)
    plot_Actuel_Hist_MJ = Actuel_Hist_MJ()
    st.pyplot(plot_Actuel_Hist_MJ)
    def Souhaite_Hist_MJ():
        fig, ax = plt.subplots(figsize= (15, 15))
        plt.xticks(fontsize=40,rotation=90)
        plt.yticks(fontsize=40)
        sns.histplot(data = sondage_MJ, x='Souhait',bins=1,hue='Souhait')
        plt.xlabel("Souhait", fontsize=60)
        plt.ylabel("Nombre de personnes", fontsize=26)
        plt.tight_layout(True)
    plot_Souhaite_Hist_MJ = Souhaite_Hist_MJ()
    st.pyplot(plot_Souhaite_Hist_MJ)
