#!/bin/bash

inotifywait -q -m -e close_write -r --include=".*.md" . | while read -r path event filename;
do
	echo -e "\n\033[1;7;37mRunning Make because $path$filename was $event\033[0;1;0m"
	make
done;
