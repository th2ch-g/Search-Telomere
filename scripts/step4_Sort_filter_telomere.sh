#!/bin/bash

chr_number=$1
mkdir seqkit_fish_result_filtered_sorted
for i in `seq $chr_number`;
do
    cat seqkit_fish_result_filtered/result${i}.txt | sort -n -k 2 > seqkit_fish_result_filtered_sorted/result${i}.txt
done

