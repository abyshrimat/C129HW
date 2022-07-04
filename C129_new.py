import csv
import pandas as pd

df = pd.read_csv("dwarf_star.csv")

df = df[df['Mass'].notna()]

df = df[df['Radius'].notna()]
#print(df.dtypes)

df["Radius"] =  0.102763 * df["Radius"]
df["Mass"] =  0.000954588 * df["Mass"]

#print(df.head(10))

df.to_csv('dwarf_star_new.csv', index = False)

