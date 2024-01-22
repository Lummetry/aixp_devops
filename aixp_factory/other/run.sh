mkdir -p logs
# check if logs folder contains ansible.log and rename it to ansible_YYYY_MM_DD__HH_MM.log
if [ -f "./logs/ansible.log" ]; then
    mv "./logs/ansible.log" "./logs/ansible_$(date +%Y_%m_%d__%H_%M).log"
fi
ANSIBLE_FORCE_COLOR=true ansible-playbook deploy.yml | tee "./logs/ansible.log"
