#@IgnoreInspection BashAddShebang
TASK=2
DATASET=large
OUTPUT_DIR=/user/${USER}/output/task${TASK}/${DATASET}
DATE=`date '+%Y_%m_%d__%H_%M_%S'`

mkdir outputs
OUTPUT_FILE=./outputs/task${TASK}.${DATASET}.${DATE}.out

# Hadoop won't start if the output directory already exists
hdfs dfs -rm -r $OUTPUT_DIR
hdfs dfs -rm -r /user/${USER}/assignment/task${TASK}

(time hadoop jar /opt/hadoop/hadoop-2.9.1/share/hadoop/tools/lib/hadoop-streaming-2.9.1.jar \
  -D mapreduce.job.name=${USER}_task${TASK}_${DATASET} \
  -input /data/${DATASET}/gutenberg \
  -output $OUTPUT_DIR \
  -mapper mapper.py \
  -combiner combiner.py \
  -reducer reducer.py \
  -file mapper.py \
  -file combiner.py \
  -file reducer.py) 2>&1 | tee ./outputs/task${TASK}.${DATASET}.${DATE}.log

# Copy output to the folder designated by the assignment document
hdfs dfs -cp ${OUTPUT_DIR} /user/${USER}/assignment/task${TASK}
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
