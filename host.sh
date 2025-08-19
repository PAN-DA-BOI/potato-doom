#!/bin/bash

if [ $# -eq 0 ]; then
    echo "Error: No flag provided. Usage: $0 [1|2|3|4]"
    exit 1
fi

case "$1" in
    1)
        map="maps/"
        ;;
    2)
        map="maps/"
        ;;
    3)
        map="maps/"
        ;;
    4)
        map="maps/"
        ;;
	5)
        map="maps/"
        ;;
	6)
        map="maps/"
		level= 
        ;;
    *)
        echo "Error: Invalid flag. Usage: $0 [1|2|3|4|5|6]"
        exit 1
        ;;
esac
zdoom -host 4 -file $map -deathmatch -warp $level