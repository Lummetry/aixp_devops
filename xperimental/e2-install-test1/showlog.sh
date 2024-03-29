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


# display the log in ./factory/logs/ansible.log
if [ -f "./factory/logs/ansible.log" ]; then
    log_with_color "Displaying ansible.log..." blue
    less -R ./factory/logs/ansible.log
else
    log_with_color "ansible.log does not exist." red
fi
