#!/bin/bash
WID=`xdotool search "Chromium" | head -1`
xdotool windowactivate --sync $WID
xdotool key --clearmodifiers alt+i
xdotool type "$1"
xdotool key Return
