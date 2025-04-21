
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
        df_concat.to_csv('dados_concatenados.csv', index=False)
        return print('Abaixo estão os 3 Dataframes concatenados:''\n',df_concat,'\n')
    
# Classe com métodos pra formatar as datas, vendas, agrupar por categoria, calcular vendas totais e filtrar vendas superiores a R$10.000,00

class Transformar:

    def formatardata(self, df_concat):
        df_concat = pd.read_csv('dados_concatenados.csv')
        df_concat['Data'] = pd.to_datetime(df_concat['Data'])
        df_concat['Data'] = df_concat['Data'].dt.strftime('%d/%m/%y')
        df_concat['Vendas Formatadas'] = df_concat['Venda'].apply(
        lambda x: f"R${x:,.2f}".replace(',', 'X').replace('.', ',').replace('X', '.')
        )
        df_concat.to_csv('dados_formatados.csv', index=False)
        return print('Abaixo estão os dados com os dados formatados: \n', df_concat, '\n')
    
    def agruparcat(self, df_formatado):
        df_formatado = pd.read_csv('dados_formatados.csv')
        df_agrupado = df_formatado.groupby('Produto')['Quantidade'].sum().reset_index()
        df_agrupado.to_csv('categorias_agrupadas.csv', index=False)
        return print('Abaixo estão os dados agrupados por categoria e suas respectivas quantidades de vendas: \n', df_agrupado, '\n')
    
    def vendastotais(self,agrupar_cat):
        agrupar_cat = pd.read_csv('dados_formatados.csv')
        agrupar_cat['Vendas Totais'] = agrupar_cat['Quantidade'] * agrupar_cat['Venda']
        vendas_totais = agrupar_cat.groupby('Produto')['Vendas Totais'].sum().reset_index()
        vendas_totais.to_csv('vendas_totais.csv', index=False)
        return print('Abaixo estão os valores das vendas totais de cada produto: \n', vendas_totais, '\n')
    
    def vendasup10mil(self,vendas_totais):
        vendas_totais = pd.read_csv('vendas_totais.csv')
        df_filtrado = vendas_totais[vendas_totais['Vendas Totais'] > 10000 ]
        df_filtrado.to_csv('vendasup10mil.csv', index=False)
        return print('Abaixo estão os produtos com vendas acima de 10.000,00: \n', df_filtrado, '\n') 
    
class Decisaosaida:

    def salvarparquet(self,arq_csv):
        df = pd.read_csv(arq_csv)
        df.to_parquet('Dados_parquet.parquet')    
