#!/bin/bash

# issue POST request
curl --request POST http://172.25.240.1:5000/api/timeline_post -d 'name=TestUser7&email=Email1@email.io&content=mystery'

# issue GET request
curl http://172.25.240.1:5000/api/timeline_post
