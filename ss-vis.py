import os, io
from google.cloud import vision
import time
import pyscreenshot as ImageGrab

os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = r"ServiceAccountToken.json"
client = vision.ImageAnnotatorClient()

def main():
    print('Capturing in 5 seconds...')
    time.sleep(5)
    im = ImageGrab.grab()
    # save image file
    path = r'fullscreen.png'
    im.save(path)
    with io.open(path, 'rb') as image_file:
        content = image_file.read()
    #new
    image = vision.types.Image(content=content)
    print('Processing...')
    response = client.text_detection(image=image)
    annotations = response.text_annotations
    if len(annotations) > 0:
        text = annotations[0].description
        with open("Output.txt", "w") as text_file:
            text_file.write("Detected Text On-Screen:\n {0}".format(text))
    else:
        text = "Couldn't understand.. try again \n"
        print(text)
    print('Finished\nCheck the Output.txt')
main()
