# Bash/Cowsay 

This is a fun little hello world that draws an ascii art version
of Tux (the Linux Mascot) saying "Hello world." to your terminal.
 
Bash should already be installed, but to install cowsay on Debian like systems:

`sudo apt install cowsay`

Then change the permission on the "hello_world.sh: file:

`chmod 744 hello_world.sh`

This will make the hello_world.sh file executable. 

Now you can run the script with:

`./hello_world.sh`

Try some of the other characters by changing Tux to:

- default (a cow)
- moose
- turtle

You can see a full list of the available characters with the following:

`ls /usr/share/cowsay/cows`

