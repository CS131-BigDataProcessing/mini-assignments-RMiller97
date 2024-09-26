#!bin/bash

# Positional Argument
TEMP=$1

# if Statement

if [ $TEMP -gt 55 ]; then
	if [ $TEMP -lt 67 ]; then
		echo "cold"
	fi
fi
if [ $TEMP -lt 85 ]; then
	if [ $TEMP -gt 67 ]; then
		echo "nice"
	fi
fi
if [ $TEMP -gt 85 ]; then
	echo "hot"
fi
if [ $TEMP -lt 55 ]; then
	echo "freezing"
fi
