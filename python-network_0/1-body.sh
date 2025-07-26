#!/bin/bash
# This script sends a GET request to a given URL and displays the body only if the response status is 200.
[ "$(curl -s -o /dev/null -w "%{http_code}" -L "$1")" -eq 200 ] && curl -s -L "$1"
