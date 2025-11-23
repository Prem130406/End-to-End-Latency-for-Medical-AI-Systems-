import pandas as pd,matplotlib.pyplot as plt
df=pd.read_csv("data/metrics.csv")
x=range(1,len(df)+1)
y=df["max_ms"]
plt.figure()
plt.bar(x,y) if "max_ms" in ["mean_ms"] else plt.plot(x,y,marker="o")
plt.title("Fig 7a")
plt.ylabel("Maximum E2E (ms)")
plt.xlabel("run")
plt.savefig("plotting/fig7a.png",bbox_inches="tight")
