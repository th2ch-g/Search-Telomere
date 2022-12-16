#!/bin/env python3

import os
import sys
import subprocess as sb
import matplotlib.pyplot as plt
import seaborn as sns


target_checked_file = sys.argv[1]
prefix = sys.argv[2]

sns.set(style = "darkgrid", palette = "muted", color_codes = True)
#fig, ax = plt.subplots(figsize = (200, 100))
fig, ax = plt.subplots(figsize = (19, 13))
#fig, ax = plt.subplots()

ax.set_title("Chromosome vs TelomereSize")
ax.set_ylabel("Estimate Telomere Size(bp)")
ax.set_xlabel("Chromosome")
plt.yscale('log')


with open(target_checked_file) as ref:
    line_number = 0
    x = 0
    for line in ref:
        line_number += 1
        line = line.rstrip()
        a = line.split(" ")
        chr_name = a[0]
        head_tail = a[1]
        start = int(a[2])
        end = int(a[3])
        strand = a[4]
        combo = int(a[5])
        if line_number % 2 == 1:
            #ax.bar(x, end - start, color = "coral", label = chr_name.split("_")[0] + "_head")
            ax.bar(chr_name + "_head", end - start, color = "coral", label = chr_name.split("_")[0] + "_head")
        else:
            #ax.bar(x + 0.8, end - start, color = "steelblue", label = chr_name.split("_")[0] + "_tail")
            ax.bar(chr_name + "_tail", end - start, color = "steelblue", label = chr_name.split("_")[0] + "_tail")
            x += 2

plt.xticks(rotation=60)
#plt.legend(loc='upper left', bbox_to_anchor=(1, 1), prop={'size': 9})
#ax.axes.xaxis.set_visible(False)
#ax.axes.xaxis.set_ticks([])
#plt.legend(loc='upper left', bbox_to_anchor=(1, 1))
#plt.legend(prop={'size': 20})
#plt.legend()
ax.grid()
plt.grid()
#fig.tight_layout()
plt.savefig(prefix+ ".png")


