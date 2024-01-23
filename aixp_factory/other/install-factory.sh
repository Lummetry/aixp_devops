#!/bin/bash

log_with_color() {
    local text="$1"
    local color="$2"
    local color_code=""

    case $color in
        red)
            color_code="0;31" # Red
            ;;
        green)
            color_code="0;32" # Green
            ;;
        blue)
            color_code="0;34" # Blue
            ;;
        yellow)
            color_code="0;33" # Yellow
            ;;
        light)
            color_code="1;37" # Light (White)
            ;;
        *)
            color_code="0" # Default color
            ;;
    esac

    echo -e "\e[${color_code}m${text}\e[0m"
}

# Function to install Python
install_python() {
  log_with_color "Installing Python..." 
  sudo apt-get update
  sudo apt-get install python3
}

# Function to install Pip
install_pip() {
  log_with_color "Installing Pip..."  
  sudo apt-get install python3-pip
}

# Function to install Ansible
install_ansible() {
  log_with_color "Installing Ansible..." 
  sudo apt-get update
  sudo apt-get install ansible
}

log_with_color "Starting setup v.0.1.0 ..." green

# Create a directory for the factory
mkdir -p factory
cd factory


# Check if Python is installed
if ! command -v python3 &> /dev/null
then
    install_python
else
    log_with_color "Python is already installed."  green
fi

# Check if Pip is installed
if ! command -v pip3 &> /dev/null
then
    install_pip
else
    log_with_color "Pip is already installed." green
fi

# Check if Ansible is installed
if ! ansible --version &> /dev/null
then
    install_ansible
else
    log_with_color "Ansible is already installed." green
fi

# Install Ansible Collection
log_with_color "Installing Ansible Collection: aidamian.aixp_factory" light
ansible-galaxy collection install aidamian.aixp_factory --force --no-cache --clear-response-cache

# Check if the collection is successfully installed 
if [ $? -eq 0 ]; then
    log_with_color "Ansible Collection: aidamian.aixp_factory is successfully installed." green
else
    log_with_color "Ansible Collection: aidamian.aixp_factory is not installed." red
    exit 1
fi

# Define the path to the collection
collection_path="$HOME/.ansible/collections/ansible_collections/aidamian/aixp_factory"

# Copy .hosts.yml from collection to current directory as hosts.yml if it does not exist
if [ ! -f "./hosts.yml" ]; then
    log_with_color "Copying .hosts.yml from the collection to hosts.yml" blue
    cp "${collection_path}/other/.hosts.yml" ./hosts.yml
else
    log_with_color "hosts.yml already exists. Not copying." blue
fi

log_with_color "Please modify the hosts.yml file with your own values." yellow


# Copy ansible.cfg from collection to current directory as ansible.cfg - overwrite if it exists
if [ ! -f "./ansible.cfg" ]; then
    log_with_color "Copying ansible.cfg from the collection..."
    cp "${collection_path}/other/ansible.cfg" ./ansible.cfg
else
    log_with_color "ansible.cfg already exists. Overwriting..."
    cp "${collection_path}/other/ansible.cfg" ./ansible.cfg
fi


# Copy run.sh from collection to current directory - overwrite if it exists
if [ ! -f "./run.sh" ]; then
    log_with_color "Copying run.sh from the collection..."
    cp "${collection_path}/other/run.sh" ./run.sh
else
    log_with_color "run.sh already exists. Overwriting..."
    cp "${collection_path}/other/run.sh" ./run.sh
fi


# Create empty key.pem file if it does not exist
if [ ! -f "./key.pem" ]; then
    log_with_color "Creating empy key.pem file"
    touch key.pem    
    log_with_color "Please write a SK in the key.pem file" yellow
else
    log_with_color "key.pem already exists. Not creating." green
fi

chmod 600 key.pem

# Copy the playbook deploy.yml from the collection `other` folder to current directory if it does not exist
if [ ! -f "./deploy.yml" ]; then
    log_with_color "Copying deploy.yml from the collection..."
    cp "${collection_path}/other/deploy.yml" ./deploy.yml
else
    log_with_color "deploy.yml already exists. Not copying."
fi

log_with_color "Setup Completed." green
