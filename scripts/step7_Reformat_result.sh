#!/bin/bash

target_file=$1
scaffold=$2

while IFS= read -r line;
do
    chr_name=$(echo $line | choose 0)
    head_tail=$(echo $line | choose 1)
    tstart=$(echo $line | choose 2)
    tend=$(echo $line | choose 3)
    strand=$(echo $line | choose 4)

    seq_len=$(seqkit grep -np $chr_name $scaffold | seqkit stats | tail -n +2 | choose 4 | choose : -f "," -o "")

    # chrname, head or tail, telomere size, telomere position
    echo "$chr_name $head_tail $(echo ""|awk -v start=$tstart -v end=$tend '{print end - start}') $(echo ""|awk -v start=$tstart -v end=$tend -v seqlen=$seq_len '{print end/seqlen*100}') $strand"

done < $target_file



