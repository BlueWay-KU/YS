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
### 3. Install pybluez
Reference: https://github.com/pybluez/pybluez
```
git clone https://github.com/pybluez/pybluez
cd pybluez
python setup.py build
python setup.py install
cd ..
```
### 4. Install bluepy
Reference: https://engineersportal.com/blog/2017/12/31/using-raspberry-pi-hm-10-and-bluepy-to-develop-an-ibeacon-mesh-network-part-1
```
git clone https://github.com/IanHarvey/bluepy.git
cd bluepy
python setup.py build
python setup.py install
cd ..
```
### 5. Install iBeacon-Scanner
```
git clone https://github.com/switchdoclabs/iBeacon-Scanner-
sudo chown pi iBeacon-Scanner-
sudo chgrp pi iBeacon-Scanner-
```
Test code
```
cd iBeacon-Scanner-
python testblescan.py
```
