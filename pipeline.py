import classes as cls

# Métodos da classe Tratamentojson pra ler os arquivos .JSON, transformar pra Dataframe e concatenar os 3 DF's.

tratamento_json = cls.Tratamentojson()
tratamento_json.lerarquivos('coleta_dia01.json')
tratamento_json.transformardf('coleta_dia01.json')
df_concat = tratamento_json.concatenardfs ('coleta_dia01.json', 'coleta_dia02.json', 'coleta_dia02.json')

# Métodos da classe Transformarjson pra formatar os dados, agrupar por categoria, calcular vendas totais e filtrar vendas acima de R$ 10.000,00.

transformacao_json = cls.Transformarjson()
transformacao_json.formatardata(df_concat)
transformacao_json.agruparcat(df_concat)
transformacao_json.vendastotais(df_concat)
transformacao_json.vendasup10mil(df_concat)

decisao_saida = cls.Decisaosaida()
decisao_saida.saidacsv('dados_concatenados.csv')