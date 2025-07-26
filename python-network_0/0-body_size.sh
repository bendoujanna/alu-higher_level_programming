#!/bin/bash
# This script takes a URL, sends a GET request using curl
curl -sL "$1" | wc -c
