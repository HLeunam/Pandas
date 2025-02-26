#P030 Gráfico de uma função.
import pandas as pd

df = pd.DataFrame({"x": list(range(1, 11))})
df["y"] = (df["x"] ** 2) + 3
lines = df.plot.line(x="x", y="y", legend=False,)