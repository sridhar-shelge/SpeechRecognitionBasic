import speech_recognition as sr
import time
import sys

time_start = time.time()
seconds = 0
minutes = 0

while(True):

    r=sr.Recognizer()
    #print(sr.Microphone.list_microphone_names())
    with sr.Microphone() as source:
        r.adjust_for_ambient_noise(source,duration=1)
        print('say start')
     
        audio = r.listen(source)
        
        text = r.recognize_google(audio)

        print(text)
        
    if(text=='start'):
        running=True

    while running:
        try:
            sys.stdout.write("\r{minutes}:{seconds}\n".format(minutes=minutes, seconds=seconds))
            sys.stdout.flush()
            time.sleep(1)
            seconds = int(time.time() - time_start) - minutes * 60
            if seconds >= 60:
                minutes += 1
                seconds = 0
            audio= r.listen(source)
            t = r.recognize_google(audio)
            if(t=='stop'):
                running=False
        except KeyboardInterrupt as e:
            running = False
