#!/bin/env python3

import sys
import os

chr_number = int(sys.argv[1])
output_dir = "seqkit_fish_result_filtered"

os.system('mkdir ' + output_dir)
for i in range(1, chr_number+1):
    line_number = 0
    out_file = open(output_dir + '/result' + str(i) + '.txt', "w")
    with open("seqkit_fish_result/result" + str(i) + ".txt") as ref:
        for line in ref:
            line_number += 1
            if line_number == 1:
                continue
            line = line.rstrip()
            if (line_number - 1) % 3 == 1:
                tmp1 = line
            if (line_number - 1) % 3 == 2:
                tmp2 = line
            if (line_number - 1) % 3 == 0:
                tmp3 = line

                # process

                # Filter1: end to end alignment query and reference
                a = tmp1.split("\t")
                ref_start = int(a[1])
                ref_end = int(a[2])
                qry_start = int(a[4])
                qry_end = int(a[5])

                if qry_end - qry_start != 7:
                    continue
                if ref_end - ref_start != 7:
                    continue

                #print(tmp1 + "\t" + tmp2 + "\t" + tmp3)
                out_file.write(tmp1 + "\t" + tmp2 + "\t" + tmp3 + "\n")

    out_file.close()


