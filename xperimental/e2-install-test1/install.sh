#!/bin/bash
mkdir -p ./factory
cd ./factory
curl -O https://raw.githubusercontent.com/Lummetry/aixp_devops/main/aixp_factory/install-factory.sh
chmod +x install-factory.sh
./install-factory.sh
