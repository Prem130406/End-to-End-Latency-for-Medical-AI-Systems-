import sys,time,random,json
n=int(os.environ.get("FRAMES","100"))
for i in range(n):
    e2e=30+random.random()*15
    print(json.dumps({"e2e_ms":e2e}))
    time.sleep(0.03)
