#!/bin/env python3

import sys
import os

result_file = "result_count_telomere.txt"
allowed_bp = int(sys.argv[1])

os.system('cat ' + result_file + ' | choose 0 | uniq > tmp.chr.list')

with open("tmp.chr.list") as ref:
    for line in ref:
        line = line.rstrip()

        chr_list = []
        with open(result_file) as ref2:
            for line2 in ref2:
                line2 = line2.rstrip()

                if line not in line2:
                    continue

                a = line2.split(" ")
                tmp_list = []
                # start end strand combo
                tmp_list.append(int(a[1]))
                tmp_list.append(int(a[2]))
                tmp_list.append(a[3])
                tmp_list.append(int(a[4]))
                chr_list.append(tmp_list)

        # process
        # make super group by allowing gap
        super_chr_list = []
        for i in range(0, len(chr_list)):
            if i == 0:
                pre_start = chr_list[i][0]
                pre_end = chr_list[i][1]
                pre_strand = chr_list[i][2]
                pre_combo = chr_list[i][3]
                continue
            if chr_list[i][0] - pre_end <= allowed_bp and chr_list[i][2] == pre_strand:
                pre_end = chr_list[i][1]
                pre_combo += chr_list[i][3]
            else:
                #print(line, pre_start, pre_end, pre_strand, pre_combo)
                super_chr_list.append([line, pre_start, pre_end, pre_strand, pre_combo])
                pre_start = chr_list[i][0]
                pre_end = chr_list[i][1]
                pre_strand = chr_list[i][2]
                pre_combo = chr_list[i][3]
        #print(line, pre_start, pre_end, pre_strand, pre_combo)
        super_chr_list.append([line, pre_start, pre_end, pre_strand, pre_combo])

        print(line, "head-telomere", super_chr_list[0][1], super_chr_list[0][2], super_chr_list[0][3], super_chr_list[0][4])
        print(line, "tail-telomere", super_chr_list[-1][1], super_chr_list[-1][2], super_chr_list[-1][3], super_chr_list[-1][4])

os.system('rm -f tmp.chr.list')
