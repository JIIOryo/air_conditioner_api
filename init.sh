
# pigpio
sudo apt install python3-pigpio -y

# pigpiod
sudo systemctl enable pigpiod
sudo systemctl start pigpiod

# download irrp.py
curl http://abyz.me.uk/rpi/pigpio/code/irrp_py.zip | zcat > irrp.py

# pip install
pip3 install -r requirements.txt

# generate config file
cp config.json.template config.json
