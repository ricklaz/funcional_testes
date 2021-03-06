#Código que faz parte dos teste para a Fucional - escrito por Ricardo Lázaro - 03/09/2020
#Calcula a média de distancia percorrido em viagens feitas por até 2 passageiros

#-*- coding: utf-8 -*-

# Importo as bibliotecas necessárias
import pandas as pd
from datetime import date

# crio variáveis para conter os nomes dos arquivos físicos
csvfull = "2018_Yellow_Taxi_Trip_Data.csv"

# crio um df lendo os dados do arquivo csv
df = pd.read_csv(csvfull, usecols=[0, 1, 2, 3, 4]) 

#converto as colunas de data para o formato padrão
df[['tpep_pickup_datetime','tpep_dropoff_datetime']] = df[['tpep_pickup_datetime','tpep_dropoff_datetime']].apply(pd.to_datetime,format='%m/%d/%Y %H:%M:%S %p')

# filtro o número de passagheiros para ATÉ 2, conforme solicitado no teste
df = df[(df['passenger_count'] <= 2)]

# obtenho o total de viagens deste data frame filtrado
viagens = df['VendorID'].count() #ou print(len(df2))

# calculo a média da distância percorrida pelos táxis
distancia_media = round(df2['trip_distance'].mean(),2)

# exibição dos resultados finais
print("RESULTADOS  DA PESQUISA 1: Foram feitas "+ str(viagens) + " viagens com até 2 passageiros e obtivemos uma média de " + str(distancia_media) + "km percorridos!")
