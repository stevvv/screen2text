import pyscreenshot as ImageGrab
from PIL import Image
import time
import sys
import requests

def main(lang):
    print('capturing in 5 seconds...')
    # print(lang)
    time.sleep(5)
    # grab fullscreen
    im = ImageGrab.grab()
    path = r'fullscreen.png'
    im.save(path)
    print('Processing...')
    url = 'https://stevtess.herokuapp.com/' + str(lang)
    files = {'file': open(path, 'rb')}
    # files = {'file': im}
    texts = requests.request('POST', url, files = files)
    if len(texts.text) > 0:
        # text = annotations[0].description
        with open("Output.txt", "w") as text_file:
            text_file.write("Detected Text On-Screen:\n {0}".format(texts.text))
    else:
        text = "Couldn't understand.. try again \n"
        print(text)
    print('Finished\nCheck the Output.txt')


if __name__ == "__main__":
    try:
        main(sys.argv[1])
    except:
        print('Kindly enter language argument \npython ss.py <eng/hin>')
