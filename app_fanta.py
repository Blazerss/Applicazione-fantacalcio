import streamlit as st
import pandas as pd
from streamlit_tags import st_tags
url= "https://raw.githubusercontent.com/Blazerss/Applicazione-fantacalcio/main/fanta.csv"
df = pd.read_csv(url)
st.title('Fanta')
keywords = st_tags(label='# Inserisci giocatore:', text='Press enter to add more', value="", suggestions=df["Nome"].tolist())

statistiche = ["Pv", "Mv", "Fm", "Gf", "Gs", "Rp", "Rc", "R+", "R-", "Ass", "Amm", "Esp", "Au"]
gioc = " ".join(keywords)
print(gioc)
df.set_index("Nome",inplace=True)
col1,col2,col3,col4,col5=st.columns(5,gap="medium")
with col1:
   if gioc:
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
    if gioc:
        st.write("**Stagione 24-25**")
    if len(gioc.split()) == 1:
        if not all(df.loc[gioc.capitalize(), [u + " 24_25" for u in statistiche]]):
            st.write(f" Partite Giocate: {int(df.loc[gioc.capitalize(), [u + " 24_25" for u in statistiche]][0])}")
            st.write(f" Media Voto: {df.loc[gioc.capitalize(), [u + " 24_25" for u in statistiche]][1]}")
            st.write(f" Fanta Media : {df.loc[gioc.capitalize(), [u + " 24_25" for u in statistiche]][2]}")
            if df.loc[gioc.capitalize(), "R"] != "P":
                st.write(f" Goal Fatti: {int(df.loc[gioc.capitalize(), [u + " 24_25" for u in statistiche]][3])}")
            if df.loc[gioc.capitalize(), "R"] == "P":
                st.write(f" Goal Subiti: {int(df.loc[gioc.capitalize(), [u + " 24_25" for u in statistiche]][4])}")
            if df.loc[gioc.capitalize(), "R"] == "P":
                st.write(f" Rigori Parati: {int(df.loc[gioc.capitalize(), [u + " 24_25" for u in statistiche]][5])}")
            if df.loc[gioc.capitalize(), "R"] != "P":
                st.write(f" Rigori Calciati: {int(df.loc[gioc.capitalize(), [u + " 24_25" for u in statistiche]][6])}")
            if df.loc[gioc.capitalize(), "R"] != "P":
                st.write(f" Rigori Segnati: {int(df.loc[gioc.capitalize(), [u + " 24_25" for u in statistiche]][7])}")
            if df.loc[gioc.capitalize(), "R"] != "P":
                st.write(f" Rigori Sbagliati: {int(df.loc[gioc.capitalize(), [u + " 24_25" for u in statistiche]][8])}")
            if df.loc[gioc.capitalize(), "R"] != "P":
                st.write(f" Assist: {int(df.loc[gioc.capitalize(), [u + " 24_25" for u in statistiche]][9])}")
            st.write(f" Ammunizioni: {int(df.loc[gioc.capitalize(), [u + " 24_25" for u in statistiche]][10])}")
            st.write(f" Espulsioni: {int(df.loc[gioc.capitalize(), [u + " 24_25" for u in statistiche]][11])}")
            st.write(f" Autogol: {int(df.loc[gioc.capitalize(), [u + " 24_25" for u in statistiche]][12])}")
    elif len(gioc.split()) > 1:
            y = [u.capitalize() for u in gioc.split()]
            x = " ".join(y)
            if not all(df.loc[x, [u + " 24_25" for u in statistiche]].isna()):
                st.write(f" Partite Giocate: {int(df.loc[x, [u + " 24_25" for u in statistiche]][0])}")
                st.write(f" Media Voto: {df.loc[x, [u + " 24_25" for u in statistiche]][1]}")
                st.write(f" Fanta Media : {df.loc[x, [u + " 24_25" for u in statistiche]][2]}")
                if df.loc[x, "R"] != "P":
                    st.write(f" Goal Fatti: {int(df.loc[x, [u + " 24_25" for u in statistiche]][3])}")
                if df.loc[x, "R"] == "P":
                    st.write(f" Goal Subiti: {int(df.loc[x, [u + " 24_25" for u in statistiche]][4])}")
                if df.loc[x, "R"] == "P":
                    st.write(f" Rigori Parati: {int(df.loc[x, [u + " 24_25" for u in statistiche]][5])}")
                if df.loc[x, "R"] != "P":
                    st.write(f" Rigori Calciati: {int(df.loc[x, [u + " 24_25" for u in statistiche]][6])}")
                if df.loc[x, "R"] != "P":
                    st.write(f" Rigori Segnati: {int(df.loc[x, [u + " 24_25" for u in statistiche]][7])}")
                if df.loc[x, "R"] != "P":
                    st.write(f" Rigori Sbagliati: {int(df.loc[x, [u + " 24_25" for u in statistiche]][8])}")
                if df.loc[x, "R"] != "P":
                    st.write(f" Assist: {int(df.loc[x, [u + " 24_25" for u in statistiche]][9])}")
                st.write(f" Ammunizioni: {int(df.loc[x, [u + " 24_25" for u in statistiche]][10])}")
                st.write(f" Espulsioni: {int(df.loc[x, [u + " 24_25" for u in statistiche]][11])}")
                st.write(f" Autogol: {int(df.loc[x, [u + " 24_25" for u in statistiche]][12])}")



