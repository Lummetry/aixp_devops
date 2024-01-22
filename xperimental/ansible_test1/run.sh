mkdir -p logs
ANSIBLE_FORCE_COLOR=true ansible-playbook deploy.yaml | tee "./logs/ansible_$(date +%Y_%m_%d__%H_%M).log"
