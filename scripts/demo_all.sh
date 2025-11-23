#!/usr/bin/env bash
set -e
bash scripts/run_single_gpu_no_mps.sh 1
bash scripts/run_single_gpu_mps.sh 1
bash scripts/run_img_two_gpus.sh 1
bash scripts/run_all_configs.sh 1
