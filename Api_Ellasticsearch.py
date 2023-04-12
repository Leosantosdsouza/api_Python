from elasticsearch import Elasticsearch
import pandas as pd

df = pd.read_csv('../Bases/Base_att/Estabelecimento_att.csv')
#Confirmando se puxou o Csv.
print(df.head(10))


es = Elasticsearch(['http://localhost:9200'])
index_name = 'estabelecimentos'

#Criando Indices para armazenamento dos dados.
if not es.indices.exists(index=index_name):
    es.indices.create(index=index_name)

documents = df.to_dict(orient='records')

#Adicionando o documento para a base.
for doc in documents:
    es.index(index=index_name, body=doc, ignore=[400, 404])

#Confirando a operação, com todas as bases.
query = {"query": {"match_all": {}}}
results = es.search(index=index_name, body=query)
hits = results['hits']['hits']

for hit in hits:
    print(hit['_source'])

"""
es = Elasticsearch(['http://localhost:9200'])

index_name = 'estabelecimento'

es.indices.delete(index=index_name, ignore=[400, 404])"""