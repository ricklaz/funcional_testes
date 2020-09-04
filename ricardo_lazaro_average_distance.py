#Código que faz parte dos teste para a Fucional
# Ricardo Lázaro - 03/09/2020

#-*- coding: utf-8 -*-

# Importo as bibliotecas necessárias
import pandas as pd
from datetime import date

# crio variáveis para conter os nomes dos arquivos físicos
csvfull = "2018_Yellow_Taxi_Trip_Data.csv"

# crio um df lendo os dados do arquivo csv filtrando apenas as colunas que preciso 
#df = pd.read_csv(csvfull, usecols=['VendorID', 'trip_distance', 'passenger_count' ]) 
df = pd.read_csv(csvfull, usecols=[0, 1, 2, 3, 4]) 

# filtro o número de passagheiros para ATÉ 2, conforme solicitado no teste
df2 = df[(df['passenger_count'] <= 2)]

# obtenho o total de viagens deste data frame filtrado
viagens = df2['VendorID'].count() #ou rint(len(df2))

# calculo a média da distância percorrida pelos táxis
media = round(df2['trip_distance'].mean(),2)

# exibição dos resultados finais
print("RESULTADOS  DA PESQUISA: Foram feitas "+ str(viagens) + " viagens com até 2 passageiros e obtivemos uma média de " + str(media) + "km percorridos!")

print(date.weekday(date.today()))
#print(date.today())
#print(date.weekday(df["tpep_pickup_datetime"]))
