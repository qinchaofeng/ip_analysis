#!/bin/bash

while read line
do
#    echo $line
    python ip_jiexi.py $line
done<ip.txt
