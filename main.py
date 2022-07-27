import pandas as pd
import plotly.express as px
import kaleido


# Passo 1 - Importar e visualizar a base de dados:
tabela = pd.read_csv(r'telecom_users.csv')

# Passo 2 - Tratar a base de dados:

# Tirando as colunas inúteis. Axis: 1=coluna 0=linha
tabela = tabela.drop(["Unnamed: 0", "IDCliente"], axis=1)

# Corrigir o tipo da informação - ajustar o TotalGasto de texto para numérico
tabela["TotalGasto"] = pd.to_numeric(tabela["TotalGasto"], errors="coerce")

# Retirar colunas com TODAS informação vazias
tabela = tabela.dropna(how="all", axis=1)  # Axis: 1=coluna 0=linha

# Retirar linhas com alguma informação vazia
tabela = tabela.dropna(how="any", axis=0)  # Axis: 1=coluna 0=linha

# print(tabela.info())


# Passo 3 - Análise inicial dos dados

print(tabela["Churn"].value_counts())  # qtd. de cancelamentos
print(tabela["Churn"].value_counts(normalize=True))  # % de cancelamentos
print(tabela["Churn"].value_counts(normalize=True).map("{:.2%}".format))  # % de cancelamentos formatado

# Passo 4 - Descobrir os motivos de cancelamento
# https://plotly.com/python/

print(tabela.columns)

for coluna in tabela.columns:
    grafico = px.histogram(tabela, x=coluna, color="Churn", text_auto=True)
    grafico.write_image(f"graphs/{coluna}.png")  # Salva os gráficos em .png
    grafico.write_image(f"graphs/{coluna}.html")  # Salva os gráficos em .html
    #grafico.show()

# Passo 4 - Conclusões

conclusao = """

1- Clientes novos estão cancelando muito.
 - Pode ser alguma promoção inicial que termina logo em seguida.
 - Primeira experiência do serviço está ruim.

2- Boleto eletrônico tem muito mais cancelamento.
 - Oferecer desconto pagando de outras formas.
 
3- Clientes com contrato mensal, cancelam muito mais.
 - Oferecer desconto para plano anual.
 
4- Clientes com menos serviços, cancelam muito mais. 
 - Oferecer serviços extras para manter o cliente.
 
5- Clientes com família maior, cancelam menos.
 - Oferecer uma segunda linha com desconto/free.
 
"""

print(conclusao)





