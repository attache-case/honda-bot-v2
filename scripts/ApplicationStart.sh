pkill -KILL -f "python main.py"
cd /home/ec2-user/honda-bot-v2/
pip3 install -r requirements.txt
nohup python src/main.py &