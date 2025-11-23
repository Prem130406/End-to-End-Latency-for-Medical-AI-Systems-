#!/usr/bin/env bash
set -e
export CUDA_VISIBLE_DEVICES=0
: "${HOLO_APP:?}"
STAMP=$(date +%Y%m%d_%H%M%S)
DIR=runs/partB/${STAMP}
mkdir -p "${DIR}"
python scripts/collect_gpu_util.py "${DIR}/gpu0.csv" >/dev/null 2>&1 &
P0=$!
export CUDA_VISIBLE_DEVICES=1
python scripts/collect_gpu_util.py "${DIR}/gpu1.csv" >/dev/null 2>&1 &
P1=$!
pids=()
N=$1
for i in $(seq 1 ${N}); do
  export CUDA_VISIBLE_DEVICES=$(( (i%2) ))
  ${HOLO_APP} 2>&1 | tee "${DIR}/app_${i}.log" &
  pids+=($!)
done
for p in "${pids[@]}"; do
  wait $p
done
kill -INT ${P0} ${P1} || true
