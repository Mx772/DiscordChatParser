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

Setup line 12 with keywords you wish to detect.

Setup line 17 with your path to pytesseract:

`pytesseract.pytesseract.tesseract_cmd =r'PATH'`

Setup line 22 with the coords of your monitor you wish for it to read. (You can use ShareX or read DEBUG below for more ways.)

`cap = ImageGrab.grab(all_screens=True, bbox =(2840, -600, 3780, 2000))`

Setup line 42 with your sound file you wish to play upon the word being found.
`playsound('G:\\Downloads\\1_second_tone.mp3')`

## DEBUG:

Uncommenting Lines 25-27 will make a pop-up of the captured screen. Useful for setting your boundary box.

Uncommenting line 37 will show you text in console of the parsed words. 

Uncommenting lines 32-34 will convert the photo to greyscale which can sometimes help word processing.
