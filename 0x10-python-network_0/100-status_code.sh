#!/bin/bash
# status Code
curl -so /dev/null -w '%{http_code}' $1
