#@IgnoreInspection BashAddShebang
TASK=2
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
  -input /data/${DATASET}/gutenberg \
  -output $OUTPUT_DIR \
  -mapper mapper.py \
  -mapper combiner.py \
  -reducer reducer.py \
  -file mapper.py \
  -file combiner.py \
  -file reducer.py) 2>&1 | tee ./outputs/task${TASK}.${DATASET}.${DATE}.log

hdfs dfs -cat ${OUTPUT_DIR}/part-* | head -n 20 > $OUTPUT_FILE
cat $OUTPUT_FILE
