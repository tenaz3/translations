import cv2
import sys
import pytesseract
import re
from os import walk


# DOCUMENTATION https://github.com/tesseract-ocr/tesseract/blob/master/doc/tesseract.1.asc
def analyse_image(image_path, config= "-l deu --oem 1 --psm 3"):
    # Read image from disk
    im = cv2.imread(image_path, cv2.IMREAD_COLOR)

    # Run tesseract OCR on image
    return pytesseract.image_to_string(im, config=config)


def save_text(image_path, text):
    name = re.match(r"(.+)\.+", image_path, re.M | re.I).group(1)

    f = open("out/" + name + ".txt", "w+")
    f.write(text)
    f.close()


if __name__ == "__main__":
    
    config = "-l deu --oem 1 --psm 3"

    agrs_size = len(sys.argv)
    image_list = []
    path = "/in/"

    _, _, image_list = next(walk(path))

    if agrs_size == 2:
        config = sys.argv[1]

    for image_path in image_list:
        if not image_path.startswith('.DS_Store'):
            text = analyse_image(path + image_path)
            save_text(image_path, text)
