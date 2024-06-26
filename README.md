# Spark On Kubernetes
![alt text](https://raw.githubusercontent.com/kayvansol/SparkOnKubernetes/main/img/logo.png?raw=true)


Spark On Kubernetes via **helm chart**

The control-plane & worker nodes addresses are :
```
192.168.56.115
192.168.56.116
192.168.56.117
```
![alt text](https://raw.githubusercontent.com/kayvansol/Ingress/main/pics/vmnet.png?raw=true)


Kubernetes cluster **nodes** :

![alt text](https://raw.githubusercontent.com/kayvansol/Ingress/main/pics/nodes.png?raw=true)

you can install helm via the link [helm](https://helm.sh/docs/intro/install) :

***
The Steps :
1) Install spark via helm chart **(bitnami)** :

<img src="https://raw.githubusercontent.com/kayvansol/SparkOnKubernetes/main/img/bitnami.png" width="500" height="200">
   
```
$ helm repo add bitnami https://charts.bitnami.com/bitnami
$ helm search repo bitnami
$ helm install kayvan-release oci://registry-1.docker.io/bitnamicharts/spark
$ helm upgrade kayvan-release bitnami/spark --set worker.replicaCount=5
```
the installed **6 pods** :

![alt text](https://raw.githubusercontent.com/kayvansol/SparkOnKubernetes/main/img/Pods.png?raw=true)

and **Services** (headless for statefull) :

![alt text](https://raw.githubusercontent.com/kayvansol/SparkOnKubernetes/main/img/Services.png?raw=true)

and the **spark master ui** is :

![alt text](https://raw.githubusercontent.com/kayvansol/SparkOnKubernetes/main/img/Master.png?raw=true)

***
2) type the below commands on kubernetes kube-apiserver :
```
kubectl exec -it  kayvan-release-spark-master-0 -- ./bin/spark-submit \
  --class org.apache.spark.examples.SparkPi \
  --master spark://kayvan-release-spark-master-0.kayvan-release-spark-headless.default.svc.cluster.local:7077 \
  ./examples/jars/spark-examples_2.12-3.4.1.jar 1000

```
or

```
kubectl exec -it  kayvan-release-spark-master-0 -- /bin/bash

./bin/spark-submit \
  --class org.apache.spark.examples.SparkPi \
  --master spark://kayvan-release-spark-master-0.kayvan-release-spark-headless.default.svc.cluster.local:7077 \
  ./examples/jars/spark-examples_2.12-3.4.1.jar 1000


./bin/spark-submit \
  --class org.apache.spark.examples.SparkPi \
  --master spark://kayvan-release-spark-master-0.kayvan-release-spark-headless.default.svc.cluster.local:7077 \
  ./examples/src/main/python/pi.py 1000


./bin/spark-submit \
  --class org.apache.spark.examples.SparkPi \
  --master spark://kayvan-release-spark-master-0.kayvan-release-spark-headless.default.svc.cluster.local:7077 \
  ./examples/src/main/python/wordcount.py //filepath

```

![alt text](https://raw.githubusercontent.com/kayvansol/SparkOnKubernetes/main/img/Command.png?raw=true)

![alt text](https://raw.githubusercontent.com/kayvansol/SparkOnKubernetes/main/img/logo2.png?raw=true)

the exact **scala & python** code of spark-examples_2.12-3.4.1.jar , pi.py & wordcount.py :

[examples/src/main/scala/org/apache/spark/examples/SparkPi.scala](https://github.com/apache/spark/blob/master/examples/src/main/scala/org/apache/spark/examples/SparkPi.scala)

[examples/src/main/python/pi.py](https://github.com/apache/spark/blob/master/examples/src/main/python/pi.py)

[examples/src/main/python/wordcount.py](https://github.com/apache/spark/blob/master/examples/src/main/python/wordcount.py)

***

3) The final **result** is 🍹 :

for **scala** :

![alt text](https://raw.githubusercontent.com/kayvansol/SparkOnKubernetes/main/img/Result.png?raw=true)

for **python** :

![alt text](https://raw.githubusercontent.com/kayvansol/SparkOnKubernetes/main/img/ResultPy.png?raw=true)

![alt text](https://raw.githubusercontent.com/kayvansol/SparkOnKubernetes/main/img/Completed.png?raw=true)

***

The other **python** <img src="https://github.com/devicons/devicon/raw/master/icons/python/python-original.svg" title="Python" alt="Python" width="20" height="20" style="max-width: 100%;"> Programm :

1) Copy **People.csv** (large file) inside spark worker pods :

![alt text](https://raw.githubusercontent.com/kayvansol/SparkOnKubernetes/main/img/ProgPy0.png?raw=true)

```
kubectl cp people.csv kayvan-release-spark-worker-{x}:/opt/bitnami/spark
```

Notes: 
- you can download the file from [link](https://www.datablist.com/learn/csv/download-sample-csv-files)  
- you can also use a **nfs share folder** for read large csv file from it instead of copying it inside pods.

2) Write some python codes inside **readcsv.py** please :
```python
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
```
![alt text](https://raw.githubusercontent.com/kayvansol/SparkOnKubernetes/main/img/ProgPy1.png?raw=true)

3) copy readcsv.py file inside spark **master** pod :
```
kubectl cp readcsv.py kayvan-release-spark-master-0:/opt/bitnami/spark
```

4) run the code :
```
kubectl exec -it  kayvan-release-spark-master-0 -- ./bin/spark-submit   --class org.apache.spark.examples.SparkPi
      --master spark://kayvan-release-spark-master-0.kayvan-release-spark-headless.default.svc.cluster.local:7077 
        readcsv.py
```

5) showing some data :

![alt text](https://raw.githubusercontent.com/kayvansol/SparkOnKubernetes/main/img/ProgPy2.png?raw=true)

6) the next result data:

![alt text](https://raw.githubusercontent.com/kayvansol/SparkOnKubernetes/main/img/ProgPy3.png?raw=true)

7) the time consuming for processing :

![alt text](https://raw.githubusercontent.com/kayvansol/SparkOnKubernetes/main/img/ProgPy4.png?raw=true)

***
The other **python** <img src="https://github.com/devicons/devicon/raw/master/icons/python/python-original.svg" title="Python" alt="Python" width="20" height="20" style="max-width: 100%;"> Programm on **Docker Desktop** :

docker-compose.yml :
```yaml
version: '3.6'

services:

  spark:
    container_name: spark
    image: bitnami/spark:latest
    environment:
      - SPARK_MODE=master
      - SPARK_RPC_AUTHENTICATION_ENABLED=no
      - SPARK_RPC_ENCRYPTION_ENABLED=no
      - SPARK_LOCAL_STORAGE_ENCRYPTION_ENABLED=no
      - SPARK_SSL_ENABLED=no
      - SPARK_USER=root   
      - PYSPARK_PYTHON=/opt/bitnami/python/bin/python3
    ports:
      - 127.0.0.1:8081:8080

  spark-worker:
    image: bitnami/spark:latest
    environment:
      - SPARK_MODE=worker
      - SPARK_MASTER_URL=spark://spark:7077
      - SPARK_WORKER_MEMORY=2G
      - SPARK_WORKER_CORES=2
      - SPARK_RPC_AUTHENTICATION_ENABLED=no
      - SPARK_RPC_ENCRYPTION_ENABLED=no
      - SPARK_LOCAL_STORAGE_ENCRYPTION_ENABLED=no
      - SPARK_SSL_ENABLED=no
      - SPARK_USER=root
      - PYSPARK_PYTHON=/opt/bitnami/python/bin/python3
```
```
docker-compose up --scale spark-worker=2
```

![alt text](https://raw.githubusercontent.com/kayvansol/SparkOnKubernetes/main/img/partition4.png?raw=true)

copy required files to containers :

for e.g.
```bash
docker cp file.csv spark-worker-1:/opt/bitnami/spark
```

python code on master :

```python
from pyspark.sql import SparkSession

spark = SparkSession.builder.appName("Writingjson").getOrCreate()

df = spark.read.option("header", True).csv("csv/file.csv").coalesce(2)

df.show()

df.write.partitionBy('name').mode('overwrite').format('json').save('file_name.json')
```

run the code on spark master docker container :
```bash
./bin/spark-submit --master spark://4f28330ce077:7077 csv/ctp.py
```
showing some data :

![alt text](https://raw.githubusercontent.com/kayvansol/SparkOnKubernetes/main/img/partition2.png?raw=true)

and the seperated json files based on name partitioning :

![alt text](https://raw.githubusercontent.com/kayvansol/SparkOnKubernetes/main/img/partition1.png?raw=true)

data for name=kayvan :

![alt text](https://raw.githubusercontent.com/kayvansol/SparkOnKubernetes/main/img/partition3.png?raw=true)
