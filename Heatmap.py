import pandas
import seaborn
import matplotlib.pyplot as plt

df = pandas.read_csv("results.csv")
print(df)
df = df.pivot("Blue Signal Cost", "Weapon Value", "Prob Red Accepts Given Blue Signals")
print(df)
hm = seaborn.heatmap(df, annot = True)
plt.savefig("Heatmap_RedBehavior.png")

df=df.pivot("Blue Signal Cost", "Weapon Value", "Prob Blue with Weapon Bluffs")
print(df)
hm = seaborn.heatmap(df, annot = True)
plt.savefig("Heatmap_BlueBehavior.png")
plt.savefig("Heatmap_BlueBehavior2.png")
