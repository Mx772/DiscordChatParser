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
keywords = ['Time remaining']

def imToString(): 

	# Local path to pytesseract exe
	# Example: C:\Users\MyPC\Documents\Tesseract-OCR\tesseract.exe
	pytesseract.pytesseract.tesseract_cmd =r'PATH'
	while(True): 

		# Set this to coords of your monitor to screenshot & Parse
		cap = ImageGrab.grab(all_screens=True, bbox =(2840, -600, 3780, 2000))

		# DEBUG | Uncommenting will pop-up screenshot of what is being captured.
		# cap.show()
		# cap2 = cv2.cvtColor(nm.array(cap), cv2.COLOR_BGR2GRAY)
		# cv2.imshow('test', cap2)
  
		tesstr = pytesseract.image_to_string(cap, lang ='eng')
  
		# DEBUG | Uncommenting will convert photo to greyscale which can aid in word-recognition.
		# tesstr = pytesseract.image_to_string( 
		# 		cv2.cvtColor(nm.array(cap), cv2.COLOR_BGR2GRAY), 
		# 		lang ='eng')

		# DEBUG | Uncommenting will print to console parsed words. 
		# print(tesstr)
  
		if any(word in tesstr for word in keywords):
			print("Found!")
			# Set to path of sound file.
			playsound('G:\\Downloads\\1_second_tone.mp3')
			print("Waiting 10 seconds")
			time.sleep(10)
		else:
			print("null")

# Calling the function 
imToString() 

    
