#!/bin/sh

# ssm parameter-store settings
INSTANCE_ID=$(curl 169.254.169.254/latest/meta-data/instance-id)
echo INSTANCE_ID=$INSTANCE_ID
ZONE=$(curl 169.254.169.254/latest/meta-data/placement/availability-zone)
echo ZONE=$ZONE
REGION=$(echo ${ZONE/%?/})
echo ZONE=$ZONE
APP_NAME=$(aws --region ${REGION} ec2 describe-instances --instance-ids ${INSTANCE_ID} --query "Reservations[0].Instances[0].Tags[?Key=='Name'].Value" --output text)
echo APP_NAME=$APP_NAME
APP_ENV=$(aws --region ${REGION} ec2 describe-instances --instance-ids ${INSTANCE_ID} --query "Reservations[0].Instances[0].Tags[?Key=='Env'].Value" --output text)
echo APP_ENV=$APP_ENV
FILENAME="/home/ec2-user/.env"
echo FILENAME=$FILENAME

SSM_PARAMS=$(aws --region ${REGION} ssm get-parameters-by-path --path "/${APP_NAME}/${APP_ENV}" --with-decryption)
echo SSM_PARAMS=$SSM_PARAMS
for params in $(echo $SSM_PARAMS | jq -r '.Parameters[] | .Name + "=" + .Value'); do
    echo ${params##*/}
done > ${FILENAME}

sudo rm -rf /home/ec2-user/honda-bot-v2/
sudo mkdir /home/ec2-user/honda-bot-v2/