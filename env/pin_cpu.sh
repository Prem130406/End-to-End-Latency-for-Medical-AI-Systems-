#!/usr/bin/env bash
set -e
core=${1:-0}
shift
taskset -c $core "$@"
