import os,sys,glob,json,re,pandas as pd,numpy as np
root=sys.argv[1]
part=sys.argv[2]
out=sys.argv[3]
rows=[]
for path in glob.glob(os.path.join(root,"**","app_*.log"),recursive=True):
    with open(path) as f:
        for line in f:
            try:
                if line.strip().startswith("{"):
                    j=json.loads(line)
                    e2e=j.get("e2e_ms")
                    if e2e is not None:
                        rows.append({"part":part,"run":os.path.dirname(path),"e2e_ms":float(e2e)})
                else:
                    m=re.search(r"e2e_ms=([0-9]+\.?[0-9]*)",line)
                    if m:
                        rows.append({"part":part,"run":os.path.dirname(path),"e2e_ms":float(m.group(1))})
            except Exception:
                pass
df=pd.DataFrame(rows)
if df.empty:
    raise SystemExit("no samples found")
g=df.groupby("run")["e2e_ms"]
meta=g.agg(["mean","std","max",lambda x: np.percentile(x,90)-np.percentile(x,10)]).reset_index()
meta.columns=["run","mean_ms","std_ms","max_ms","flat_ms"]
meta.to_csv(out,index=False)
print(out)
