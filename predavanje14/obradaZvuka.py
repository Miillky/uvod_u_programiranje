import time
import speech_recognition as sr
import webbrowser

tekst = 'nista'


def otvoriWeb(imeStranice):
    chrome_path = '/usr/bin/google-chrome %s'
    rijeci = imeStranice.split(" ")
    if not imeStranice == 'nista' and rijeci[0] == 'page':
        webbrowser.get(chrome_path).open("http://" + rijeci[1] + ".com")


r = sr.Recognizer()
m = sr.Microphone()
r.non_speaking_duration = 0.2
r.pause_threshold = 0.3
# r.energy_threshold = 50
with m as source:
    r.adjust_for_ambient_noise(source)
    # start listening in the background
    stopListening = r.listen_in_background(m, callback)
    # stop_listenting when called, stops background listening

while True:
    time.sleep(0.5)
    if tekst == 'texit':
        stopListening()
        break


# funkcija koja se poziva ukoliko listen_in_background detektira input mikrofona
def callback(recognizer, audio):
    global tekst
    print('NASA')
    # primljene audio podatke pokušamo prepoznati pomoći Google Speech Recognition
    try:
        tekst = recognizer.recognize_google(audio)
        print("Google Speech Recognition thinks you said " + tekst)
        otvoriWeb(tekst)
    except sr.UnknownValueError:
        print("Google Speech Recognition could not understand autio")
        tekst = 'nista'
    except sr.RequestError as e:
        print("Could not request results from Google Speech Recognition service; {}".format(e))
        tekst = 'nista'