with col3:
    if gioc:
       st.write("**Stagione 23-24**")
    if len(gioc.split()) == 1:
        if not all(df.loc[gioc.capitalize(), [u + " 23_24" for u in statistiche]]):
            st.write(f" Partite Giocate: {int(df.loc[gioc.capitalize(), [u + " 23_24" for u in statistiche]][0])}")
            st.write(f" Media Voto: {df.loc[gioc.capitalize(), [u + " 23_24" for u in statistiche]][1]}")
            st.write(f" Fanta Media : {df.loc[gioc.capitalize(), [u + " 23_24" for u in statistiche]][2]}")
            if df.loc[gioc.capitalize(), "R"] != "P":
                st.write(f" Goal Fatti: {int(df.loc[gioc.capitalize(), [u + " 23_24" for u in statistiche]][3])}")
            if df.loc[gioc.capitalize(), "R"] == "P":
                st.write(f" Goal Subiti: {int(df.loc[gioc.capitalize(), [u + " 23_24" for u in statistiche]][4])}")
            if df.loc[gioc.capitalize(), "R"] == "P":
                st.write(f" Rigori Parati: {int(df.loc[gioc.capitalize(), [u + " 23_24" for u in statistiche]][5])}")
            if df.loc[gioc.capitalize(), "R"] != "P":
                st.write(f" Rigori Calciati: {int(df.loc[gioc.capitalize(), [u + " 23_24" for u in statistiche]][6])}")
            if df.loc[gioc.capitalize(), "R"] != "P":
                st.write(f" Rigori Segnati: {int(df.loc[gioc.capitalize(), [u + " 23_24" for u in statistiche]][7])}")
            if df.loc[gioc.capitalize(), "R"] != "P":
                st.write(f" Rigori Sbagliati: {int(df.loc[gioc.capitalize(), [u + " 23_24" for u in statistiche]][8])}")
            if df.loc[gioc.capitalize(), "R"] != "P":
                st.write(f" Assist: {int(df.loc[gioc.capitalize(), [u + " 23_24" for u in statistiche]][9])}")
            st.write(f" Ammunizioni: {int(df.loc[gioc.capitalize(), [u + " 23_24" for u in statistiche]][10])}")
            st.write(f" Espulsioni: {int(df.loc[gioc.capitalize(), [u + " 23_24" for u in statistiche]][11])}")
            st.write(f" Autogol: {int(df.loc[gioc.capitalize(), [u + " 23_24" for u in statistiche]][12])}")

    elif len(gioc.split()) > 1:
        y = [u.capitalize() for u in gioc.split()]
        x = " ".join(y)
        if not all(df.loc[x, [u + " 23_24" for u in statistiche]].isna()):
            st.write(f" Partite Giocate: {int(df.loc[x, [u + " 23_24" for u in statistiche]][0])}")
            st.write(f" Media Voto: {df.loc[x, [u + " 23_24" for u in statistiche]][1]}")
            st.write(f" Fanta Media : {df.loc[x, [u + " 23_24" for u in statistiche]][2]}")
            if df.loc[x, "R"] != "P":
                st.write(f" Goal Fatti: {int(df.loc[x, [u + " 23_24" for u in statistiche]][3])}")
            if df.loc[x, "R"] == "P":
                st.write(f" Goal Subiti: {int(df.loc[x, [u + " 23_24" for u in statistiche]][4])}")
            if df.loc[x, "R"] == "P":
                st.write(f" Rigori Parati: {int(df.loc[x, [u + " 23_24" for u in statistiche]][5])}")
            if df.loc[x, "R"] != "P":
                st.write(f" Rigori Calciati: {int(df.loc[x, [u + " 23_24" for u in statistiche]][6])}")
            if df.loc[x, "R"] != "P":
                st.write(f" Rigori Segnati: {int(df.loc[x, [u + " 23_24" for u in statistiche]][7])}")
            if df.loc[x, "R"] != "P":
                st.write(f" Rigori Sbagliati: {int(df.loc[x, [u + " 23_24" for u in statistiche]][8])}")
            if df.loc[x, "R"] != "P":
                st.write(f" Assist: {int(df.loc[x, [u + " 23_24" for u in statistiche]][9])}")
            st.write(f" Ammunizioni: {int(df.loc[x, [u + " 23_24" for u in statistiche]][10])}")
            st.write(f" Espulsioni: {int(df.loc[x, [u + " 23_24" for u in statistiche]][11])}")
            st.write(f" Autogol: {int(df.loc[x, [u + " 23_24" for u in statistiche]][12])}")

