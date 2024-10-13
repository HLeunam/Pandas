# Criando um DataFrame passando um índice datetime usando date_range().
import pandas as pd
import numpy as np

# Gerar index com datas entre 01/01/2013 até 06/01/2013.
dates = pd.date_range("20130101", periods=6)
print(dates)

# Gerar DataFrame.
df = pd.DataFrame(np.random.randn(6,4), index=dates, columns=list("ABCD"))
print(df)

