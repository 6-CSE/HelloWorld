
# Installation 


**How to install Go Ubuntu**

```
$ sudo apt-get update

$ wget -c https://dl.google.com/go/go1.14.2.linux-amd64.tar.gz -O - | sudo tar -xz -C /usr/local
```

Adjusting the Path Variable : 

```
$ sudo echo 'export GOPATH=$HOME/work' >> ~/.profile
$ sudo echo 'export PATH=$PATH:/usr/local/go/bin:$GOPATH/bin' >> ~/.profile
$ source ~/.profile
```
OR
```
$ sudo nano ~/.profile

At the end of the file, add this line:

export GOPATH=$HOME/work
export PATH=$PATH:/usr/local/go/bin:$GOPATH/bin

(ctrl+s and ctrl+x to exit nano)

$ source ~/.profile
```

to know version : 
```
$ go version 
```



# How to run

```
$ go run HelloWorld.go 
```
# uninstall go

```
$ sudo apt-get remove --auto-remove golang-go.
```
