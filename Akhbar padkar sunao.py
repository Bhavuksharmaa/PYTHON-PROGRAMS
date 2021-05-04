import requests
import json

def speak(str):
    from win32com.client import Dispatch
    speak = Dispatch("SAPI.SpVoice")
    speak.speak(str)

if __name__ == '__main__':
    news = requests.get("http://newsapi.org/v2/top-headlines?country=in&category=entertainment&apiKey=5158698934984adb8de5e3d7126017c9")
    content = news.text
    content_dict = json.loads(content)
    art = content_dict["articles"]
i = 1
for  d_oflist in art:
    speak(f"listion corefully news number {i} hunny")
    speak(d_oflist["title"])
    i= i+1

speak("thankyou hunny")