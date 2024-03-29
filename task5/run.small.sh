#@IgnoreInspection BashAddShebang
TASK=5
DATASET=small
OUTPUT_DIR=/user/${USER}/output/task${TASK}/${DATASET}
DATE=`date '+%Y_%m_%d__%H_%M_%S'`

mkdir outputs
OUTPUT_FILE=./outputs/task${TASK}.${DATASET}.${DATE}.out

# Hadoop won't start if the output directory already exists
hdfs dfs -rm -r $OUTPUT_DIR

(time hadoop jar /opt/hadoop/hadoop-2.9.1/share/hadoop/tools/lib/hadoop-streaming-2.9.1.jar \
  -D mapred.reduce.tasks=1 \
  -D mapreduce.job.name=${USER}_task${TASK}_${DATASET} \
  -input /data/${DATASET}/imdb/title.basics.tsv \
  -output $OUTPUT_DIR \
  -mapper mapper.py \
  -reducer reducer.py \
  -file mapper.py \
  -file reducer.py) 2>&1 | tee ./outputs/task${TASK}.${DATASET}.${DATE}.log

# Copy first 20 lines from the output as designated by the assignment document
hdfs dfs -cat ${OUTPUT_DIR}/part-* | head -n 20 > $OUTPUT_FILE
# Copy the actual output to local
hdfs dfs -copyToLocal ${OUTPUT_DIR}/* ./outputs/
# Rename all outputs for current run
# Too tired to find a solution without the cd hack
cd outputs
for i in part-*; do mv "$i" "task${TASK}.${DATASET}.${DATE}.${i%.*}"; done
cd ..
cat $OUTPUT_FILE
