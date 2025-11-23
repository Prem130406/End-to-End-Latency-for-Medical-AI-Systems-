#!/usr/bin/env bash
set -e
export CUDA_MPS_PIPE_DIRECTORY=/tmp/mps_$USER
echo quit | nvidia-cuda-mps-control
rm -rf "$CUDA_MPS_PIPE_DIRECTORY"
