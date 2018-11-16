yum install mosquitto -y

systemctl enable mosquitto

systemctl start mosquitto

pip install --upgrade pip

pip install paho-mqtt
