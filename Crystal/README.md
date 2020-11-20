# Installation 

**Install Arch**   
sudo pacman -S crystal shards  


**Install MacOS**

brew update   
brew install crystal   


**Install Ubuntu**  

## Setup repository  
First you have to add the repository to your APT configuration.
For easy setup just run in your command line: 

curl -sSL https://dist.crystal-lang.org/apt/setup.sh |     sudo bash
That will add the signing key and the repository configuration. If you prefer to do it manually, execute the following commands:

curl -sL "https://keybase.io/crystal/pgp_keys.asc" |      sudo apt-key add -
echo "deb https://dist.crystal-lang.org/apt crystal main" | sudo tee /etc/apt/sources.list.d/crystal.list
sudo apt-get update
Install
Once the repository is configured you’re ready to install Crystal:

sudo apt install crystal
The following packages are not required, but recommended for using the respective features in the standard library:

sudo apt install libssl-dev  #  for using OpenSSL    
sudo apt install libxml2-dev     #  for using XML    
sudo apt install libyaml-dev     #  for using YAML   
sudo apt install libgmp-dev      #  for using Big numbers   
sudo apt install libz-dev        #  for using crystal play
