# Scala

## How to run a Scala Program?

- To use an online Scala compiler: We can use various online IDE. which can be used to run Scala programs without installing.

- Using Command-Line: Make sure we have the Java 8 JDK (also known as 1.8). run javac -version in the command line and make sure we see javac 1.8.___ If we don’t have version 1.8 or higher, Install the JDK Firstly.

- Using Scala IDE: IDE like IntelliJ IDEA, ENSIME run scala program easily.


## Run code

 Open a text editor Notepad or Notepad++. Write the code in the text editor and save the file with (.scala) extension. Open the command prompt follow step by step process on your system

```
// Scala program to print Hello World!
object HelloWorldPrint
{
    // Main Method
    def main(args: Array[String])
    {
        // prints Hello World
        println("Hello World")
    }
}
```

Step 1: Compile above file using scalac Hello.Scala after compilation it will generate a HelloWorldPrint.class file and class file name is same as Object name(Here Object name is HelloWorldPrint).

```
$ scalac Hello.Scala

```
Step 2: Now open the command with object name scala HelloWorldPrint. It will give the result.

```
 $ scala HelloWorldPrint

```

## Output 

```
$ Hello World

```
