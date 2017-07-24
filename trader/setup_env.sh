#!/bin/sh
touch .env
echo '' > ./.env
echo user=$(whoami)  >> .env
echo uid=$(id -u $user) >> .env
echo gid=$(id -g $user) >> .env
echo https_proxy=$https_proxy >> .env
echo http_proxy=$http_proxy >> .env

