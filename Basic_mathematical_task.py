import speech_recognition as sr
import operator
import pyttsx3

engine = pyttsx3.init() # object creation


def get_operator_fn(op):
    return {
        '+' : operator.add,
        '-' : operator.sub,
        'x' : operator.mul,
        'X' : operator.mul,
        'divided' :operator.__truediv__,
        'Mod' : operator.mod,
        'mod' : operator.mod,
        '^' : operator.xor,
        }[op]
def eval_binary_expr(op1, oper, op2):
    op1,op2 = int(op1), int(op2)
    return get_operator_fn(oper)(op1, op2)

r=sr.Recognizer()
#print(sr.Microphone.list_microphone_names())
with sr.Microphone() as source:
    r.adjust_for_ambient_noise(source,duration=1)
    # r.energy_threshold()
    print("please say calculate: ")
    engine = pyttsx3.init()
    engine.say('please say calculate')
    engine.runAndWait()
    audio= r.listen(source)
    text = r.recognize_google(audio)
    print(text)
    try:
        if('calculate'==text):
            print('What do you want to calculate: Example 2+3')
            audio= r.listen(source)
            t = r.recognize_google(audio)
            print(t)
            temp=(eval_binary_expr(*(t.split())))
            print(temp)
            t=str(temp)
            
    except:
        print('Error occured')
            
            
    



