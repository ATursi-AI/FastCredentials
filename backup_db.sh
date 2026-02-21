#!/bin/bash
DATE=$(date +%Y-%m-%d_%H%M)
BACKUP_DIR=~/backups
SOURCE_DB=~/fastcredentials/db.sqlite3

# 1. Create backup with timestamp
cp $SOURCE_DB $BACKUP_DIR/db_backup_$DATE.sqlite3

# 2. Delete backups older than 7 days to save space
find $BACKUP_DIR -name "db_backup_*.sqlite3" -mtime +7 -delete
