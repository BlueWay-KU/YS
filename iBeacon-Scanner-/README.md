## RPi iBeacon scanner
### 1. Make workspace
```
sudo -s
mkdir Bluetooth
cd Bluetooth
```
### 2. Install dependecies
```
apt-get install git libbluetooth-dev libboost-python-dev libboost-thread-dev libglib2.0-dev bluez bluez-hcidump python-bluez build-essential
```
Turn on the bluetooth module
```
hciconfig hci0 up
```
### 3. Install iBeacon-Scanner
```
git clone https://github.com/switchdoclabs/iBeacon-Scanner-
sudo chown pi iBeacon-Scanner-
sudo chgrp pi iBeacon-Scanner-
```
testblescan.py를 사용하기 편하게 바꿔놓은 코드 = scan.py
