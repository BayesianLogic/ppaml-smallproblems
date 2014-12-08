#!/bin/bash
source $1

PARAM_FILE=$1
INPUT_DIR=$2
OUTPUT_DIR=$3

mkdir -p $OUTPUT_DIR
echo $2 > input_dir
echo $3 > output_dir

python prob2_gen.py < input_dir

$ENGROOT/blog-VERSION/bin/blog -n $NUM_SAMPLES prob2.blog -o $3/prob2_out

