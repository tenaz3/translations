import cv2
import sys
import pytesseract
import re

if __name__ == '__main__':

  if len(sys.argv) < 2:
    print('Usage: python3 converter.py folder')
    sys.exit(1)
  
  imPath = sys.argv[1]
    
  # DOCUMENTATION https://github.com/tesseract-ocr/tesseract/blob/master/doc/tesseract.1.asc
  config = ('-l deu --oem 1 --psm 3')

  # Read image from disk
  im = cv2.imread(imPath, cv2.IMREAD_COLOR)

  # Run tesseract OCR on image
  text = pytesseract.image_to_string(im, config=config)
  matches = re.match( r'\/in\/(.+)\.+', imPath, re.M|re.I)

  name = matches.group(1)

  f = open('out/' + name + ".txt","w+")
  f.write(text)
  f.close()
