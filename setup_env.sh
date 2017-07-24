#!/bin/sh
touch .env
echo '' > ./.env
echo uid=$(id -u $user) >> .env
echo gid=$(id -g $user) >> .env
