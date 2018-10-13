#@IgnoreInspection BashAddShebang
TASK=8
DATASET=small
OUTPUT_DIR_JOB_1=/user/${USER}/output/task${TASK}/${DATASET}/job1
OUTPUT_DIR_JOB_2=/user/${USER}/output/task${TASK}/${DATASET}/job2
DATE=`date '+%Y_%m_%d__%H_%M_%S'`

mkdir outputs
mkdir outputs/job1
mkdir outputs/job2

OUTPUT_FILE_JOB_1=./outputs/job1/task${TASK}.${DATASET}.${DATE}.out
OUTPUT_FILE_JOB_2=./outputs/job2/task${TASK}.${DATASET}.${DATE}.out

# Hadoop won't start if the output directories already exists
hdfs dfs -rm -r $OUTPUT_DIR_JOB_1
hdfs dfs -rm -r $OUTPUT_DIR_JOB_2

(time hadoop jar /opt/hadoop/hadoop-2.9.1/share/hadoop/tools/lib/hadoop-streaming-2.9.1.jar \
  -D mapreduce.job.name=${USER}_task${TASK}_${DATASET}_job1 \
  -D num.key.fields.for.partition=2 \
  -input /data/${DATASET}/imdb/title.basics.tsv \
  -input /data/${DATASET}/imdb/title.ratings.tsv \
  -output $OUTPUT_DIR_JOB_1 \
  -mapper mapper.py \
  -reducer reducer.py \
  -file mapper.py \
  -file reducer.py) 2>&1 | tee ./outputs/job1/task${TASK}.${DATASET}.${DATE}.log

(time hadoop jar /opt/hadoop/hadoop-2.9.1/share/hadoop/tools/lib/hadoop-streaming-2.9.1.jar \
  -D mapreduce.job.name=${USER}_task${TASK}_${DATASET}_job2 \
  -input $OUTPUT_DIR_JOB_1 \
  -output $OUTPUT_DIR_JOB_2 \
  -mapper mapper2.py \
  -reducer reducer2.py \
  -file mapper2.py \
  -file reducer2.py) 2>&1 | tee ./outputs/job2/task${TASK}.${DATASET}.${DATE}.log


# Copy first 20 lines from the output as designated by the assignment document
hdfs dfs -cat ${OUTPUT_DIR_JOB_1}/part-* | head -n 20 > $OUTPUT_FILE_JOB_1
hdfs dfs -cat ${OUTPUT_DIR_JOB_2}/part-* | head -n 20 > $OUTPUT_FILE_JOB_2
# Copy the actual output to local
hdfs dfs -copyToLocal ${OUTPUT_DIR_JOB_1}/* ./outputs/job1
hdfs dfs -copyToLocal ${OUTPUT_DIR_JOB_2}/* ./outputs/job2
# Rename all outputs for current run
# Too tired to find a solution without the cd hack
cd outputs/job1
for i in part-*; do mv "$i" "task${TASK}.${DATASET}.${DATE}.${i%.*}"; done
cd ../..
cd outputs/job2
for i in part-*; do mv "$i" "task${TASK}.${DATASET}.${DATE}.${i%.*}"; done
cd ../..
cat $OUTPUT_FILE_JOB_1
cat $OUTPUT_FILE_JOB_2
