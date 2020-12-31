#!/bin/sh

# ssm parameter-store settings
IP_ADDRESS=$(hostname  -I | awk -F" " '{print $1}')
INSTANCE_ID=$(curl ${IP_ADDRESS}/latest/meta-data/instance-id)
ZONE=$(curl ${IP_ADDRESS}/latest/meta-data/placement/availability-zone)
REGION=$(echo ${ZONE/%?/})
APP_NAME=$(aws --region ${REGION} ec2 describe-instances --instance-ids ${INSTANCE_ID} --query "Reservations[0].Instances[0].Tags[?Key=='Name'].Value" --output text)
APP_ENV=$(aws --region ${REGION} ec2 describe-instances --instance-ids ${INSTANCE_ID} --query "Reservations[0].Instances[0].Tags[?Key=='Env'].Value" --output text)
FILENAME="/home/ec2-user/.env"

SSM_PARAMS=$(aws --region ${REGION} ssm get-parameters-by-path --path "/${APP_NAME}/${APP_ENV}" --with-decryption)
for params in $(echo $SSM_PARAMS | jq -r '.Parameters[] | .Name + "=" + .Value'); do
    echo ${params##*/}
done > ${FILENAME}

sudo rm -rf /home/ec2-user/honda-bot-v2/
sudo mkdir /home/ec2-user/honda-bot-v2/