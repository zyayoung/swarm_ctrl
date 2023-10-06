#!/bin/bash
  
echo "Are you sure you want to delete bags on all machines? (y/n)"  
  
read answer  
  
if [ "$answer" != "y" ]; then  
  echo "Action cancelled."  
  exit 0  
fi

./run_parallel.sh "rm /home/orangepi/.ros/*.bag*"
