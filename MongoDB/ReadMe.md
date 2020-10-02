
# Installation 


**How to install Postgresql on Ubuntu**

```
$ sudo apt-get update

$ sudo apt install -y mongodb

Checking the Service and Database :

$ sudo systemctl status mongodb
```



# How to run 

```
(By default mongodb has no enabled access control, so there is no default user or password.)

$ sudo mongo

> var file = cat('HelloWorld.json');  

> use firstdatabase;                     

> var o = JSON.parse(file);         

> db.hello.insert(o);                

> db.hello.find({}, {_id:0});
```
