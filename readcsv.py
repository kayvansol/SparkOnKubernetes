from pyspark.sql import SparkSession
#from pyspark.sql.functions import sum
from pyspark.context import SparkContext

spark = SparkSession\
            .builder\
            .appName("Mahla")\
            .getOrCreate()
        

sc = spark.sparkContext

path = "people.csv"

df = spark.read.options(delimiter=",", header=True).csv(path)

df.show()

#df.groupBy("Job Title").sum().show() 

df.createOrReplaceTempView("Peopletable")
df2 = spark.sql("select Sex, count(1) countsex, sum(Index) sex_sum " \
                "from peopletable group by Sex")
df2.show()

#df.select(sum(df.Index)).show()
