#!/bin/bash
# This script takes a URL, sends a GET request using curl, 
# and displays the size of the response body in bytes.


curl -sL "$1" | wc -c
