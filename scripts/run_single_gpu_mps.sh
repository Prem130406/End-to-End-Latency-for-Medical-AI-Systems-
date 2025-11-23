#!/usr/bin/env bash
set -e
bash env/mps_start.sh
bash scripts/run_generic.sh partA $1
bash env/mps_stop.sh
