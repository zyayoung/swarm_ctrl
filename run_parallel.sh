#!/bin/bash

# Register a function to be called on exit
function cleanup {
  echo "Cleaning up..."
  pkill -P $$ # Kill all child processes of this script
}

trap cleanup EXIT

MACHINES=$(cat machines)

for machine in $MACHINES; do
    echo + ssh $machine "$@"
    ssh $machine /home/orangepi/e2e_planner_v1/tools/run_cmd_in_env.sh "$@" &
done

wait
