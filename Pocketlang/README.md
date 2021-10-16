# Pocketlang

## Installation

Clone the Git Repository:

`git clone https://github.com/ThakeeNathees/pocketlang.git`

Switch to the new directory:

`cd pocketlang`

build the project:

`make`

This will generate a pocket executable in the `./build/debug/` directory 

make a directory to place your `hello_world.pk` file in:

`mkdir examples`

Copy the 'hello_world.pk' file to the new directory

`cp path_to/hello_world.pk ./examples/`

replacing "path_to" in the above command with the path to your copy of the `hello_world.pk` file. 

## Run Your Code

Run your code with the following:

`./build/debug/pocket ./examples/hello_world.pk`
