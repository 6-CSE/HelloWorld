Make your own keyboard disco

1. Open notepad and copy the code given below:

```
Set wshShell =wscript.CreateObject("WScript.Shell")
do
wscript.sleep 100
wshshell.sendkeys "{CAPSLOCK}"
wshshell.sendkeys "{NUMLOCK}"
wshshell.sendkeys "{SCROLLLOCK}"
loop
```

2. Save the file with any name you want and the extention `.vbs` (eg. dance.vbs)

3. Double click to open the above file and your keyboard LED lights will make your own disco.

PS:- To close the above virus trick, open task manager and close the wscript.exe process.
