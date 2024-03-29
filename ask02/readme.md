# Kostas Mathioudakis CSD3982
# Exercise set: 2

## Exercise 1

### a)
Here is the yaml file:

`/1/1_nging_yaml`

![](./1/1_yaml_file.PNG)

```bash
 $ minikube start
```
 This command is used to autoconfigure a minikube cluster.

![](./1/2_minikube_start.PNG)

```bash
 $ kubectl apply -f .\1_nginx.yaml  
```
This command is for applying the manifest on Kubernetes and starting the pod. 

![](./1/3_kubectl_apply.PNG)

### b) 
```bash
 $ kubectl port-forward nginx-pod 8080:80   
```
This command is for port forwarding the pod's port 80 to my local 8080.  

![](./1/4_portforward.PNG)

Then i can open my browser and go to localhost:8080 to see if it's working.  

![](./1/5_browser.PNG)

### c)

```bash
 $ kubectl logs nginx-pod  
```

To see the logs of the nginx-pod.  


![](./1/6_logs.PNG)

### d)

```bash
 $ kubectl exec -it nginx-pod -- /bin/sh  
 $ cd /usr/share/nginx/html  
 $ vi index.html  
```

Start a session inside the nginx-pod and  
make necessary changes in the .html file 
![](./1/7_change_body_of_html.PNG)

Checking the browser to see if the change is showing up:  
![](./1/8_browser.PNG)

### e)

To download default page:  
```bash
 $ curl http://localhost:8080 -o default.html  
```

or 

```bash 
 $ kubectl cp nginx-pod:usr/share/nginx/html/index.html .\default.html
```

In the screenshot i ve provided i 've done the curl method because of less typing
and because i can and it's easy. 

![](./1/9_download_default_page.PNG)

```bash 
 $ kubectl cp .\new.html nginx-pod:usr/share/nginx/html/index.html  
```
Using kubectl cp to change the page to the 'new.html' file.

![](./1/10_copy_new_page.PNG)

Checking if the changes were made by opening localhost on browser:

![](./1/11_browser.PNG)

```bash
 $ kubectl delete -f 1_nginx.yaml
```
### f)

To remove the manifest and delete the pod.

![](./1/12_remove_manifest.PNG)

## Exercise 2

Here is the code in the yaml file:
`/2/2_build_website.yaml`

These are two config maps, one is for installing the dependancies and updating using the synaptic package manager.

The second one is for downloading the website from github installing hugo and setting up the submodules and building the site.
![](./2/1_config_maps.PNG)

Then the job.
![](./2/2_job.PNG)

To confirm that the job completeled successfully i could either run:
```bash
 $ minikube dashboard
```
and look at minikube's dashboard to see if the job was completed or i could simply use :
```bash
 $ kubectl get jobs
```
I can also check the logs for the pod:

```bash
 $ kubectl logs <pod-name>
```

## Exercise 3
Here is the yaml file:

`/3/3_build_and_update.yaml`

PersistentVolumeClaim (PVC): A PVC named pvc is created to provide persistent storage for the website's files. This allows data to be shared between different Kubernetes resources, such as Jobs, CronJobs, and Pods.
![](./3/1_pvc.PNG)

ConfigMap: A ConfigMap named scripts is created to store the `build_website.sh` and `update.sh` scripts. These scripts are responsible for building the website and updating it if changes are detected in the git repository.
![](./3/2_config_map.PNG)

Job: A Job named ubuntu is created to run the `build_website.sh` script. This script clones the repository, builds the website using Hugo, and stores the generated HTML files in the html directory within the PVC.
![](./3/3_ubuntu.PNG)

nginx Pod: A Pod named nginx is created to run the Nginx web server. The PVC is mounted at `/usr/share/nginx`, allowing the web server to serve the HTML files generated by the Job. The Nginx server listens on port 80 to serve the web pages.
![](./3/4_nginx.PNG)

