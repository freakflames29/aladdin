# python bot
import time
from time import sleep
import pywhatkit as pw
import wikipedia as wiki
import webbrowser as wb
import playsound as ps
from program_open import open
from pywhatkit.core.exceptions import InternetException
import re
import joke
import weather


class Aladdin:

    def __init__(self):
        self.user_input = ""
        self.songPlayed = False

    def checkurl(self, string):
        pass

    # buffer
    def buffer(self):

        for i in range(3):
            print("Aladdin typing.", end="\r")
            sleep(0.1)
            print("Aladdin typing..", end="\r")
            sleep(0.1)
            print("Aladdin typing...", end="\r")
            sleep(0.1)
            print("Aladdin typing.  ", end="\r")

    # play on youtube
    def playit(self, song):
        print("\033[1;36mAladdin:\033[1;39m", "Song is going to play on youtube")

        pw.playonyt(song)

    # google search
    def web(self, query):

        url = "https://www.google.com/search?q=" + query
        wb.open(url)
        return "Searching in google..."

    # sing
    def sing(self):
        self.buffer()
        print("\033[1;36mAladdin:\033[1;39m", "Alright ! Let's sing")
        ps.playsound("/home/sourav/Music/sing.mp3")
        self.songPlayed = True

    def tell_me_a_joke(self):
        self.buffer()
        print("\033[1;36mAladdin:\033[1;39m", joke.joke(), "😂️")
        sleep(3)
        ps.playsound("/home/sourav/Documents/aladdin/blob/hahaha.mp3")

    def weather(self):
        self.buffer()
        info=weather.get_weather()
        print("\033[1;36mAladdin:\033[1;39m", "The weather is")
        print("Temperature:", info['Temperature'])
        print("Humidity:", info['Humidity'])
        print("Weather:", info['Weather'])
        print("Feels like:", info['Feels like'])

    def reply(self):
        if "hello" in self.user_input or "hi" in self.user_input:
            return "Hello! how are you today?"

        elif "how are you" in self.user_input:
            return "I am fine, thanks for asking"

        elif "i am good" in self.user_input:
            return "I am glad to hear that you are good in this hard time !"

        elif "i am fine" in self.user_input:
            return "I am glad to hear that you are good in this hard time !"

        elif "your name" in self.user_input or "who are you" in self.user_input:
            return "My name is Aladdin.I am your friend"

        elif "my name is" in self.user_input:
            name = self.user_input.replace("my name is", "")
            return "Nice to meet you!" + name

        elif "play the song" in self.user_input or "play song" in self.user_input:

            if "play the song" in self.user_input:
                song = self.user_input.replace("play the song", "")
            else:
                song = self.user_input.replace("play song", "")

            self.playit(song)
            return ""

        elif "play" in self.user_input:
            song = self.user_input.replace("play ", "")
            self.playit(song)
            return ""

        elif "what is" in self.user_input:
            query = self.user_input  # .replace("what is", "")
            return self.web(query)

        elif "sing for me" in self.user_input or "sing a song" in self.user_input:
            self.sing()
            return ""

        elif "what can you do" in self.user_input or "what can you do for me" in self.user_input or "show me your skills" in self.user_input:
            return "I can search for you in google and play songs on youtube,i can sing for you too"

        elif "you are awesome" in self.user_input or "you are cool" in self.user_input or "you are the best" in self.user_input:
            return "Thank you for saying that"

        elif "it was good" in self.user_input or "it was nice" in self.user_input or "it was fun" in self.user_input or "it was awesome" in self.user_input:
            if self.songPlayed:
                self.songPlayed = False
                return "Thank you thank you"
            else:
                return "I am sorry I did not play anything"
        elif "open" in self.user_input:
            # isurl=self.checkurl(self.user_input) # TODO: check if url
            cmd = self.user_input.replace("open", "")
            open(cmd)
            return ""
        elif "tell me a joke" in self.user_input:
            self.tell_me_a_joke()
            return ""

        elif "how is the weather" in self.user_input or "weather" in self.user_input or "weather today" in self.user_input or "how is the day" in self.user_input or "forecast" in self.user_input:
            self.weather()
            return ""

        else:
            return "Sorry, I didn't get that"

    # user input
    def capt(self):
        while True:
            inp = input("\033[1;33mYou:\033[1;39m")
            self.user_input = inp.casefold()
            if self.user_input == "exit" or self.user_input == "bye":
                if self.user_input == "bye":
                    print("\033[1;36mAladdin:\033[1;39m", "Bye! See you soon")
                break
            res = self.reply()

            if res != "":
                self.buffer()
                print("\033[1;36mAladdin:\033[1;39m", res)


ob = Aladdin()
ob.capt()
