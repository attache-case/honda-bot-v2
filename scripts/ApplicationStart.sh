#!/bin/sh

# pkill -KILL -f "python main.py"
cd /home/ec2-user/honda-bot-v2/
source ~/py-envs/honda-bot/bin/activate
pip install -r requirements.txt
nohup python main.py &