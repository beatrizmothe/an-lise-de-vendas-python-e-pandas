import pandas as pd 

df_vendas = pd.read_csv("clientes_dataset.csv")

print(df_vendas.head())

print("Shape:", df_vendas.shape) #Total de linhas e colunas

df_vendas["receita"] = df_vendas["quantidade"] * df_vendas["preco_unitario"] #Calculo da receita
print(df_vendas["receita"])

categoria_eletronicos = df_vendas[df_vendas["categoria"] == "Eletrônicos"] #Filtra categoria eletronicos
print(categoria_eletronicos)

produto_mais_vendido = (
    df_vendas.groupby("produto")["quantidade"] #Produto mais vendido
    .sum()
    .sort_values(ascending=False)
    .head(1)
)
print(produto_mais_vendido.index[0])


regiao_maior_receita = (
    df_vendas.groupby("regiao")["receita"] #Região com maior receita
    .sum()
    .sort_values(ascending=False)
    .head(1)
)
print(regiao_maior_receita)

df_vendas.to_excel("vendas_processado.xlsx", index=False) #Salva o arquivo em excel
