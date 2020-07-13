from halo import FaceRecognition
from sanic import Sanic
from sanic.response import json

# Initialize the model
FR = FaceRecognition()

app = Sanic("Core microservice")


@app.route("/", methods=["POST"])
async def predict(request):
    args = request.json
    img = args["img"]

    pred, score = FR.predict(img)
    return json({"pred": pred, "score": score})


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=9000)

