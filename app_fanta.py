
import streamlit as st
import pandas as pd
from streamlit_tags import st_tags
import requests
from io import StringIO


def load_original_data():
    url = 'https://raw.githubusercontent.com/[username]/[repository]/main/[file].csv'
    response = requests.get(url)
    if response.status_code == 200:
        return pd.read_csv(StringIO(response.text))
    else:
        st.error("Failed to load data from GitHub.")
        return None

df = pd.read_excel("C:/Users/bront/OneDrive/Desktop/fanta.xlsx")
st.title('Fanta')
keywords = st_tags(label='# Inserisci giocatore:', text='Press enter to add more', value="",
                       suggestions=df["Nome"].tolist())
statistiche = ["Pv", "Mv", "Fm", "Gf", "Gs", "Rp", "Rc", "R+", "R-", "Ass", "Amm", "Esp", "Au"]
gioc = " ".join(keywords)
df.set_index("Nome",inplace=True)
if len(gioc.split()) == 1:
    st.write(f"Squadra: {df.loc[gioc.capitalize(),"Squadra"]}")
    if df.loc[gioc.capitalize(), "Diff."] >= 0:
        st.write("Status: Hyped")
    else:
        st.write("Status: No hype")
    st.write(f"Attributi: {df.loc[gioc.capitalize(), "attributi"]}")
    st.write(f"Resistenza Infortuni: {df.loc[gioc.capitalize(), "Res. Inf."]}")
    if not all(df.loc[gioc.capitalize(), [ u + " 23_24" for u in statistiche] ]):
        st.write(["Statistiche 23-24:",f" {df.loc[gioc.capitalize(), [ u + " 23_24" for u in statistiche] ]}"])
    if not all(df.loc[gioc.capitalize(), [ u + " 22_23" for u in statistiche] ]):
        st.write(["Statistiche 22-23:",f" {df.loc[gioc.capitalize(), [ u + " 22_23" for u in statistiche] ]}"])
    if not all(df.loc[gioc.capitalize(), statistiche]):
        st.write(["Statistiche 21-22:",f" {df.loc[gioc.capitalize(),  statistiche] }"])


elif len(gioc.split())>1:
    y = [u.capitalize() for u in gioc.split()]
    x = " ".join(y)
    print(gioc)

    st.write(f"Squadra: {df.loc[x,"Squadra"]}")
    if df.loc[x, "Diff."] >= 0:
        st.write("Status: Hyped")
    else:
        st.write("Status: No hype")

    st.write(f"Attributi: {df.loc[x, "attributi"]}")
    st.write(f"Resistenza Infortuni: {df.loc[x, "Res. Inf."]}")

    if not all(df.loc[x, [u + " 23_24" for u in statistiche]].isna()):
       st.write(f"Statistiche 23-24: {df.loc[x, [u + " 23_24" for u in statistiche]]}")
    if not all(df.loc[x, [u + " 22_23" for u in statistiche]].isna()):
        st.write(f"Statistiche 22-23: {df.loc[x, [u + " 22_23" for u in statistiche]]}")
    if not all(df.loc[x,statistiche].isna()):
        st.write(f"Statistiche 21-22: {df.loc[x, statistiche]}")

