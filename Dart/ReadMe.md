
# Installation 


**How to install dart SDK on Ubuntu**

***Perform the following one-time setup:***
```
$ sudo apt-get update

$ sudo apt-get install apt-transport-https

$ sudo sh -c 'wget -qO- https://dl-ssl.google.com/linux/linux_signing_key.pub | apt-key add -'
 
$ sudo sh -c 'wget -qO- https://storage.googleapis.com/download.dartlang.org/linux/debian/dart_stable.list > /etc/apt/sources.list.d/dart_stable.list'
```



***Then install the Dart SDK:***
```
$ sudo apt-get update
 
$ sudo apt-get install dart
```
---


# How to run

```
$ dart HelloWorld.dart
```
