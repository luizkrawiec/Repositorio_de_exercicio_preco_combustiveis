import pandas as pd

# Substitua 'seuarquivo.csv' pelo caminho do seu arquivo CSV
gasolina = 'gasolina.csv'

# Use a função read_csv para ler o arquivo CSV e criar um DataFrame
gasolina_df = pd.read_csv(gasolina)

# Agora você tem seu DataFrame pronto para ser usado
print(gasolina_df)

import seaborn as sns
import matplotlib.pyplot as plt

# Crie o gráfico de linhas
sns.set(style="whitegrid")  # Define o estilo do gráfico
plt.figure(figsize=(10, 5))  # Define o tamanho da figura

# Plote o gráfico de linhas
sns.lineplot(x="dia", y="venda", data=gasolina_df, marker="o", color="b", linestyle="-")

# Adicione rótulos e título ao gráfico
plt.xlabel("Dia")
plt.ylabel("Venda")
plt.title("Vendas de Gasolina ao longo dos Dias")

# Exiba o gráfico
plt.show()

#exportando o  gráfico
plt.savefig("grafico_gasolina.png")
