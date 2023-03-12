# Exercise 1 #
# Kostas Mathioudakis CSD3982 #

## Exercise 1 ##
### (a) ### 
docker pull nginx:1.23.3  
docker pull nginx:1.23.3-alpine  
![screenshot](./1/a.PNG)

### (b) ###  
docker image ls
![screenshot](./1/b.PNG)

### (c) ### 
docker run -d -p 80:80 nginx:1.23.3-alpine
curl http://localhost
#### The answer of curl is the html file being hosted by the container in the localhost ####  
![screenshot](./1/c.PNG)

### (d) ###
docker ps
![screenshot](./1/d.PNG)

### (e) ###
docker logs (id)
![screenshot](./1/e.PNG)

### (f) ###
docker stop (id)
![screenshot](./1/f.PNG)

### (g) ###
docker ps -a  
docker start (id)  
docker ps  
![screenshot](./1/g.PNG)

### (h) ###
docker ps  
docker stop (id)  
docker rm (id)  
docker ps -a  
![screenshot](./1/h.PNG)

## Exercise 2 ##
### (a) ###  
docker run -d -p 80:80 --name my-nginx nginx:1.23.3-alpine  
docker exec -it my-nginx /bin/sh  
cd /usr/share/nginx/html  
cat index.html  
#### We ran the container with port forwarding to forward it on our machine. Then we opened a shell session in it and changed the contexts of 'index.html' in the '/usr/share/nginx/html' location and added "MY" to where we had to.  Below is a screenshot from the local machine where we curl and see the changes, and below that is another screenshot from the browser  ####
![screenshot](./2/a.PNG)


![screenshot](./2/a2.PNG)


![screenshot](./2/a3.PNG)

### (b) ###  
docker cp my-nginx://usr//share//nginx//html//index.html index.html
ls && cat index.html  
![screenshot](./2/b.PNG)

### (c) ###
docker stop my-nginx  
docker rm my-nginx  
docker run -d -p 80:80 --name my-nginx nginx:1.23.3-alpine
#### We can see that now the page is not changed. That is of course normal because the changes we did on it before were inside the container which we later removed so now the changes are lost. The page we loaded now is from the new container we pulled from docker hub and it has the default html text it ships with. ####
![screenshot](./2/c1.PNG)


![screenshot](./2/c2.PNG)
