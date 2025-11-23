#!/usr/bin/env bash
set -e
export CUDA_MPS_PIPE_DIRECTORY=/tmp/mps_$USER
export CUDA_MPS_LOG_DIRECTORY=/tmp/mps_$USER
mkdir -p "$CUDA_MPS_PIPE_DIRECTORY" "$CUDA_MPS_LOG_DIRECTORY"
nvidia-cuda-mps-control -d
