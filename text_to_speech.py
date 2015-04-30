import pyttsx

def tell (quest) :
    engine=pyttsx.init()
    engine.say(quest)
    engine.runAndWait()
