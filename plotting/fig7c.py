import pandas as pd,matplotlib.pyplot as plt
df=pd.read_csv("data/metrics.csv")
x=range(1,len(df)+1)
y=df["flat_ms"]
plt.figure()
plt.bar(x,y) if "flat_ms" in ["mean_ms"] else plt.plot(x,y,marker="o")
plt.title("Fig 7c")
plt.ylabel("Flatness P90-P10 (ms)")
plt.xlabel("run")
plt.savefig("plotting/fig7c.png",bbox_inches="tight")
