# Bash with ASCII text

This may seem a bit silly, but this technique has a real use. You can use this 
to display the hostname of a machine when logging in using ssh. 

Bash is already installed on most Linux machines, so you only need to change 
the file permissions to make it executable:

`chmod 744 hello_world.sh`

you can then run the executable script with the following:

`./hello_world.sh`

You can generate your own ASCII text here:

[ASCII Text Generator](https://patorjk.com/software/taag/#p=display&f=Doh&t=Hello%20world) 

## Quick Tip
Use the up and down arrow keys to navigate through the various fonts, rather 
than using the drop down selector and your mouse - it is much faster and easier.

## Caution
Be careful with fonts that make use of special characters like quotes ("), single quotes (') 
and backticks (`). They may require you to quote or escape them: 
[Quoting special Characters in Bash](https://www.oreilly.com/library/view/learning-the-bash/1565923472/ch01s09.html
).

