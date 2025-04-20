
import pandas as pd
import json

# Classe com métodos pra ler os arquivos .JSON, tranformar pra Dataframe e concatenar os três DF's.

class Tratamentojson:

    def lerarquivos(self,ler_json):
        with open(ler_json, 'r', encoding='utf-8') as l:
            carrega_json = json.load(l)   
        return print('Abaixo está o arquivo lido:''\n',json.dumps(carrega_json, indent=4, ensure_ascii=False),'\n')
  
    def transformardf(self,transformar_json):
        self.transformar_json = transformar_json
        df = pd.read_json(transformar_json)  
        return print('Abaixo está o arquivo convertido de .JSON para Dataframe:''\n',df,'\n') 
    
    def concatenardfs (self, df1, df2, df3):
        self.df1 = pd.read_json(df1)
        self.df2 = pd.read_json(df2)
        self.df3 = pd.read_json(df3)

        df_concat = pd.concat([self.df1, self.df2, self.df3], ignore_index=True)
        return print('Abaixo estão os 3 Dataframes concatenados:''\n',df_concat,'\n')
