#!/bin/bash
wget "https://github.com/ZDoom/gzdoom/releases/download/g4.14.2/gzdoom_4.14.2_arm64.deb"
sudo apt-get install -y ./gzdoom_4.14.2_arm64.deb
# Check if a flag is provided
if [ $# -eq 0 ]; then
    echo "Error: No flag provided. Usage: $0 [1|2|3|4]"
    exit 1
fi


case "$1" in
    1)
        echo "Running script for flag 1 (1.1.1.101)"
        
        ;;
    2)
        echo "Running script for flag 2 (1.1.1.102)"
        
        ;;
    3)
        echo "Running script for flag 3 (1.1.1.103)"
        
        ;;
    4)
        echo "Running script for flag 4 (1.1.1.104)"
        
        ;;
    *)
        
        exit 1
        ;;
esac


