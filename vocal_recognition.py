import speech_recognition as sr

rec_vocal = sr.Recognizer()
micro = sr.Microphone()


def speech_rec(voice):
    with voice as source:
        print("Dites quelque chose")
        audio = rec_vocal.listen(source)
        print("Okay")

    try:
        text = rec_vocal.recognize_google(audio, language="fr-FR")
        print("Vous avez dit : " + text)
    except sr.UnknownValueError:
        print("L'audio n'as pas été compris")
    except sr.RequestError as e:
        print("Le service Google Speech API ne fonctionne plus" + format(e))
