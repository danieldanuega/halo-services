# Halo Services

This service, contains 2 microservices and 1 python client:
- core_service
- model_service
- client

core_service will talk to model_service with REST and then client will connect to core_service through REST for process the video stream in real time.

## Work Process

1. Client will take input from camera and capture each frame, then client preprocesses the captured frame before sending to core_service.
2. At core_service it passes the frame to model_service to be predicted its vector representation, after that model_service will compute the similarity between the frame and faces from database.
3. Core_service will return the name and the confident score to client.

## TODO

- Make client with JS(?)
- Create registration process at core_service.
- Reload the FaceRecognition object after registration process to update the database verification process.
