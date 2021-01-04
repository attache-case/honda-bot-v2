#!/bin/sh

# ssm parameter-store settings
INSTANCE_ID=$(curl 169.254.169.254/latest/meta-data/instance-id)
echo INSTANCE_ID=$INSTANCE_ID
ZONE=$(curl 169.254.169.254/latest/meta-data/placement/availability-zone)
echo ZONE=$ZONE
REGION=$(echo ${ZONE/%?/})
echo REGION=$REGION
APP_NAME=$(aws --region ${REGION} ec2 describe-instances --instance-ids ${INSTANCE_ID} --query "Reservations[0].Instances[0].Tags[?Key=='Name'].Value" --output text)
echo APP_NAME=$APP_NAME
APP_ENV=$(aws --region ${REGION} ec2 describe-instances --instance-ids ${INSTANCE_ID} --query "Reservations[0].Instances[0].Tags[?Key=='Env'].Value" --output text)
echo APP_ENV=$APP_ENV

SSM_PARAMS=$(aws --region ${REGION} ssm get-parameters-by-path --path "/${APP_NAME}/${APP_ENV}" --with-decryption)
echo SSM_PARAMS=$SSM_PARAMS
for param_data in $(echo $SSM_PARAMS | jq -c '.Parameters[] | { Name, Value }'); do
    name=$(echo ${param_data} | jq -r '.Name')
    value=$(echo ${param_data} | jq -r '.Value')
    export ${name##*/}=${value}
done

cd /home/ec2-user/honda-bot-v2/
source ~/.venv/honda-bot/bin/activate
pip install -r requirements.txt
nohup python main.py &
