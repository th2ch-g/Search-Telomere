#!/bin/env python3

import sys
import os
import subprocess as sb

prefix = sys.argv[1]
chr_number = int(sys.argv[2])

# Record data
all_chr_list = []
for i in range(1, chr_number+1):
    line_number = 0
    chr_list = []
    tmp_chr_list = []
    with open("seqkit_fish_result_filtered_sorted/result" + str(i) + ".txt") as ref:
        for line in ref:
            line = line.rstrip()
            line_number += 1
            if line_number == 1:
                cmd = 'seqkit grep -np ' + line.split("\t")[0] + ' ' +  prefix + '.NoN.fa  | seqkit stats | tail -n +2 | choose 4 | choose : -f "," -o "" '
                res = sb.run(cmd, shell = True, capture_output = True, text = True)
                seq_len = int(res.stdout.rstrip())

            a = line.split("\t")
            # seqlen, chr_name, start, end, strand
            tmp_chr_list.append(seq_len)
            tmp_chr_list.append(a[0])
            tmp_chr_list.append(int(a[1]))
            tmp_chr_list.append(int(a[2]))
            tmp_chr_list.append(a[6])
            chr_list.append(tmp_chr_list)
            tmp_chr_list = []

    all_chr_list.append(chr_list)



# make group
for i in range(0, len(all_chr_list)):
    for j in range(0, len(all_chr_list[i])):
        if j == 0:
            pre_start = all_chr_list[i][j][2]
            pre_end = all_chr_list[i][j][3]
            pre_strand = all_chr_list[i][j][4]
            combo = 1
            continue
        if all_chr_list[i][j][2] == pre_end and all_chr_list[i][j][4] == pre_strand:
            pre_end = all_chr_list[i][j][3]
            combo += 1
        else:
            print(all_chr_list[i][j][1], pre_start, pre_end, pre_strand, combo)
            pre_start = all_chr_list[i][j][2]
            pre_end = all_chr_list[i][j][3]
            pre_strand = all_chr_list[i][j][4]
            combo = 1
    print(all_chr_list[i][j][1], pre_start, pre_end, pre_strand, combo)

