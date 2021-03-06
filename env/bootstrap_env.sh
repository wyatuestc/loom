#!/bin/bash

# Setup keys
cp keys/id_rsa ~/.ssh/
cat keys/id_rsa.pub >> ~/.ssh/authorized_keys

# Ensure that ssh works without asking for Authenticity to be accepted
## TODO: for hosts: ssh-keyscan $host >> ~/.ssh/known_hosts
SERVERS="node-0 node-1 localhost 127.0.0.1 10.10.1.1 10.10.1.2 10.10.101.1 10.10.101.2 10.10.102.1 10.10.102.2"
for h in $SERVERS; do
    ssh-keyscan -H $h >> ~/.ssh/known_hosts
done

# Setup env variable for the git repo
cd ..
LOOM_HOME=`pwd`
echo "export LOOM_HOME=$LOOM_HOME" >> ~/.bashrc

# Install ansible
sudo apt-get install -y software-properties-common
sudo apt-add-repository -y ppa:ansible/ansible
sudo apt-get update
sudo apt-get install -y ansible

# Download OFED and MFT and DPDK
#wget http://content.mellanox.com/ofed/MLNX_OFED-4.1-1.0.2.0/MLNX_OFED_LINUX-4.1-1.0.2.0-ubuntu16.04-x86_64.tgz
#wget http://www.mellanox.com/downloads/MFT/mft-4.7.0-42-x86_64-deb.tgz
#wget http://fast.dpdk.org/rel/dpdk-17.08.tar.xz

# Setup CloudLab HDs for storage
#sudo mkfs -t ext4 -F /dev/sda4
#sudo mkdir /scratch
#sudo mount /dev/sda4 /scratch
#sudo chmod -R 777 /scratch
