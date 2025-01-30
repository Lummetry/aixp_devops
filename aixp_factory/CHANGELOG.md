# Changelog


## 1.2.45 - 2025-01-30
  - extra packages

--------------------------------------------------------------------------

## 1.2.44 - 2025-01-23
  - auto-warmup config
  - added multiple packages
  - custom NTP server configuration


## 1.2.40 - 2025-01-21
  - EE_MQTT_SUBTOPIC fix


## 1.2.38 - 2024-11-28
  - work on docker login & internal cr

## 1.2.37 - 2024-11-26
  - added pip support for newer Debian distr with py 3.12+
  - added snap support for nvtop
  - some logging stuff
  - fixed symbolic link for streams


## 1.2.30 - 2024-10-04
  - added self-check-ee-01 to admin pipeline


## 1.2.29 - 2024-09-31
  - add ~/streams symlink to pipeline folder
  - update restart time

## 1.2.27 - 2024-09-24
  - default warmup
  - other 1.2.25 changes
  - maintenance restart at 40+ hours


## 1.2.24 - 2024-09-18
  - extra lms container rm


## 1.2.23 - 2024-09-16
  - fix LMS services
  - update monitor schedule


## 1.2.21 - 2024-09-05
  - variable to configure image prune


## 1.2.20 - 2024-08-26
  - fixed admin pipeline destination folder



## 1.2.19 - 2024-08-23
  - added aixp_MINIO_MAX_SERVER_QUOTA 


## 1.2.18 - 2024-08-20
  - removed aixp_UPDATE_MONITOR_START/END
  - added aixp_UPDATE_MONITOR_SCHEDULE


## 1.2.17 - 2024-08-19
  - aixp_ADD_ORIGINAL_IMAGE
  - ADD_ORIGINAL_IMAGE blocked


## 1.2.15 - 2024-08-14
  - added jtop


## 1.2.14 - 2024-08-12
  - added ntp and htop to prerequisites
  - added aixp_DEBUG_LOG_PAYLOADS
  - added "MAX_BATCH_FIRST_STAGE" : {{ aixp_MAX_BATCH_FIRST_STAGE | default(8) }}


## 1.2.10 - 2024-08-08
  - LMS fixes
  - docker pull limit


## 1.2.7 - 2024-08-07
  - aixp_UPDATE_MONITOR_REBOOT_ON_RESTART

## 1.2.6 - 2024-08-05
  - /etc/hosts fix


## 1.2.3 - 2024-08-02
  - pipeline config (admin_pipeline)



## 1.1.1 - 2024-07-31
  - config only deployment using `--skip` option


## 1.0.12 - 2024-07-30
  - fix #2 for config only deployment
  - removed image prune for the moment from service template


## 1.0.5 - 2024-07-20
  - fix for config only deployment


## 1.0.3 - 2024-07-11
  - added `-m {{ aixp_container_memory_limit | default('30GB') }}


## 1.0.2 - 2024-07-09
  - added `run-config.sh` for config only deployment
  - installer now works also on Red Hat


## 0.9.27 - 2024-07-02
  - ansible galaxy fix



## 0.9.24 - 2024-06-18
  - mqtt certs


## 0.9.19 - 2024-06-17
  - fix ee auto update 
  - fixed StartLimitBurst=0 and other issues

## 0.9.17 - 2024-06-13
  - LMS
  - dev mode


## 0.9.15 - 2024-06-12
  - TLS


## 0.9.13 - 2024-06-10
  - new env vars  
  - version check


## 0.9.7 - 2024-06-05
  - custom images
  - gpus
  - force template overwrite
  - better service handling
  - various fixes


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
 - added naeural_client tests
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
