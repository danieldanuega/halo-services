# Halo Services

This service, contains 2 microservices:
- core_service
- model_service

core_service will talk to model_service with REST and then client will connect to core_service through message broker ImageZMQ for process the video stream in real time.
