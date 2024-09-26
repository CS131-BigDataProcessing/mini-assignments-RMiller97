#!/bin/bash

# Positional Argument
AGE=$1

# Nested if Script
if [ $AGE -lt 13 ]; then
	echo "child"
elif [ $AGE -lt 20 ]; then
	echo "teen"
elif [ $AGE -lt 65 ]; then
	echo "adult"
else
	echo "elderly"
fi

