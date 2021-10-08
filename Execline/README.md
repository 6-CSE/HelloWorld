# Execline

To install execline on Debian like systems: 

`sudo apt install execline`

Make your hello_world.e file executable:

`chmod 744 hello_world.e`

You can execute the file with:

`./hello_world.e`

## Note ##
The execline executable may not have been installed on your path.
if running the program results in a **No such file or directory error**. 

You will need to edit the first line of the hello_world.e file.

*\#!/usr/lib/execline/bin/execline*

This line is called a shebang, it tells the system to run the file using the 
program (execlineb - the package is execline but the executable is execlineb) and where to find it (its path). 

The shebang line begins with **#!** this is followed immediately (no spaces) 
by the full path to the excline executable **execlineb**.

You can find the full path using the find command:

`sudo find / -name execlineb`

edit the first line of hello_world.e replacing: 

*/usr/lib/execline/bin/execline*

with the path returned from the find command.

## References ##

For more info on the [shebang](https://bash.cyberciti.biz/guide/Shebang)

To learn more about the * find * and *chmod* commands see their respective man pages 

`man find`

`man chmod`

