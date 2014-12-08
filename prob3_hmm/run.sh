#!/bin/bash
source $1

PARAM_FILE=$1
INPUT_DIR=$2
OUTPUT_DIR=$3

mkdir -p $OUTPUT_DIR
echo $2 > input_dir
echo $3 > output_dir

python prob3_gen.py < input_dir
$ENGROOT/blog-VERSION/bin/blog -n $NUM_SAMPLES prob3.blog -o $3/hmm_out
python output_processing.py < output_dir
$ENGROOT/blog-VERSION/bin/blog -e blog.engine.ParticleFilter -n $NUM_SAMPLES prob3.blog -o $3/hmmfiltering_out