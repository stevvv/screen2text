import pyscreenshot as ImageGrab
import pytesseract as pt
from PIL import Image
import time
import sys

def main():
    print('capturing in 5 seconds...')
    time.sleep(5)
    # grab fullscreen
    im = ImageGrab.grab()
    custom_oem_psm_config = r'--psm 3'
    # print('SCREEN CONTENT BELOW : \n')
    print('Processing...')
    annotations = pt.image_to_string(im, lang='eng', config=custom_oem_psm_config)
    if len(annotations) > 0:
        # text = annotations[0].description
        with open("Output.txt", "w") as text_file:
            text_file.write("Detected Text On-Screen:\n {0}".format(annotations))
    else:
        text = "Couldn't understand.. try again \n"
        print(text)
    print('Finished\nCheck the Output.txt')

main()
