import time,sys,subprocess,csv,os
interval=float(os.environ.get("UTIL_INTERVAL","0.1"))
out=sys.argv[1]
didx=os.environ.get("CUDA_VISIBLE_DEVICES","0")
with open(out,"w",newline="") as f:
    w=csv.writer(f)
    w.writerow(["ts","gpu_util","mem_util"])
    while True:
        try:
            res=subprocess.check_output(["nvidia-smi","--query-gpu=utilization.gpu,utilization.memory","--format=csv,noheader,nounits","-i",didx])
            line=res.decode().strip().split(",")
            ts=time.time()
            w.writerow([ts,int(line[0]),int(line[1])])
            f.flush()
            time.sleep(interval)
        except KeyboardInterrupt:
            break
