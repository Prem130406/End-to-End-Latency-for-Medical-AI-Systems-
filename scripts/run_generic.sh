#!/usr/bin/env bash
set -e
PART=$1
N=$2
STAMP=$(date +%Y%m%d_%H%M%S)
DIR=runs/${PART}/${STAMP}
mkdir -p "${DIR}"
: "${HOLO_APP:?set HOLO_APP to your app command}"
if [ -z "${CUDA_VISIBLE_DEVICES}" ]; then export CUDA_VISIBLE_DEVICES=0; fi
python scripts/collect_gpu_util.py "${DIR}/gpu.csv" >/dev/null 2>&1 &
UTIL_PID=$!
pids=()
for i in $(seq 1 ${N}); do
  ${HOLO_APP} 2>&1 | tee "${DIR}/app_${i}.log" &
  pids+=($!)
done
for p in "${pids[@]}"; do
  wait $p
done
kill -INT ${UTIL_PID} || true
