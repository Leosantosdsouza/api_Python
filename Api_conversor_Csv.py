import pymongo
import pandas as pd

client = pymongo.MongoClient("localhost",27017)

#Testando o localhost se esta conectado, junto com a lista de DataBases.
print(client.list_database_names())

df = pd.read_csv("../Bases/Base_atual/K3241.K03200Y9.D30211.ESTABELE", delimiter=";", encoding="ISO-8859-1", header= None, low_memory=False)
#Confirmando se completou a operação de pegar o csv.
print(df.head(2))

df.columns = ['CNPJ BÁSICO',
              'CNPJ ORDEM',
              'CNPJ DV',
              'IDENTIFICADOR MATRIZ/FILIAL',
              'NOME FANTASIA',
              'SITUAÇÃO CADASTRAL',
              'DATA SITUAÇÃO CADASTRAL',
              'MOTIVO SITUAÇÃO CADASTRAL',
              'NOME DA CIDADE NO EXTERIOR',
              'PAIS',
              'DATA DE INÍCIO ATIVIDADE',
              'CNAE FISCAL PRINCIPAL',
              'CNAE FISCAL SECUNDÁRIA',
              'TIPO DE LOGRADOURO',
              'LOGRADOURO',
              'NÚMERO',
              'COMPLEMENTO',
              'BAIRRO',
              'CEP',
              'UF',
              'MUNICÍPIO',
              'DDD 1',
              'TELEFONE 1',
              'DDD 2',
              'TELEFONE 2',
              'DDD DO FAX',
              'FAX',
              'CORREIO ELETRÔNICO',
              'SITUAÇÃO ESPECIAL',
              'DATA DA SITUAÇÃO ESPECIAL']

#Confirmando se fez a conversão do Indice
print(df.head(2))

df2 = df.filter(items=['CNPJ BÁSICO', 'CNPJ ORDEM', 'CNPJ DV', 'NOME FANTASIA', 'CEP', 'DDD 1', 'TELEFONE 1', 'CORREIO ELETRÔNICO']).head(10)
#Confirmação que conseguiu pegar apenas os filtros listados junto com a quantidade necessaria de cadastros.
print(df2.head(10))

#Convertendo para um Csv, com os filtros pego.
df2.to_csv('Estabelecimento_att.csv')
