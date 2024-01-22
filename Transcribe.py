import speech_recognition as sr
import chatterbot
import os

Listener = sr.Recognizer()
mic = sr.Microphone()
Bot = chatterbot.ChatBot("ChatDot")

def recognize(recognizer, microphone):
    if not isinstance(recognizer, sr.Recognizer):
        raise TypeError("`recognizer` must be `Recognizer` instance")

    if not isinstance(microphone, sr.Microphone):
        raise TypeError("`microphone` must be `Microphone` instance")

    with microphone as source:
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source)

    response = {
        "success": True,
        "error": None,
        "transcription": None
    }

    try:
        response["transcription"] = recognizer.recognize_google(audio)
    except sr.RequestError:
        response["success"] = False
        response["error"] = "API unavailable"
    except sr.UnknownValueError:
        response["error"] = "Unable to recognize speech"

    return response

print("Starting...")

while True:
    Query = recognize(Listener, mic)["transcription"]
    
    Response = Bot.get_response(Query)
    print(Query)
    if Response == None:
        Response = input("Enter Text")
    os.system("gtts-cli '"+str(Response)+"' --output Latest.mp3")
    os.system("mpg321 Latest.mp3")
    

    print(Response)
