import streamlit as st
import pandas as pd
from streamlit_tags import st_tags
import plotly.graph_objects as go
import os


df = pd.read_excel("C:/Users/bront/OneDrive/Desktop/fanta.xlsx")
st.title('Fanta')


keywords = st_tags(label='# Inserisci giocatore:',text='Press enter to add more',value="",suggestions=df["Nome"].tolist())

gioc = " ".join(keywords)
df.set_index("Nome",inplace=True)
print(gioc)
if gioc:
    st.write(f"Squadra: {df.loc[gioc.capitalize(),"Squadra"]}")
    st.write(f"Attributi: {df.loc[gioc.capitalize(), "attributi"]}")
    st.write(f"Resistenza Infortuni: {df.loc[gioc.capitalize(), "Res. Inf."]}")
    st.write(f"Statistiche 21-22: {df.loc[gioc.capitalize(), ["Pv","Mv","Fm","Gf","Gs","Rp","Rc","R+","R-","Ass","Amm","Esp","Au"]]}")
