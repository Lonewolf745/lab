import java.io.IOException;
import java.util.StringTokenizer;
import org.apache.hadoop.conf.Configuration;
import org.apache.hadoop.fs.Path;
import org.apache.hadoop.io.IntWritable;
import org.apache.hadoop.io.LongWritable;
import org.apache.hadoop.io.Text;
import org.apache.hadoop.mapreduce.Job;
import org.apache.hadoop.mapreduce.Mapper;
import org.apache.hadoop.mapreduce.Reducer;
import org.apache.hadoop.mapreduce.lib.input.FileInputFormat;
import org.apache.hadoop.mapreduce.lib.output.FileOutputFormat;
public class MaxTemperature {
  public static class TemperatureMapper extends Mapper<LongWritable, Text, Text, IntWritable>
{
    private final static int MISSING = 9999;
    
public void map(LongWritable key, Text value, Context context) throws IOException, InterruptedException 
{
String line = value.toString();
String year = line.substring(15,19);
int air;
if(line.charAt(87)=='+')
{
air = Integer.parseInt(line.substring(88,92));
}
else
{
air = Integer.parseInt(line.substring(87,92));
}
context.write(new Text(year),new IntWritable(air)); 
 }
  }
  
  public static class MaxReducer extends Reducer <Text,IntWritable,Text,IntWritable> {
    
    public void reduce(Text key, Iterable<IntWritable> values, Context context) throws IOException, InterruptedException {
      int max_value=Integer.MIN_VALUE;
      for(IntWritable value : values)
      max_value = Math.max(max_value,value.get());
      context.write(key, new IntWritable(max_value));
    }
  }
  public static void main(String[] args) throws Exception {
    Configuration conf = new Configuration();
    Job job = Job.getInstance(conf, "Max Temperature");
    job.setJarByClass(MaxTemperature.class);
    job.setMapperClass(TemperatureMapper.class);
    job.setReducerClass(MaxReducer.class);
    job.setOutputKeyClass(Text.class);
    job.setOutputValueClass(IntWritable.class);
    FileInputFormat.addInputPath(job, new Path(args[0]));
    FileOutputFormat.setOutputPath(job, new Path(args[1]));
    System.exit(job.waitForCompletion(true) ? 0 : 1);
  }
}
