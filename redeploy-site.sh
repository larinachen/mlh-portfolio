#!/bin/bash

# kill existing tmux session
tmux kill-ses -t mlh-portfolio
# cd into project folder (~/mlh-portfolio)
cd ~/mlh-portfolio
# make sure site has the lastest version
git fetch && git reset origin/main --hard
# enter virtual environment
source python3-virtualenv/bin/activate
# install dependencies
pip install -r requirements.txt
# start tmux and run flask server
tmux new -d -s mlh-portfolio 'flask run --host=0.0.0.0'