# Collection for AiXp edge nodes deployment factory

## Description

This sub-repository contains all the DevOps related files for the on-prem fleet deployments of AiXpand project.


## Installation

To install the collection, create a folder such as `edge-deploy` and within create a `install.sh` as follows:

```bash
mkdir edge-deploy
cd edge-deploy
touch install.sh
```

Then paste the following into the `install.sh` file:

```bash
#!/bin/bash
curl -L "https://raw.githubusercontent.com/Lummetry/aixp_devops/main/aixp_factory/other/install-factory.sh?$RANDOM" -o install-factory.sh
chmod +x install-factory.sh
./install-factory.sh
rm install-factory.sh
```

Then run the `install.sh` script:

```bash
chmod +x install.sh
./install.sh
```


## Logistics

The repository contains a `build.sh` script that is used to manually build & push the collection however it should not be usually used as there is a GitHub action that builds & pushes the collection automatically on every commit. The GitHub action is triggered only when modifications are made to the `aixp_factory` directory and will only build and push the collection if the version in the `aixp_factory/galaxy.yml` file is higher than the version in the Ansible Galaxy repository.