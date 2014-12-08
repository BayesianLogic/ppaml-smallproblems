#!/bin/bash
source $1

PARAM_FILE=$1
INPUT_DIR=$2
OUTPUT_DIR=$3

mkdir -p $OUTPUT_DIR
echo $2 > input_dir
echo $3 > output_dir

python prob1_gen.py < input_dir
blog -n $NUM_SAMPLES prob1.blog -o $3/prob1_out
