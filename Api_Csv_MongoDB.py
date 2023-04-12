from pymongo import MongoClient
import pandas as pd

client = MongoClient("localhost", 27017)
#Testando se o localhost está conectado.
print(client.list_database_names())

df = pd.read_csv("../Bases/Base_att/Estabelecimento_att.csv", encoding='utf-8')
#Confirmação se conseguiu fazer a leitura do csv.
print(df.head(3))

data = df.to_dict(orient="records")
#Print para confimar a operação do dataframe.
print(data)

#Criando o bando de dados do diretorio.
db = client["Estabelecimentos"]
db.Estabelecimento.insert_many(data)

#Confirmação do armazenamento no mongoDB.
print(db)