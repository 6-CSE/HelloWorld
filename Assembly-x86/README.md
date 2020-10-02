## Installation 

### How to install NASM

```bash
$ sudo apt install as31 nasm 
```

### How to run

```bash
$ nasm -f elf64 hello_world.asm
$ ld -s -o hello_world hello_world.o
$ ./hello_world
```

### How to Uninstall NASM

```bash
$ sudo apt remove as31 nasm
```