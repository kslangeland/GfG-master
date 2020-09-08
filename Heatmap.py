import pandas
import seaborn
import matplotlib.pyplot as plt

df = pandas.read_csv("results.csv")
print(df)
df = df.pivot("Blue Signal Cost", "Weapon Value", "Prob Blue Signals Given Weapon")
print(df)
hm = seaborn.heatmap(df, annot = True)
plt.savefig("Heatmap.png")