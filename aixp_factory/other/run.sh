# This script runs the ansible playbook deploy.yml and saves the output to a log file.
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

# extract the aidamian.aixp_factory collection version 
collection_name="aidamian.aixp_factory"
cover=$(ansible-galaxy collection list | grep "$collection_name" | awk '{print $2}')


log_with_color "      ###############################################################" green
log_with_color "      ########                                               ########" green
log_with_color "      ########            AiXp Factory v$cover               ########" green
log_with_color "      ########                                               ########" green
log_with_color "      ###############################################################" green

# check if factory folder exists
if [ ! -d "./factory" ]; then
    log_with_color "factory folder does not exist. Please run install-factory.sh first." red
    exit 1
fi

cd factory

curr_dir=$(pwd)

# print working directory
log_with_color "Working in $curr_dir" blue


# check if hosts.yml has been minimally configured
if grep -q 'ansible_user: ""' hosts.yml; then
    log_with_color "ansible_user is not set in hosts.yml" red
    exit 1
fi

mkdir -p logs
# check if logs folder contains ansible.log and rename it to ansible_YYYY_MM_DD__HH_MM.log
if [ -f "./logs/ansible.log" ]; then
    mv "./logs/ansible.log" "./logs/ansible_$(date +%Y_%m_%d__%H_%M).log"
fi
ANSIBLE_FORCE_COLOR=true ansible-playbook deploy.yml | tee "./logs/ansible.log"