with col4:
    if gioc:
        st.write("**Stagione 22-23**")
    if len(gioc.split()) == 1:

        if not all(df.loc[gioc.capitalize(), [u + " 22_23" for u in statistiche]]):
            st.write(f" Partite Giocate: {int(df.loc[gioc.capitalize(), [u + " 22_23" for u in statistiche]][0])}")
            st.write(f" Media Voto: {df.loc[gioc.capitalize(), [u + " 22_23" for u in statistiche]][1]}")
            st.write(f" Fanta Media : {df.loc[gioc.capitalize(), [u + " 22_23" for u in statistiche]][2]}")
            if df.loc[gioc.capitalize(), "R"] != "P":
                st.write(f" Goal Fatti: {int(df.loc[gioc.capitalize(), [u + " 22_23" for u in statistiche]][3])}")
            if df.loc[gioc.capitalize(), "R"] == "P":
                st.write(f" Goal Subiti: {int(df.loc[gioc.capitalize(), [u + " 22_23" for u in statistiche]][4])}")
            if df.loc[gioc.capitalize(), "R"] == "P":
                st.write(f" Rigori Parati: {int(df.loc[gioc.capitalize(), [u + " 22_23" for u in statistiche]][5])}")
            if df.loc[gioc.capitalize(), "R"] != "P":
                st.write(f" Rigori Calciati: {int(df.loc[gioc.capitalize(), [u + " 22_23" for u in statistiche]][6])}")
            if df.loc[gioc.capitalize(), "R"] != "P":
                st.write(f" Rigori Segnati: {int(df.loc[gioc.capitalize(), [u + " 22_23" for u in statistiche]][7])}")
            if df.loc[gioc.capitalize(), "R"] != "P":
                st.write(f" Rigori Sbagliati: {int(df.loc[gioc.capitalize(), [u + " 22_23" for u in statistiche]][8])}")
            if df.loc[gioc.capitalize(), "R"] != "P":
                st.write(f" Assist: {int(df.loc[gioc.capitalize(), [u + " 22_23" for u in statistiche]][9])}")
            st.write(f" Ammunizioni: {int(df.loc[gioc.capitalize(), [u + " 22_23" for u in statistiche]][10])}")
            st.write(f" Espulsioni: {int(df.loc[gioc.capitalize(), [u + " 22_23" for u in statistiche]][11])}")
            st.write(f" Autogol: {int(df.loc[gioc.capitalize(), [u + " 22_23" for u in statistiche]][12])}")

    elif len(gioc.split()) > 1:
        y = [u.capitalize() for u in gioc.split()]
        x = " ".join(y)

        if not all(df.loc[x, [u + " 22_23" for u in statistiche]].isna()):
            st.write(f" Partite Giocate: {int(df.loc[x, [u + " 22_23" for u in statistiche]][0])}")
            st.write(f" Media Voto: {df.loc[x, [u + " 22_23" for u in statistiche]][1]}")
            st.write(f" Fanta Media : {df.loc[x, [u + " 22_23" for u in statistiche]][2]}")
            if df.loc[x,"R"] != "P":
               st.write(f" Goal Fatti: {int(df.loc[x, [u + " 22_23" for u in statistiche]][3])}")


               st.write(f" Rigori Calciati: {int(df.loc[x, [u + " 22_23" for u in statistiche]][6])}")

               st.write(f" Rigori Segnati: {int(df.loc[x, [u + " 22_23" for u in statistiche]][7])}")

               st.write(f" Rigori Sbagliati: {int(df.loc[x, [u + " 22_23" for u in statistiche]][8])}")

               st.write(f" Assist: {int(df.loc[x, [u + " 22_23" for u in statistiche]][9])}")
            if df.loc[x,"R"] == "P":
               st.write(f" Goal Subiti: {int(df.loc[x, [u + " 22_23" for u in statistiche]][4])}")

               st.write(f" Rigori Parati: {int(df.loc[x, [u + " 22_23" for u in statistiche]][5])}")

            st.write(f" Ammunizioni: {int(df.loc[x, [u + " 22_23" for u in statistiche]][10])}")
            st.write(f" Espulsioni: {int(df.loc[x, [u + " 22_23" for u in statistiche]][11])}")
            st.write(f" Autogol: {int(df.loc[x, [u + " 22_23" for u in statistiche]][12])}")


