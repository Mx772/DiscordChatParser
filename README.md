# DiscordChatParser
 Reads Discord Chat and parses chat.

This was written for someone in a discord where giveaways would randomly pop-up. 
The use-case was that chat would go fast, and the user needed to be able to react within 30 seconds to a new giveaway being posted. 

The bot has now since changed, and the keyword can be changed to 'Ends':

![image](https://user-images.githubusercontent.com/9059161/135683423-565f3f02-aeb1-45e0-b0e4-dfa18f30770a.png)

It was previously based on the embed from:

https://github.com/jagrosh/GiveawayBot

![image](https://user-images.githubusercontent.com/9059161/135683462-83ffbf03-8acc-402e-8313-0c80076c3296.png)

## SETUP:

You must have:
- numpy
- playsound
- pytesseract
- cv2
- PIL

Note: Pytesseract can be downloaded from google: [Tesseract OCR](https://github.com/tesseract-ocr/tesseract)

### Config:

`keywords` array takes an array of strings to detect.

`pyTessPath` takes a path to your PyTesseract path. 

Ex: 
```
C:\Users\MyPC\Documents\Tesseract-OCR\tesseract.exe
```
`boundingBox` takes the coords of your screen to search. You can use ShareX to get coords using `region capture`. 

`sound` is a bool which will play sound or not when text is found. 

`soundFile` is a path to the sound file to play. 

`pauseTime` is the amount of seconds to wait after finding any keyword.

`debug` enables debug mode.

`greyScale` converts the image to greyscale which can help with OCR.

## DEBUG:
Enabling Debug mode will show the image captured by ImageGrab. 
It will also print the words found in the captured image. 