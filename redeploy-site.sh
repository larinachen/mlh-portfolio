#!/bin/bash


# cd into project folder (~/mlh-portfolio)
cd ~/mlh-portfolio
# make sure site has the lastest version
git fetch && git reset origin/main --hard
# enter virtual environment
source python3-virtualenv/bin/activate
# install dependencies
pip install -r requirements.txt
# restart myportfolio.service
systemctl restart myportfolio

