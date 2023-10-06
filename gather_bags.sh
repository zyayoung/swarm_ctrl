#!/bin/bash

MACHINES=$(cat machines)
CMD="ip a"

DATE=$(date +"%Y%m%d-%H%M")

for machine in $MACHINES; do
    mkdir -p bags_$DATE/$machine/
    scp $machine:/home/orangepi/.ros/*.bag* bags_$DATE/$machine/ &
done

wait
