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

log_with_color "###############################################################" green
log_with_color "########                                               ########" green
log_with_color "########                  AiXp Factory                 ########" green
log_with_color "########                                               ########" green
log_with_color "###############################################################" green

# check if factory folder exists
if [ ! -d "./factory" ]; then
    echo "factory folder does not exist. Please run install-factory.sh first."
    exit 1
fi
cd factory
mkdir -p logs
# check if logs folder contains ansible.log and rename it to ansible_YYYY_MM_DD__HH_MM.log
if [ -f "./logs/ansible.log" ]; then
    mv "./logs/ansible.log" "./logs/ansible_$(date +%Y_%m_%d__%H_%M).log"
fi
ANSIBLE_FORCE_COLOR=true ansible-playbook deploy.yml | tee "./logs/ansible.log"
