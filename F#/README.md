## Installation 

### How to install F#

```bash
$ sudo apt-key adv --keyserver hkp://keyserver.ubuntu.com:80 --recv-keys 3FA7E0328081BFF6A14DA29AA6A19B38D3D831EF
$ echo "deb https://download.mono-project.com/repo/ubuntu stable-bionic main" | sudo tee /etc/apt/sources.list.d/mono-official-stable.list
$ sudo apt update
$ sudo apt install mono-complete fsharp
```

### How to run

```bash
$ dotnet fsi HelloWorld.fsx
```

### How to Uninstall F#

```bash
$ sudo apt remove mono-complete fsharp
```