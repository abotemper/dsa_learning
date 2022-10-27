public static void main(String[] args) throws Exception {
  JobConf conf = new JobConf(WordCount.class);
  conf.setJobName("wordcount");
  conf.setMapperClass(MapClass.class);
  conf.setCombinerClass(ReduceClass.class);
  conf.setReducerClass(ReduceClass.class);
  FileInputFormat.setInputPaths(conf, args[0]);
  FileOutputFormat.setOutputPath(conf, new Path(args[1]));
  conf.setOutputKeyClass(Text.class);
  conf.setOutputValueClass(IntWritable.class);
  JobClient.runJob(conf);
}

  public class MapClass extends MapReduceBase implements Mapper<LongWritable, Text, Text, IntWritable> {
private final static IntWritable ONE = new IntWritable(1);
public void map(LongWritable key, Text value,
OutputCollector<Text, IntWritable> out,
Reporter reporter) throws IOException {
String line = value.toString();
StringTokenizer itr = new StringTokenizer(line);
while (itr.hasMoreTokens()) {
out.collect(new text(itr.nextToken()), ONE);
}
}
}

public class ReduceClass extends MapReduceBase implements Reducer<Text, IntWritable, Text, IntWritable> {
public void reduce(Text key, Iterator<IntWritable> values,
OutputCollector<Text, IntWritable> out,
Reporter reporter) throws IOException {
int sum = 0;
while (values.hasNext()) {
sum += values.next().get();
}
out.collect(key, new IntWritable(sum));
}
}