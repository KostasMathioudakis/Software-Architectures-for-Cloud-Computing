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
