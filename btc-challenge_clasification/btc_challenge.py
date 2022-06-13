import csv, json
from tabulate import  tabulate
import pandas as pd
import os

def behaviour(df):
    verictn= df['Close']- df['Open']
    if verictn<0:
        return 'BAJA'
    elif verictn>0:
        return 'SUBE'
    else:
        return 'ESTABLE'


file_object= "./JandJ.csv"
df= pd.read_csv(file_object)
df_2= df.copy()
df_2=df_2.drop(['Date','Open','High','Low','Close','Adj Close','Volume'], axis = 1)
df_2['Fecha analizada']=df["Date"]
df_2["Comportamiento de la acción"]=df.apply(behaviour,axis=1)
df_2["abs Diferencia Close-Open"]=abs(df['Close']-df['Open'])
#df_2=df_2.set_index('Fecha Analizada')
df_2.to_csv('./analisis_archivo.csv', sep='\t', index=False)
my_dict={}

cot=df.loc[df['Volume'] == df['Volume'].min()]
cot_2=df.loc[df['Volume'] == df['Volume'].max()]
cot_3 =df_2.loc[df_2['abs Diferencia Close-Open']==df_2['abs Diferencia Close-Open'].max()]

my_dict['date_lowest_volume']= str(cot['Date'].values[0])
my_dict['lowest_volume']= int(df['Volume'].min())
my_dict['date_highest_volume']= str(cot_2['Date'].values[0])
my_dict['highest_volume']= int(df['Volume'].max())
my_dict['mean_volume']= float(df['Volume'].mean())
my_dict['date_greatest_difference']= str(cot_3['Fecha analizada'].values[0])
my_dict['greatest_difference']= float(df_2['abs Diferencia Close-Open'].max())


# for index, row in df.iterrows():
#  if row['Volume']==df['Volume'].min():
#     date=df['Date'] 

# Escribe los datos en un archivo JSON:
with open('detalles.json', 'w') as f:
    json.dump(my_dict,f)

# print(df_2.head(10))
# print('\n',date)