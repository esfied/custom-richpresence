#!/bin/bash

while true; do
    if pgrep -f "/Applications/nameofapp.app" > /dev/null; then  # Path of the software you'll use to execute Rich Presence
        if ! pgrep -f "richpresence.py" > /dev/null; then
            cd /Users/nameofuser/custom-richpresence  # Location of the folder
            python3 richpresence.py &
        fi
    else
        if pgrep -f "richpresence.py" > /dev/null; then
            pkill -f "richpresence.py"
        fi
    fi
    sleep 10
done
