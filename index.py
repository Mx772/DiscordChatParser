# cv2.cvtColor takes a numpy ndarray as an argument 
import numpy as nm 
# Used to play sounds on alert
from playsound import playsound
# Image Reading
import pytesseract 
# Image Processing
import cv2 
import time
from PIL import ImageGrab 

############################################
# 			Config Settings
############################################

keywords = ['Time remaining']
pyTessPath = r'PATH'
boundingBox = (2840, -600, 3780, 2000)
sound = False
soundFile = 'G:\\Downloads\\1_second_tone.mp3'
pauseTime = 10
debug = False
greyScale = False

############################################
############################################

def imToString(): 
	pytesseract.pytesseract.tesseract_cmd = pyTessPath
	while(True): 
		cap = ImageGrab.grab(all_screens=True, bbox = boundingBox)
		tesstr = pytesseract.image_to_string(cap, lang ='eng')
		if greyScale:
			tesstr = pytesseract.image_to_string( 
					cv2.cvtColor(nm.array(cap), cv2.COLOR_BGR2GRAY), 
					lang ='eng')
		if debug:
			print("################# DEBUG: #################")
			cap.show()
			print(tesstr)
			print("################# END DEBUG #################")

		if any(word in tesstr for word in keywords):
			print("Found!")
			if sound:
				playsound(soundFile)
			print("Waiting 10 seconds")
			time.sleep(pauseTime)
		else:
			print("null")

imToString() 

    
