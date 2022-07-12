#!/bin/bash


# cd into project folder (~/mlh-portfolio)
cd ~/mlh-portfolio
# make sure site has the lastest version
git fetch && git reset origin/main --hard
# spin containers down
docker compose -f docker-compose.prod.yml down
# spin containers up
docker compose -f docker-compose.prod.yml up -d --build

