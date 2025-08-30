#!/bin/bash

# run docker and publish port 13000 to host
docker run -it --rm -p 1300:1300 \
    wottreng/object-detection:latest bash