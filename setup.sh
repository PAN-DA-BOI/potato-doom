#!/bin/bash
wget "https://github.com/ZDoom/gzdoom/releases/download/g4.14.2/gzdoom_4.14.2_arm64.deb"
sudo apt-get install -y ./gzdoom_4.14.2_arm64.deb


if [ $# -eq 0 ]; then
    echo "Error: No flag provided. Usage: $0 [1|2|3|4]"
    exit 1
fi

INTERFACE="eth0"
NETMASK="255.255.255.0"
GATEWAY="1.1.1.1"

case "$1" in
    1)
        IP_ADDRESS="1.1.1.101"
		rm potato2.py
		rm potato3.py
		rm potato4.py
        ;;
    2)
        IP_ADDRESS="1.1.1.102"
		rm potato1.py
		rm potato3.py
		rm potato4.py
        ;;
    3)
        IP_ADDRESS="1.1.1.103"
		rm potato2.py
		rm potato1.py
		rm potato4.py
        ;;
    4)
        IP_ADDRESS="1.1.1.104"
		rm potato2.py
		rm potato3.py
		rm potato1.py
        ;;
    *)
        echo "Error: Invalid flag. Usage: $0 [1|2|3|4]"
        exit 1
        ;;
esac

sudo ip addr flush dev $INTERFACE
sudo ip link set $INTERFACE down
sudo ip addr add $IP_ADDRESS/$NETMASK dev $INTERFACE
sudo ip link set $INTERFACE up
sudo ip route add default via $GATEWAY
echo "IP address set to $IP_ADDRESS on $INTERFACE"


