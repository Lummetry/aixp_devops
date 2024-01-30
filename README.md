# AiXp main DevOps repository

## Description

This repository contains all the DevOps related files for the on-prem fleet deployments of AiXpand project.

## How-to

The following `install.sh` script will download and execute the installation script for the AiXpand Factory.

```bash
#!/bin/bash
curl -L "https://raw.githubusercontent.com/Lummetry/aixp_devops/main/aixp_factory/other/install-factory.sh?$RANDOM" -o install-factory.sh
chmod +x install-factory.sh
./install-factory.sh
rm install-factory.sh
```

Following the installation of the AiXpand Factory, the user must edit the `./factory/hosts.yml` that defines the target hosts and all required variables that will be used by the Ansible playbooks. Finally using `run.sh` script the user can execute the whole process.
The above `./install.sh` script can be called anytime to update the AiXpand Factory before running a `./run.sh` command

### [Todo list here](TODO.md)

## License

## Citation

```bibtex
@article{milik2023aixpand,
  title={AiXpand AI OS - Decentralized ubiquitous computing MLOps execution engine},
  author={
    Milik, Beatrice and 
    Saraev, Stefan and 
    Bleotiu, Cristian and 
    Lupaescu, Radu and 
    Hobeanu, Bogdan and 
    Damian, Andrei Ionut
  },
  journal={arXiv preprint arXiv:2306.08708},
  year={2023}
}
```

