#!/bin/bash
# send data POST method
curl -s -X POST -d 'email=test@gmail.com&subject=I will always be here for PLD' $1
