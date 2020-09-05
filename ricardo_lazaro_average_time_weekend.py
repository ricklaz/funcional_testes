#Código que faz parte dos teste para a Fucional - escrito por Ricardo Lázaro - 03/09/2020
#Calcula a média de tempo percorrido em viagens feitas nos fins de semana (sábados e domingos)


#-*- coding: utf-8 -*-

# Importo as bibliotecas necessárias
import pandas as pd
from datetime import * #datetime, date, timedelta
from string import Template

# crio variáveis para conter os nomes dos arquivos físicos
csvfull = "2018_Yellow_Taxi_Trip_Data.csv" 

#Leio o arquivo fisico e carreo no dataframe
df = pd.read_csv(csvfull, usecols=[0, 1, 2, 3, 4]) 

#converto as colunas de data para o formato padrão
df[['tpep_pickup_datetime','tpep_dropoff_datetime']] = df[['tpep_pickup_datetime','tpep_dropoff_datetime']].apply(pd.to_datetime,format='%m/%d/%Y %H:%M:%S %p')

#crio colunas adicionais no df - dia_semana e tempo_decorrido (em minutos)
df['dia_semana'] = df['tpep_pickup_datetime'].dt.dayofweek
df['tempo_decorrido'] = round(((df['tpep_dropoff_datetime'] - df['tpep_pickup_datetime']).astype('timedelta64[s]')/60),2)

# filtro as viagens só de sábados e domingos (6 e 7 respectivamente) 
fds = [6,7]
df = df[df['dia_semana'].isin(fds)]

#obtenho o tatal de registros filtrados, ou seja, as viagens feitas entre sábado e domingo
viagens = df['VendorID'].count() #ou len(df)

#obtenho a média em minutos da coluna tempo percorrido
tempo_medio = round((df["tempo_decorrido"].mean()),2)

# exibição dos resultados finais
print("RESULTADOS  DA PESQUISA 2: Foram feitas "+ str(viagens) + " viagens durante os fins de semana(sábados e domingos) e obtivemos uma média de " + str(tempo_medio) + " minutos por viagem!")