#!/bin/bash

# Input path of scripts directory
export PATH="<path>/Search-Telomere/scripts:$PATH"

#######################################################################
USAGE='
run-pipeline.sh:
    Search Telomere

USAGE:
    run-pipeline.sh -a <Allow telomere decay bp> -s <Scaffold.fasta> -n <Chromosome_number>

OPTIONS:
    -h, --help                      print help
    -s, --scaffold                  scaffold fasta file
    -a, --allow                     How many bp of telomere decay do we allow [default: 0]
    -p, --prefix                    prefix [default: out]
    -n, --chr-number                Chromosome number [default: 28]
    -r, --telomere-search-range     Telomere search range [default: 150000]
    -m, --motif                     Telomere motif [default: TTTAGGG]

REQUIREMENT:
    seqkit                  seqkit is used for fasta processing
'

scaffold_flag=0
chr_number="28"
telomere_search_range="150000"
prefix="out"
allow_bp="0"
motif="TTTAGGG"
while :;
do
    case $1 in
        -h | --help)
            echo "$USAGE" >&1
            exit 0
            ;;
        -s | --scaffold)
            scaffold_flag=1
            if [ -z "$2" ]; then
                echo "[ERROR] scaffold file name is not detected." >&2
                exit 1
            fi
            scaffold_file=$2
            shift
            ;;
        -a | --allow)
            if [ -z "$2" ]; then
                echo "[ERROR] allow bp size is not detected" >&2
                exit 1
            fi
            allow_bp="$2"
            shift
            ;;
        -p | --prefix)
            if [ -z "$2" ]; then
                echo "[ERROR] prefix is not detected" >&2
                exit 1
            fi
            prefix="$2"
            shift
            ;;
        -n | --chr-number)
            if [ -z "$2" ]; then
                echo "[ERROR] chromosome number is not detected" >&2
                exit 1
            fi
            chr_number="$2"
            ;;
        --)
            shift
            break
            ;;
        -?*)
            echo "[ERROR] Unknown option : ${1}" >&2
            exit 1
            ;;
        *)
            break
    esac
    shift
done


if [ $scaffold_flag -eq 0 ]; then
    echo "[ERROR] file option is necessary" >&2
    exit 1
fi

#=======================================================================
set -e

step1_Prepare.sh $scaffold_file $prefix $chr_number
step2_Search_telomere.sh $prefix $motif $telomere_search_range
step3_Filter_search_telomere.py $chr_number $motif
step4_Sort_filter_telomere.sh $chr_number
step5_Count_telomere.py $prefix $chr_number > result_count_telomere.txt
step6_Check_count_telomere.py $allow_bp > result_count_telomere.checked.txt
#step7_Reformat_result.sh $ $scaffold_file
step8_Plot_telomere_size.py result_count_telomere.checked.txt $prefix

echo "All pipiline done" >&1
