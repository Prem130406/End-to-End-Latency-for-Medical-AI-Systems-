import pandas as pd,matplotlib.pyplot as plt
df=pd.read_csv("data/metrics.csv")
x=range(1,len(df)+1)
y=df["mean_ms"]
plt.figure()
plt.bar(x,y) if "mean_ms" in ["mean_ms"] else plt.plot(x,y,marker="o")
plt.title("Fig 5a")
plt.ylabel("Average E2E (ms)")
plt.xlabel("run")
plt.savefig("plotting/fig5a.png",bbox_inches="tight")
