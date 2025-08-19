#!/bin/bash

if [ $# -ne 2 ]; then
    echo "Error: Two arguments required. Usage: $0 [1|2|3|4] [1|2|3|4|5|6]"
    exit 1
fi

case "$1" in
    1)
        IP_ADDRESS="1.1.1.101"
        ;;
    2)
        IP_ADDRESS="1.1.1.102"
        ;;
    3)
        IP_ADDRESS="1.1.1.103"
        ;;
    4)
        IP_ADDRESS="1.1.1.104"
        ;;
    *)
        echo "Error: Invalid first argument. Usage: $0 [1|2|3|4] [1|2|3|4|5|6]"
        exit 1
        ;;
esac

case "$2" in
    1)
        map="maps/map1"
        ;;
    2)
        map="maps/map2"
        ;;
    3)
        map="maps/map3"
        ;;
    4)
        map="maps/map4"
        ;;
    5)
        map="maps/map5"
        ;;
    6)
        map="maps/map6"
        ;;
    *)
        echo "Error: Invalid second argument. Usage: $0 [1|2|3|4] [1|2|3|4|5|6]"
        exit 1
        ;;
esac

zdoom -join $IP_ADDRESS -file $map
