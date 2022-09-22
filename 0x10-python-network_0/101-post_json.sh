#!/bin/bash
# Send JSON data
curl -s -d "@$2" -X POST -H 'Content-Type: application/json' $1
