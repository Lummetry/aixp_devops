# Collection for AiXp edge nodes deployment factory


## Description

This sub-repository contains all the DevOps related files for the on-prem fleet deployments of AiXpand project.


## Logistics

The repository contains a `build.sh` script that is used to manually build & push the collection however it should not be usually used as there is a GitHub action that builds & pushes the collection automatically on every commit. The GitHub action is triggered only when modifications are made to the `aixp_factory` directory and will only build and push the collection if the version in the `aixp_factory/galaxy.yml` file is higher than the version in the Ansible Galaxy repository.