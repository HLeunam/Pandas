# Criando um DataFrame passando um dicionário de
# objetos onde as chaves são os rótulos das colunas e os
# valores são os valores das colunas.
import pandas as pd
import numpy as np

# Gerar DataFrame apartir de dicionário.
df2 = pd.DataFrame(
    {
        "A": 1.0,
        "B": pd.Timestamp("20130102"),
        "C": pd.Series(1, index=list(range(4)), dtype="int32"),
        "D": np.array([3] * 4, dtype="int32"),
        "E": pd.Categorical(["test", "train", "test", "train"]),
        "F": "foo",
    }
)

print(df2)

# Descobrir o tipo de dados do DF.
print(df2.dtypes)
print(df2.boxplot)

# Visualizando Dados.

# Método DataFrame.head().
print("Os primeiros dois registros sao:")
print(df2.head(2))

# Método DataFrame.tail().
print("Os dois ultimos registros sao:")
print(df2.tail(2))