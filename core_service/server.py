from halo import FaceRecognition
from imagezmq import ImageHub


# Initialize the model
FR = FaceRecognition()

imageHub = ImageHub()

while True:
    print("Listening to client . . .")
    _, img = imageHub.recv_image()
    pred, score = FR.predict(img)
    result = pred + "/" + str(score)
    imageHub.send_reply(bytes(result, encoding="utf-8"))
