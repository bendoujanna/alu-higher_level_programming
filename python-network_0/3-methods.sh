#!/bin/bash
# Sends a HEAD request and displays allowed HTTP methods
curl -sI "$1" | grep -i "^Allow:" | cut -d' ' -f2-
