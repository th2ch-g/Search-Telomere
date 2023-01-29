#!/bin/bash

ref=$1
prefix=$2
chr_number=$3
change_nuc=$4
# change from N to $4 for seqkit fish
# https://github.com/shenwei356/seqkit/issues/135
cat $ref | sed -e "s/N/${change_nuc}/g" > ${prefix}.NoN.fa
seqkit split -p $chr_number ${prefix}.NoN.fa

