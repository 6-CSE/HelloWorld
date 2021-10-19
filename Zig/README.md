# Zig

## Installation

Download the appropriate package from the [Ziglang website](https://ziglang.org/download/)

for example on my Raspberry Pi:

`wget https://ziglang.org/download/0.8.1/zig-linux-armv7a-0.8.1.tar.xz`

Uncompress the downloaded file 

`tar xvf zig-linux-armv7a-0.8.1.tar.xz`

switch to the new directory:

`cd zig-linux-armv7a-0.8.1/'

Create a new directory to hold your `hello_world.zig` file

`mkdir examples`

Copy the `hello_world.zig` file to this new directory:

`cp path_to/hello_world.zig ./examples/`

replacing path_to in the above command with the actual path to `hello_world.zig` from your system.

## Compile Your Code

`./zig build-exe ./examples/hello_world.zig`

## Run the Resulting Binary

`./hello_world`