with col5:
    if gioc:
       st.write("**Stagione 21-22**")
    if len(gioc.split()) == 1:

        if not all(df.loc[gioc.capitalize(), statistiche]):
            st.write(f" Partite Giocate: {int(df.loc[gioc.capitalize(), statistiche][0])}")
            st.write(f" Media Voto: {df.loc[gioc.capitalize(),  statistiche][1]}")
            st.write(f" Fanta Media : {df.loc[gioc.capitalize(),  statistiche][2]}")
            if df.loc[gioc.capitalize(), "R"] != "P":
                st.write(f" Goal Fatti: {int(df.loc[gioc.capitalize(), statistiche][3])}")
            if df.loc[gioc.capitalize(), "R"] == "P":
                st.write(f" Goal Subiti: {int(df.loc[gioc.capitalize(),  statistiche][4])}")
            if df.loc[gioc.capitalize(), "R"] == "P":
                st.write(f" Rigori Parati: {int(df.loc[gioc.capitalize(),  statistiche][5])}")
            if df.loc[gioc.capitalize(), "R"] != "P":
                st.write(f" Rigori Calciati: {int(df.loc[gioc.capitalize(),  statistiche][6])}")
            if df.loc[gioc.capitalize(), "R"] != "P":
                st.write(f" Rigori Segnati: {int(df.loc[gioc.capitalize(),  statistiche][7])}")
            if df.loc[gioc.capitalize(), "R"] != "P":
                st.write(f" Rigori Sbagliati: {int(df.loc[gioc.capitalize(),  statistiche][8])}")
            if df.loc[gioc.capitalize(), "R"] != "P":
                st.write(f" Assist: {int(df.loc[gioc.capitalize(),  statistiche][9])}")
            st.write(f" Ammunizioni: {int(df.loc[gioc.capitalize(),  statistiche][10])}")
            st.write(f" Espulsioni: {int(df.loc[gioc.capitalize(), statistiche][11])}")
            st.write(f" Autogol: {int(df.loc[gioc.capitalize(), statistiche][12])}")

    elif len(gioc.split()) > 1:
        y = [u.capitalize() for u in gioc.split()]
        x = " ".join(y)

        if not all(df.loc[x, statistiche].isna()):
            st.write(f" Partite Giocate: {int(df.loc[x, statistiche][0])}")
            st.write(f" Media Voto: {df.loc[x, statistiche][1]}")
            st.write(f" Fanta Media : {df.loc[x,  statistiche][2]}")
            if df.loc[x, "R"] != "P":
                st.write(f" Goal Fatti: {int(df.loc[x, statistiche][3])}")
            if df.loc[x, "R"] == "P":
                st.write(f" Goal Subiti: {int(df.loc[x, statistiche][4])}")
            if df.loc[x, "R"] == "P":
                st.write(f" Rigori Parati: {int(df.loc[x, statistiche][5])}")
            if df.loc[x, "R"] != "P":
                st.write(f" Rigori Calciati: {int(df.loc[x, statistiche][6])}")
            if df.loc[x, "R"] != "P":
                st.write(f" Rigori Segnati: {int(df.loc[x, statistiche][7])}")
            if df.loc[x, "R"] != "P":
                st.write(f" Rigori Sbagliati: {int(df.loc[x, statistiche][8])}")
            if df.loc[x, "R"] != "P":
                st.write(f" Assist: {int(df.loc[x, statistiche][9])}")
            st.write(f" Ammunizioni: {int(df.loc[x, statistiche][10])}")
            st.write(f" Espulsioni: {int(df.loc[x, statistiche][11])}")
            st.write(f" Autogol: {int(df.loc[x, statistiche][12])}")


col1,col2=st.columns(2)

with col1:

   squadra = st_tags(label="Squadra", text='Press enter to add more', suggestions=df.index.tolist())
with col2:
    crediti = st_tags(label="Crediti", text='Press enter to add more')

x=0
df1 = pd.DataFrame(columns=["Rosa","Squadra","Costo","Crediti Rimasti"])
rosa=[]
for i in squadra:
    if len(i.split()) == 1:
        rosa.append( i.capitalize())
    else:
        y = [u.capitalize() for u in i.split()]
        rosa.append( " ".join(y))


for i in range(len(rosa)):
    d = {"Rosa":rosa[i],"Squadra":df.loc[rosa[i],"Squadra"],"Costo":int(crediti[i]),"Crediti Rimasti" : 500 - x - int(crediti[i])}

    df1 = df1._append(d,ignore_index=True)
    x += int(crediti[i])
df1.set_index("Rosa",inplace=True)
if not df1.empty:
   table= st.table(df1)


