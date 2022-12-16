#!/bin/bash

ref=$1
prefix=$2
chr_number=$3
cat $ref | sed -e 's/N//g' > ${prefix}.NoN.fa
seqkit split -p $chr_number ${prefix}.NoN.fa

