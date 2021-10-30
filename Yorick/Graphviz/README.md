# Graphviz

## Installation

To install grapviz on Debian like systems:

`sudo apt install graphviz`

**Optionally** to make running and opening the resulting image a single step, 
install `xdg-utils`:

`sudo apt install xdg-utils`

## Run Your Code  

To generate your image use the following command:

`dot hello_world.gv -Tpng >hello.png`

This will generate a `hello.png` file in your current directory. You can open this 
with your browser or image editing program. 

**Alternatively** If you installed the `xdg-utils` package, you can generate the 
image and open it using your default png viewer, all in a single step, by using 
the following:

`dot hello_world.gv -Tpng >hello.png | xdg-open hello.png`
