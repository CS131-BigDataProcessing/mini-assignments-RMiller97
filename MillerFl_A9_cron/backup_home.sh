#!/bin/bash

# Define backup destination
BACKUP_DIR="$HOME/backups"
DATE=$(date +"%Y-%m-%d_%H-%M-%S")
BACKUP_FILE="$BACKUP_DIR/home_backup_$DATE.tar.gz"

# Create back up of home directory
tar -czf $BACKUP_FILE $HOME
