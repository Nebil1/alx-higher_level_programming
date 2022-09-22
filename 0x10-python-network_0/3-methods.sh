#!/bin/bash
# show all possible methods
curl -sI -X OPTIONS $1 | grep 'Allow:' | cut -d ' ' -f2-
