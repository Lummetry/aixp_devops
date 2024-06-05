# Changelog

## 0.9.2 - 2024-06-05
  - custom images
  - gpus
  - force template overwrite
  - various fixes

--------------------------------------------------------------------------

## 0.8.30 - 2024-05-31
  - fix custom CRs


## 0.8.29 - 2024-05-24
  - insecure cr accepted


## 0.8.28 - 2024-05-22
  - added custom container registry

## 0.8.25 - 2024-05-21
  - added hosts and lm-sensors


## 0.8.15 - 2024-05-17
  - fixed vars


## 0.8.13 - 2024-05-14
  - fixed service status

## 0.8.12 - 2024-05-09
  - new release manager update


## 0.8.11 - 2024-04-30
  - show aixp_app_version tag 
  - pip, docker package also for Jetson

## 0.8.6 - 2024-04-25
  - check for target env


## 0.8.5 - 2024-04-23
  - support for Nvidia Jetson

## 0.7.28 - 2024-04-15
  - fixed version in default config for Hyfy E2

## 0.7.27 - 2024-04-12
  - hot-fix: reverted to timezone volume for the moment

## 0.7.26 - 2024-04-11
  - added docker package

## 0.7.25 - 2024-03-28
  - removed timezones

## 0.7.24 - 2024-03-27
  - fix target envs
  - added QA env

## 0.7.22 - 2024-03-13
  - show.sh with params

## 0.7.21 - 2024-03-12
  - fixed service to allow restart
  - url names

## 0.7.17 - 2024-03-04
 - added GPU-only setup 
 - README.md
 - various changes in install scripts

## 0.7.12 - 2024-03-04
 - hold GPU

## 0.7.11 - 2024-03-02
 - no spaces allowed in host names

## 0.7.10 - 2024-03-01
 - verbosity
 - fixed os check
 - fixed apt upgrade

## 0.7.6 - 2024-02-27
 - non-mandatory Snap install

## 0.7.5 - 2024-02-26
 - fixed doker prune

## 0.7.4 - 2024-03-01
 - added lsb_release

## 0.7.3 - 2024-02-02
 - fixed pip install

## 0.7.2 - 2024-02-02
 - removed Py3.10 required install
 - working end-to-end tests
 - refactor & cleanup

## 0.5.27 - 2024-02-01
 - better python/pip install tasks

## 0.5.21 - 2024-01-29
 - added plugin utils
 - finished aixp connection tests

## 0.5.4 - 2024-01-28
 - prepared module and action scripts
 - added PyE2 tests
 - fix Nvidia container test

## 0.4.16 - 2024-01-27
 - added test_action.py script

## 0.4.8 - 2024-01-26
 - control node precheck  
 - fixed aixp_app_version
 - docker login/pull issues
 - GitHub actions

## 0.4.3 - 2024-01-25
 - added Go install in pre-requisites
 - better .hosts.yml

## 0.4.2 - 2024-01-24
 - moved to new account
 - fix .env template
 - better run.sh script
 - fixed deploy
 - image loading & checking

## 0.2.0 - 2024-01-23
 - Added target envs: dev, pre, prod
 - added config templates including .env template
 - tests

## 0.0.1 - 2024-01-22
 - Initial release of the role.
