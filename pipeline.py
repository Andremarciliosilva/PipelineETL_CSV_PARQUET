import classes as cls

# Aramazenamento dos três arquivos .JSON em variáveis pra facilitar o manuseio.

json1 = 'coleta_dia01.json'
json2 = 'coleta_dia02.json'
json3 = 'coleta_dia03.json'

# Métodos da classe pra ler os arquivos .JSON, transformar pra Dataframe e concatenar os 3 DF's.

tratamento_json = cls.Tratamentojson()
tratamento_json.lerarquivos('coleta_dia01.json')
tratamento_json.transformardf('coleta_dia03.json')
tratamento_json.concatenardfs (json1, json2, json3)
