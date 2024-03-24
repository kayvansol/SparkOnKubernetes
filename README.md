# Spark On Kubernetes
Spark On Kubernetes via helm chart

The control-plane & worker nodes addresses are :
```
192.168.56.115
192.168.56.116
192.168.56.117
```
![alt text](https://raw.githubusercontent.com/kayvansol/Ingress/main/pics/vmnet.png?raw=true)


Kubernetes cluster nodes :

![alt text](https://raw.githubusercontent.com/kayvansol/Ingress/main/pics/nodes.png?raw=true)


The Steps :
1) Install spark via helm chart :
```
$ helm repo add bitnami https://charts.bitnami.com/bitnami
$ helm search repo bitnami
$ helm install kayvan-release oci://registry-1.docker.io/bitnamicharts/spark
```
the installed pods :

![alt text](https://raw.githubusercontent.com/kayvansol/SparkOnKubernetes/main/img/Pods.png?raw=true)
