# Spark On Kubernetes
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

***
The Steps :
1) Install spark via helm chart **(bitnami)** :
```
$ helm repo add bitnami https://charts.bitnami.com/bitnami
$ helm search repo bitnami
$ helm install kayvan-release oci://registry-1.docker.io/bitnamicharts/spark
```
the installed **pods** :

![alt text](https://raw.githubusercontent.com/kayvansol/SparkOnKubernetes/main/img/Pods.png?raw=true)

and **Services** (headless for statefull) :

![alt text](https://raw.githubusercontent.com/kayvansol/SparkOnKubernetes/main/img/Services.png?raw=true)

and the **spark master** is :

![alt text](https://raw.githubusercontent.com/kayvansol/SparkOnKubernetes/main/img/Master.png?raw=true)

***
2) type the below commands on kubernetes kube-apiserver :
```
kubectl exec -it  kayvan-release-spark-master-0 -- /bin/bash

./bin/spark-submit \
  --class org.apache.spark.examples.SparkPi \
  --master spark://kayvan-release-spark-master-0.kayvan-release-spark-headless.default.svc.cluster.local:7077 \
  ./examples/jars/spark-examples_2.12-3.4.1.jar 1000
```

![alt text](https://raw.githubusercontent.com/kayvansol/SparkOnKubernetes/main/img/Command.png?raw=true)

***
3) The final **result** is 🍹 :

![alt text](https://raw.githubusercontent.com/kayvansol/SparkOnKubernetes/main/img/Result.png?raw=true)

![alt text](https://raw.githubusercontent.com/kayvansol/SparkOnKubernetes/main/img/Completed.png?raw=true)