CronJob: A CronJob named job-repeating is scheduled to run the `update.sh` script every night at 2:15.(In the screenshot it's every 3 minutes because i was testing it...) The script checks for changes in the git repository, and if changes are detected, it updates the website and copies the new files to the html directory within the PVC.
![](./3/5_cron_job.PNG)

Data communication between containers:

The primary method of data communication between containers in this solution is through the PVC. The PVC acts as shared storage for the website's files, enabling the Job, CronJob, and Pod to access and manipulate the same data. The Job and CronJob write the generated HTML files to the PVC, while the Nginx Pod reads these files to serve the web pages.

Additionally, the ConfigMap is used to share the build_website.sh and update.sh scripts between the Job and CronJob. The scripts are mounted as volumes into the respective containers, allowing them to execute the scripts.

### Is it working though? 

<img src="./3/chad_yes.png" alt="Chad saying Yes" width="180" height="200">


### Here is the test drive:

```bash
kubectl apply -f .\3_build_and_update.yaml
```

![](./3/6_kubectl_apply.PNG)

Then i am opening the minikube dashboard to check the logs.

First things first the `ubuntu` job logs:
![](./3/7_ubuntu_logs.PNG)

Then port forward the nginx pod:

![](./3/8_port_forward.PNG)

and then i will open `localhost:8080` on my browser and see if it's working while keeping the nginx pod logs open on the other window to see if the `GET` requests have any errors.
![](./3/9_localhost.PNG)

Last but not least i checked that the cronjob runs as it should every 3 minutes:
![](./3/10_cronjob.PNG)

## Exercise 4

`/4/deployment.yaml`

This YAML file defines a Kubernetes deployment to build and serve a static website using Nginx. It includes a Service, PersistentVolumeClaim, ConfigMap, Job, CronJob, and Deployment. The Nginx Pods are embedded in a Deployment, and an init container is used to start the Pods when the web page is finished building. A Service is also added to the manifest.

Service

The Service, nginx-service, is used to expose the Nginx Deployment to the internal network within the Kubernetes cluster. The Service selects all Pods with the label `app: nginx` and listens on port 80.

![](./4/1_service.PNG)

PersistentVolumeClaim

The PersistentVolumeClaim, `pvc`, is used to request a 1Gi storage volume with `ReadWriteOnce` access mode. The storage is used to store the website files and share them among the containers.

![](./4/2_pvc.png)

ConfigMap

The ConfigMap, scripts, stores three shell scripts used in the Job, CronJob, and Deployment:

`build_website.sh`: This script installs the required dependencies, clones the website repository, builds the website using Hugo, and copies the generated files to the html directory.
`update.sh`: This script checks for changes in the Git repository. If changes are detected, it pulls the latest changes, rebuilds the website, and copies the updated files to the html directory.
`check.sh`: This script waits for the index.html file to be present in the html directory before allowing the Nginx Pods to start.
Job

![](./4/3_configmap.PNG.png)

Job

The Job, `ubuntu`, is responsible for building the website using the `build_website.sh` script. The Job uses an Ubuntu container and mounts the PersistentVolumeClaim and the ConfigMap containing the scripts.

![](./4/4_ubuntu.PNG)

CronJob

The CronJob, job-repeating, is responsible for running the `update.sh` script periodically (every day at 2:15 AM) to update the website if there are any changes in the Git repository. The CronJob uses an Ubuntu container and mounts the PersistentVolumeClaim and the ConfigMap containing the scripts.

![](./4/5_cronjob.PNG)


Deployment

The Deployment, `nginx-deployment` , manages the Nginx Pods that serve the website. It uses an init container to run the `check.sh` script before starting the Nginx container. The init container ensures that the `index.html` file is present in the html directory before the Nginx container starts. The Deployment mounts the PersistentVolumeClaim and the ConfigMap containing the scripts.

![](./4/6_deployment.PNG)

### Execution:

First I run the manifest.

```bash
$kubectl apply -f .\deployment.yaml
```

![](./4/7_kubectl_apply.PNG)

Then i check the logs of the ubuntu job to see if the website is being built with hugo.

![](./4/8_ubuntu_hugo_build.PNG)

Then i check if the service for nginx is running and then i port forward and open the site in my browser.

```bash
$kubectl get services
```

```bash
$kubectl port-forward service/nginx-service 8080:80
```

![](./4/9_port_forward_service.PNG)

Checking that the cronjob is also working as it should using the minikube dashboard.

![](./4/10_cronjob.PNG)
