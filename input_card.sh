#!/bin/bash
xdotool search --name Kiosk windowfocus --sync
xdotool key --clearmodifiers alt+i
xdotool type "$1"
xdotool key Return
