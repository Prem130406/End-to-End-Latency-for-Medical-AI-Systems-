#!/usr/bin/env bash
set -e
bash scripts/run_single_gpu_no_mps.sh $1
bash scripts/run_single_gpu_mps.sh $1
bash scripts/run_img_two_gpus.sh $1
bash env/mps_start.sh
bash scripts/run_img_two_gpus.sh $1
bash env/mps_stop.sh
CORES=($(seq 0 7))
i=0
N=$1
STAMP=$(date +%Y%m%d_%H%M%S)
DIR=runs/partC/${STAMP}
mkdir -p "${DIR}"
: "${HOLO_APP:?}"
for k in $(seq 1 ${N}); do
  c=${CORES[$((i%${#CORES[@]}))]}
  i=$((i+1))
  bash env/pin_cpu.sh $c ${HOLO_APP} 2>&1 | tee "${DIR}/app_${k}.log" &
  pids+=($!)
done
for p in "${pids[@]}"; do
  wait $p
done
