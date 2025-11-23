# Holoscan Latency Determinism

This repository contains the exact steps I used to collect data and reproduce the results for three groups of experiments:
1) Single GPU with and without CUDA Multi-Process Service (Figures 5a–5c)
2) Isolated compute and graphics on multiple GPUs (Figures 6a–6c)
3) All configurations together: Single GPU, Single+MPS, Isolated Multi-GPU, Isolated Multi-GPU+MPS, and Isolated Multi-GPU+MPS+CPU Pinning (Figures 7a–7c)

The repo is split into three phases for each part:
- acquisition: how GPUs were set up and the application was executed to generate raw logs
- export: how raw logs were normalized into CSV files
- plotting: how the nine figures were regenerated

The application is expected to emit per-frame timestamps to stdout or a file in JSON-lines or CSV form with at least these fields:
ingest_ts, pre_ts, infer_ts, render_ts, e2e_ms
If your Holoscan app already logs differently, adapt `parse/compute_metrics.py`'s reader to your field names.

## Requirements

- Ubuntu 20.04/22.04
- NVIDIA driver for your GPUs
- CUDA 12.x
- NVIDIA CUDA MPS available
- python 3.10
- pip packages: see `requirements.txt`
- Holoscan SDK installed and your app binary or Python entry point available locally
- `nvidia-smi`, `taskset` available on PATH

Python deps:
```
pip install -r requirements.txt
```

## Hardware Profiles I used

- Single GPU: Quadro P5000 (also tested with RTX A4000 single GPU on a separate machine)
- Isolated multi-GPU: two GPUs in the system; compute and graphics split across devices
- CPU pinning optional

## Directory Layout

- env/: helper scripts for MPS, CPU pinning
- scripts/: launchers for each experiment part; they create `runs/<part>/<timestamp>/...`
- parse/: converts raw per-frame logs into normalized CSV metrics
- plotting/: figure scripts that read `data/metrics.csv` and regenerate Figures 5–7
- data/: consolidated CSV produced by `parse/compute_metrics.py`
- runs/: raw artifacts per run

## Before You Start

Set your application entry in an environment variable. For a Python Holoscan app:
```
export HOLO_APP="python -u holoscan_apps/endoscopy_app.py"
```
For a compiled app:
```
export HOLO_APP="/path/to/bin/endoscopy_app --args"
```

## Part A : Single GPU, with and without CUDA MPS (Figures 5a–5c)

acquisition:
```
bash scripts/run_single_gpu_no_mps.sh 1
bash scripts/run_single_gpu_no_mps.sh 3
bash scripts/run_single_gpu_no_mps.sh 5

bash scripts/run_single_gpu_mps.sh 1
bash scripts/run_single_gpu_mps.sh 3
bash scripts/run_single_gpu_mps.sh 5
```

export:
```
python parse/compute_metrics.py runs partA data/metrics.csv
```

plotting:
```
python plotting/fig5a.py
python plotting/fig5b.py
python plotting/fig5c.py
```

## Part B : Isolated compute and graphics on multiple GPUs (Figures 6a–6c)

acquisition:
```
bash scripts/run_img_two_gpus.sh 1
bash scripts/run_img_two_gpus.sh 3
bash scripts/run_img_two_gpus.sh 5
```

export:
```
python parse/compute_metrics.py runs partB data/metrics.csv
```

plotting:
```
python plotting/fig6a.py
python plotting/fig6b.py
python plotting/fig6c.py
```

## Part C : All configurations (Figures 7a–7c)

acquisition:
```
bash scripts/run_all_configs.sh 1
bash scripts/run_all_configs.sh 3
bash scripts/run_all_configs.sh 5
```

export:
```
python parse/compute_metrics.py runs partC data/metrics.csv
```

plotting:
```
python plotting/fig7a.py
python plotting/fig7b.py
python plotting/fig7c.py
```

## Notes

- The launchers assume your app writes per-frame logs to `stdout`. They mirror that to files under `runs/.../app_<i>.log` and sample GPU utilization using `scripts/collect_gpu_util.py` in parallel.
- CPU pinning is enabled for the IMG-MPS-Pin configuration via `env/pin_cpu.sh`.
- If you are reproducing on different GPUs, keep the naming consistent; the scripts only care about device indices.

## Recreate in one go

```
bash scripts/demo_all.sh
python parse/compute_metrics.py runs all data/metrics.csv
python plotting/plot_all.py
```

