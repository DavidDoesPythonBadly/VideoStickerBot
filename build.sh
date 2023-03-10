#!/bin/bash


export DOCKER_BUILDKIT=1

docker build --pull --rm -f "Python/Dockerfile" -t videostickerbot:jwcmods "./"

docker comopse -f Python/docker-compose.yml up -d ==build
