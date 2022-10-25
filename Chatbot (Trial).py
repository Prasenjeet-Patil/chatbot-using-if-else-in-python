from gtts import gTTS
from playsound import playsound
import datetime
import webbrowser

x = datetime.datetime.now()
r1 = x.strftime("%d")
r2 = x.strftime("%B")
r3 = x.strftime("%Y")
r4 = x.strftime("%A")

r5 = x.strftime("%I")
r6 = x.strftime("%M")
r7 = x.strftime("%p")

print('Hi, How can I help you?')
while (True):
    que = input("Enter Something: ")
    if 'hello' in que:
        res = "Hello there! How can I help you!"
        audio1 = 'speech1.mp3'
        sph1 = gTTS(text = res, lang = 'en', slow=False)
        sph1.save(audio1)
        playsound(audio1)
    elif 'date' in que:
        audio2 = 'speech2.mp3'
        sph2 = gTTS(text = "Today's day and date is: " + str(r4) + " " + str(r1) + " " + str(r2) + " " + str(r3), lang = 'en', slow=False)
        sph2.save(audio2)
        playsound(audio2)
    elif 'time' in que:
        audio3 = 'speech3.mp3'
        sph3 = gTTS(text = "Your current time is: " + str(r5) + " " + str(r6) + " " + str(r7), lang = 'en')
        sph3.save(audio3)
        playsound(audio3)
    elif 'girlfriend' in que:
        audio4 = 'speech4.mp3'
        sph4 = gTTS(text = "I'm sorry, but I'm currently engaged with your computer's Wi-fi. Thank you.", lang = 'en')
        sph4.save(audio4)
        playsound(audio4)
    elif 'boyfriend' in que:
        audio5 = 'speech5.mp3'
        sph5 = gTTS(text = "I'm currently engaged with your computer's Wi-fi!", lang = 'en')
        sph5.save(audio5)
        playsound(audio5)
    elif 'my name' in que:
        audio6 = 'speech6.mp3'
        sph6 = gTTS(text = "Your name is: Prasenjeet Patil", lang = 'en')
        sph6.save(audio6)
        playsound(audio6)
    elif 'your name' in que:
        audio7 = 'speech7.mp3'
        sph7 = gTTS(text = "My name is: Kitty!", lang = 'en')
        sph7.save(audio7)
        playsound(audio7)
    elif 'made' in que:
        audio8 = 'speech8.mp3'
        sph8 = gTTS(text = "I was created by Prasenjeet Patil", lang = 'en')
        sph8.save(audio8)
        playsound(audio8)
    elif 'open google' in que:
        audio9 = 'speech9.mp3'
        sph9 = gTTS(text = "Opening Google", lang = 'en')
        sph9.save(audio9)
        playsound(audio9)
        webbrowser.open('https://www.google.com/')
        print('Done!')
    elif 'open youtube' in que:
        audio10 = 'speech10.mp3'
        sph10 = gTTS(text = "Opening YouTube", lang = 'en')
        sph10.save(audio10)
        playsound(audio10)
        webbrowser.open('https://www.youtube.com/')
    elif 'music' in que:
        audio11 = 'speech11.mp3'
        sph11 = gTTS(text = "Playing Music on V L C Media Player", lang = 'en')
        sph11.save(audio11)
        playsound(audio11)
        webbrowser.open("D:/My Songs/My Favourite Songs/PHIR KABHI- Full SongM.S. DHONI -THE UNTOLD STORYArijit SinghSushant Singh Disha Patani.mp3")
    elif 'joke' in que:
        audio12 = 'speech12.mp3' 
        sph12 = gTTS(text = "Ha ha ha ha. I don't know a joke! L O L", lang = 'en')
        sph12.save(audio12)
        playsound(audio12)
    elif 'what can you do for me' in que:
        res = "Hello, Prasenjeet. Your text assistant is with you. I can't do much more because my manufacturing work is in progress. But I can do some basic things for you. For example: I can play a song for you and more!"
        audio13 = 'speech13.mp3'
        sph13 = gTTS(text = res, lang = 'en')
        sph13.save(audio13)
        playsound(audio13)
    elif 'borne' in que:
        audio14 = 'speech14.mp3'
        sph14 = gTTS(text = 'You were born on the 16th of April 2004', lang = 'en')
        sph14.save(audio14)
        playsound(audio14)
    elif 'my birthday' in que:
        playsound('D:/My Songs/Assistant Songs/Happy Birthday To You (Jingle).mp3')
        audio15 = 'speech15.mp3'
        sph15 = gTTS(text = "Happy Birthday to you, Enjoy your beautiful and special day...", lang = 'en')
        sph15.save(audio15)
        playsound(audio15)
    elif 'bye' in que:
        audio19 = 'speech19.mp3'
        sph19 = gTTS(text = "OK bye... We will meet soon. Have a nice day!", lang = 'en')
        sph19.save(audio19)
        playsound(audio19)
        break
    else:
        audio20 = 'speech20.mp3'
        sph20 = gTTS(text = "I didn't understood what you are saying. Please type it again.", lang = 'en')
        sph20.save(audio20)
        playsound(audio20)