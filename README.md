#### Pipeline ETL que lê os dados, transforma e converte para .JSON para CSV e/ou PARQUET

Objetivo: Desenvolver uma pipeline ETL que leia arquivos .JSON, transforma para Dataframe, concatena os Dataframes, 
transforma os dados pra CSV ou PARQUET.

Abaixo temos um fluxograma pra demonstrar as etapas de execução da pipeline:

<div align="center"> <h4>Fluxograma<h4> </div>

<div align="center"> 
<img src="fluxograma.png" alt="Fluxograma">
</div>

 **Tarefas**:

1. Ler os arquivos .JSON e carregar os dados.
2. Transformar pra Dataframe e concatenar todos os arquivos.
3. Transformar os dados
4. Decidir se vai ser salvo em CSV ou em Parquet.

**Divisão das terafas do projeto**

1. **Criar uma classe com métodos que:**:
    
* Leia os arquivos. `.lerarquivos`
* Transforme para DataFrame.`.transformardf`
* Concatena os Dataframes.`.concatenardf`
* Transformar os dados:
1. Agrupar por categoria. `.agruparcat`
2. Somar vendas totais de cada produto. `.vendastotais`
3. Filtrar vendas acima de R$ 10.000,00 `.vendasup10mil`
* Converter pra CSV. `.convertercsv`
* Converter pra Parquet. `.converterparquet`
* Salvar em CSV. `.salvarcsv`
* Salvar em Parquet. `.salvarparquet`
