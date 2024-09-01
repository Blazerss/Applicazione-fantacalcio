import streamlit as st
import pandas as pd
from streamlit_tags import st_tags
url= "https://raw.githubusercontent.com/Blazerss/Blazerss/main/fanta.csv"
df = pd.read_csv(url)
st.title('Fanta')
keywords = st_tags(label='# Inserisci giocatore:', text='Press enter to add more', value="", suggestions=df["Nome"].tolist())

statistiche = ["Pv", "Mv", "Fm", "Gf", "Gs", "Rp", "Rc", "R+", "R-", "Ass", "Amm", "Esp", "Au"]
gioc = " ".join(keywords)
print(gioc)
df.set_index("Nome",inplace=True)
col1,col2,col3,col4=st.columns(4,gap="medium")
with col1:
   st.write("**Generali**")
   if len(gioc.split()) == 1:
       st.write(f"Squadra: {df.loc[gioc.capitalize(),"Squadra"]}")
       if df.loc[gioc.capitalize(), "Diff."] >= 0:
           st.write("Status: Hyped")
       else:
           st.write("Status: No hype")
       st.write(f"Attributi: {df.loc[gioc.capitalize(), "attributi"]}")
       st.write(f"Resistenza Infortuni: {df.loc[gioc.capitalize(), "Res. Inf."]}")

   elif len(gioc.split())>1:
       y = [u.capitalize() for u in gioc.split()]
       x = " ".join(y)

       st.write(f"Squadra: {df.loc[x,"Squadra"]}")
       if df.loc[x, "Diff."] >= 0:
           st.write("Status: Hyped")
       else:
           st.write("Status: No hype")

       st.write(f"Attributi: {df.loc[x, "attributi"]}")
       st.write(f"Resistenza Infortuni: {df.loc[x, "Res. Inf."]}")



with col2:
    st.write("**Stagione 23-24**")
    if len(gioc.split()) == 1:
        if not all(df.loc[gioc.capitalize(), [u + " 23_24" for u in statistiche]]):
            st.write(["Statistiche 23-24:", f" {df.loc[gioc.capitalize(), [u + " 23_24" for u in statistiche]]}"])

    elif len(gioc.split()) > 1:
        if not all(df.loc[x, [u + " 23_24" for u in statistiche]].isna()):
            st.write(f"Statistiche 23-24: {df.loc[x, [u + " 23_24" for u in statistiche]]}")

with col3:
    st.write("**Stagione 22-23**")
    if len(gioc.split()) == 1:

        if not all(df.loc[gioc.capitalize(), [u + " 22_23" for u in statistiche]]):
            st.write(["Statistiche 22-23:", f" {df.loc[gioc.capitalize(), [u + " 22_23" for u in statistiche]]}"])

    elif len(gioc.split()) > 1:

        if not all(df.loc[x, [u + " 22_23" for u in statistiche]].isna()):
            st.write(f"Statistiche 22-23: {df.loc[x, [u + " 22_23" for u in statistiche]]}")

with col4:
    st.write("**Stagione 21-22**")
    if len(gioc.split()) == 1:

        if not all(df.loc[gioc.capitalize(), statistiche]):
             st.write(["Statistiche 21-22:", f" {df.loc[gioc.capitalize(), statistiche]}"])
    elif len(gioc.split()) > 1:

        if not all(df.loc[x, statistiche].isna()):
            st.write(f"Statistiche 21-22: {df.loc[x, statistiche]}")
