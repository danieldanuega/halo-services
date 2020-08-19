# Model Service

Configuration and settings for halo model deployment with Docker Tensorflow Serving docker.

## Usage

1. Before you run this please create `./models/deepface/<VER_NUM>` and put the halo model (tf model not keras model) inside the `<VER_NUM>` folder.
2a. Use docker-compose to run this model. (not yet supported)
2b. Use docker run `docker run --gpus all -t --name halo-serving -p 8500:8500 -p 8501:8501 -v $PWD/models/FbDeepFace:/models/deepface -v $PWD/serving.conf:/models/serving.conf tensorflow/serving:latest-gpu --model_config_file=/models/serving.conf --allow_version_labels_for_unavailable_models=true`
