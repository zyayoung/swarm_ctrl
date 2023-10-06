#!/bin/bash

# Register a function to be called on exit
function cleanup {
  echo "Cleaning up..."
  pkill -P $$ # Kill all child processes of this script
}

trap cleanup EXIT

for i in $(seq 254); do
ping -c 1 -Q 192.168.22.$i | grep "bytes from" &
# sleep 0.1
done

wait
