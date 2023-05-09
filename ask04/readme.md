# Kostas Mathioudakis CSD3982
# Exercise set: 3

***

## Exercise 1

First start minikube withe `kubernetes-version=1.22.4` :

```bash
$   minikube start --kubernetes-version=1.22.4
```


### (a) Create a crd:

```bash
$   kubectl apply -f fruit-crd.yaml
```

![](./img/1_a.PNG)

### b) Create the `fruit` instance:

```bash
$   kubectl apply -f fruit.yaml
```

![](./img/1_b.PNG)

### c) Return the new instance in Yaml Format:

```bash
$   kubectl get apple -o yaml
```

![](./img/1_c.PNG)

### d) Return a list of all available instances:

```bash
$   kubectl get fruits
```

![](./img/1_d.PNG)

***

## Exercise 2

### a)

The dockerfile located at `./2/Dockerfile`:

![](./img/2_a_dockerfile.PNG)

Commands used to build and upload/push to dockerhub:

```bash
    $  docker build -t hw4-2:latest -f Dockerfile .
    $  docker image tag hw4-2:latest kostasmathioudakis/hw4-2
    $  docker push kostasmathioudakis/hw4-2
```

![](./img/2_a_build_and_push_to_dockerhub.PNG)

### b)

The deployment file is at `./2/exercise-4-task-2-deployment.yaml`:

![](./img/2_b_deployment.PNG)

PS: i removed those permissions(rules) i am using in the screenshot and just used * because i couldnt find how to make it work otherwise.

Apply the greeting-crd and the deployment:

```bash
$  kubectl apply -f greeting-crd.yaml
$  kubectl apply -f exercise-4-task-2-deployment.yaml
```

Minikube dashboard logs:

![](./img/2_b_log.PNG)

```bash
$ kubect apply hello-world.yaml
```

![](./img/2_b_hello_dashboard.PNG)

We can also use:

```bash
$ kubectl get services
$ kubectl logs {name}
```

![](./img/2_b_get_services.PNG)

***

## Exercise 3

### a)

 - Removed the lines in the dockerfile for kubectl because they are not necessary for this.
 - Changed the controller app parameters.
 - Built and pushed to dockerhub.


`./3/Dockerfile`

![](./img/3_a_dockerfile.PNG)

`./3/controller.py`

![](./img/3_a_controller.PNG)

![](./img/3_a_dockerhub.PNG)

### b)

The demo pod yaml file is at `/3/demo-pod.yaml`:

![](./img/3_b_demo_pod.PNG)

Made changes to the webhook to the proxy ip and to the container image.

`/3/webhook.yaml`:

![](./img/3_b_webhook.PNG)

First add jetstack and install cert-manager:

```bash
$   helm repo add jetstack https://charts.jetstack.io

$   helm install cert-manager jetstack/cert-manager --namespace cert-manager --create-namespace --version v1.7.2 --set installCRDs=true
```

Then create the namespace, start the webhook and start the demo pods (one in the default namespace and one in the new `test` namespace ) to see if the custom label injection is working properly:

```bash

$   kubectl create namespace test
$   kubectl label namespace test custom-label-injector=enabled
$   kubectl apply -f webhook.yaml
$   kubectl apply -f demo-pod.yaml
$   kubectl apply -f demo-pod.yaml --namespace=test

```

![](./img/3_init_demo.PNG)

To test if it's working correctly:

```bash
$   kubectl get pods -A
$   kubectl get pods -A selector "custom-label"
$   kubectl logs deployment/controller -n custom-label-injector
$   kubectl get pods -A -o=custom-columns=NAMESPACE:.metadata.namespace,NAME:.metadata.name,LABELS:.metadata.labels
```

![](./img/3_get_pods.PNG)

![](./img/3_demo_custom_label_injector.PNG)

![](./img/3_b_labels.PNG)
