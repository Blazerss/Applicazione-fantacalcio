import pandas as pd
from bs4 import BeautifulSoup as bs
import requests

df1 = pd.read_excel("C:/Users/bront/OneDrive/Desktop/Quotazioni_Fantacalcio_Stagione_2024_25 (1).xlsx", header=1)
df1=df1.drop(columns=["RM","Qt.A M","Qt.I M","Diff.M","FVM M"])
df2 = pd.read_excel("C:/Users/bront/OneDrive/Desktop/Statistiche_Fantacalcio_Stagione_2023_24 (1).xlsx", header=1)
df2=df2.drop(columns=["R","Rm","Nome","Squadra"])
df3 = pd.read_excel("C:/Users/bront/OneDrive/Desktop/Statistiche_Fantacalcio_Stagione_2022_23.xlsx", header=1)
df3=df3.drop(columns=["R","Rm","Nome","Squadra"])
df4 = pd.read_excel("C:/Users/bront/OneDrive/Desktop/Statistiche_Fantacalcio_Stagione_2021_22.xlsx", header=1)
df4=df4.drop(columns=["R","Rm","Nome","Squadra"])


df5=pd.merge(df1,df2,on="Id",how='left')
df6=pd.merge(df5,df3,on="Id",how='left',suffixes=(" 23_24"," 22_23"))
df7=pd.merge(df6,df4,on="Id",how='left')

df7 = df7.drop(columns="Id")
df1 = pd.read_csv('C:/Users/bront/PycharmProjects/pythonProject/asta1.csv',encoding='latin-1')
df1=df1.drop(columns=['ALG FTP','FM 23-24','FM 22-23' ,'FM 21-22 '])

df8=pd.merge(df7,df1,on="Nome",how='left')

new_cols=[
    "Nome",
    "Squadra",
    "R",
    "attributi",
    "Res. Inf."]

df8=df8.reindex(columns= new_cols + list(df8.columns.difference(new_cols, sort=False)))
df8=df8.drop_duplicates(subset=["Nome"])


df8.to_excel('C:/Users/bront/OneDrive/Desktop/fanta.xlsx', index=False )
