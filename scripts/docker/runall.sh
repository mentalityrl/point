#!/bin/bash

RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[0;33m'
CYAN='\033[0;36m'
NC='\033[0m' # No Color
#  --force-recreate --remove-orphans

for i in *; do
    if [ -d "${i}" ]; then
    cd ${i}
        if [ -f "docker-compose.yml" ]; then
            echo -e "${GREEN}Bringing up container's in $(pwd)${NC}"
            echo""
            docker-compose up -d
            echo""
            echo -e "${YELLOW}----------------------------------------------------------------------------${NC}"
            echo""
        else
            echo -e "${RED}No docker-compose.yml found in $(pwd); skipping directory${NC}"
            echo""
            echo -e "${YELLOW}----------------------------------------------------------------------------${NC}"
            echo""
        fi
    cd ..
    fi
done
