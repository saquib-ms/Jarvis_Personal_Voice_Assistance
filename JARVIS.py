import pyttsx3 #pip install pyttsx3
import speech_recognition as sr #pip install speechRecognition
import datetime
import wikipedia #pip install wikipedia
import webbrowser
import os
import smtplib

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
# print(voices[1].id)
engine.setProperty('voice', voices[0].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def takeCommand():
    #It takes microphone input from the user and returns string output

    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        r.energy_threshold = 100
        audio = r.listen(source,0,3)

    try:
        print("Recognizing...")    
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")

    except Exception as e:
        # print(e)    
        print("Say that again please...")  
        return "None"
    return query



# def sendEmail(to, content):
#     server = smtplib.SMTP('smtp.gmail.com', 587)
#     server.ehlo()bhbbjnknj
#     server.starttls()
#     server.login('youremail@gmail.com', 'your-password')
#     server.sendmail('youremail@gmail.com', to, content)
#     server.close()

if __name__ == "__main__":
    while True:
    # if 1:
        query = takeCommand().lower()
        if "wake up" in query:
            from GreetMe import greetMe
            greetMe()

            while True:
                query = takeCommand ().lower()
                if "hello" in query:
                    speak("Hello sir, how are you ?")
                elif "i am fine" in query:
                    speak("that's great, sir")
                elif "how are you" in query:
                    speak("Perfect, sir")
                elif "thank you" in query:
                    speak("you are welcome, sir")

                elif 'the time' in query:
                    strTime = datetime.datetime.now().strftime("%H:%M:%S")    
                    speak(f"Sir, the time is {strTime}")
                    print(strTime)
                

                elif 'google' in query:
                    from SearchNow import searchGoogle
                    searchGoogle(query)
                
                elif 'youtube' in query:
                    from SearchNow import searchYoutube
                    searchYoutube(query)
                
                elif 'wikipedia' in query:
                    from SearchNow import searchWikipedia
                    searchWikipedia(query)

                elif 'open notepad' in query:
                    npath = "C:\\Windows\\notepad.exe"
                    os.startfile(npath)
                
                elif 'open excel' in query:
                    npath = "C:\\Program Files\\Microsoft Office\\root\\Office16\\EXCEL.EXE"
                    os.startfile(npath)
                elif 'open microsoft excel' in query:
                    npath = "C:\\Program Files\\Microsoft Office\\root\\Office16\\EXCEL.EXE"
                    os.startfile(npath)

                elif 'open word' in query:
                    npath = "C:\\Program Files\\Microsoft Office\\root\\Office16\\WINWORD.EXE"
                    os.startfile(npath)
                elif 'open microsoft word' in query:
                    npath = "C:\\Program Files\\Microsoft Office\\root\\Office16\\WINWORD.EXE"
                    os.startfile(npath)
                    
                elif "go to sleep" in query:
                    speak("Ok sir و You can call me anytime")
                    break
                    
                elif 'open stackoverflow' in query:
                    webbrowser.open("stackoverflow.com")
                    break   
                


        elif "shutdown" or "shut down" in query:
            speak("I am happy to assist you sir! I'm going offline.")
            break


        


