#!/bin/bash

# Activity 1: Displaying messages
who
date
$HOME
$USER

# Activity 2: Working with positional arugments
YOUR_NAME=$1
YOUR_MONEY=$2
echo "My name is $1 and I have \$$2 in my wallet."

# Activity 3: Math time
mathvar1=($[1+5])
mathvar2=($[mathvar1*20])
mathvar3=10
mathvar4=($[mathvar1*(mathvar2+mathvar3)])
echo "Variable 1 is $mathvar1. Variable 2 is $mathvar2. Using $mathvar3 for Variable 3, our final Variable 4 is $mathvar4."

# Activity 4: More math. Working with floating-point solution

floating=$(echo "scale=3; 4.5/1.7"|bc)
echo "Our floating variable is $floating."
