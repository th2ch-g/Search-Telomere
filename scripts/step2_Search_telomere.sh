#!/bin/bash

prefix=$1
motif=$2
telomere_search_range=$3
count=0
mkdir seqkit_fish_result
for i in $(ls ${prefix}.NoN.fa.split/*.fa);
do
    count=$(( $count + 1 ))
    echo $i
    seqkit fish -j 20 -a -g -F $motif $i -r ":${telomere_search_range},-${telomere_search_range}:" \
        2> seqkit_fish_result/result${count}.txt
done


