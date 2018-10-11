#@IgnoreInspection BashAddShebang
TASK=1
DATASET=large
OUTPUT_DIR=/user/${USER}/output/task${TASK}/${DATASET}
OUTPUT_FILE=./outputs/task${TASK}.${DATASET}.`date '+%Y_%m_%d__%H_%M_%S'`.out

# Hadoop won't start if the output directory already exists
hdfs dfs -rm -r $OUTPUT_DIR
hdfs dfs -rm -r /user/${USER}/assignment/task${TASK}

time hadoop jar /opt/hadoop/hadoop-2.9.1/share/hadoop/tools/lib/hadoop-streaming-2.9.1.jar \
  -D mapred.reduce.tasks=1 \
  -D mapreduce.job.name=${USER}_task${TASK}_${DATASET} \
  -input /data/${DATASET}/gutenberg \
  -output $OUTPUT_DIR \
  -mapper mapper.py \
  -reducer reducer.py \
  -file mapper.py \
  -file reducer.py | tee ./outputs/task${TASK}.${DATASET}.`date '+%Y_%m_%d__%H_%M_%S'`.log

hdfs dfs -cp ${OUTPUT_DIR}/part-* /user/${USER}/assignment/task${TASK}
hdfs dfs -cat ${OUTPUT_DIR}/part-* | head -n 20 > $OUTPUT_FILE
cat $OUTPUT_FILE
