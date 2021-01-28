from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer
from tkinter import *
import  speech_recognition as s
import threading
#import pyttsx3
#engine = pyttsx3.init()
#voice=engine.getProperty('voices')
#engine.setProperty('voice', voice[0].id)

#def speak(word):
 #   engine.say(word)
  #  engine.runAndWait()

bot = ChatBot('My Bot')

convo = [
    'hello',
    'hi there !',
    'what is your name ?',
    'My name is Bot , i am created by Durgesh',
    'how are you ?',
    'I am doing great these days',
    'thank you',
    'In which city you live ?',
    'I live in lucknow',
   'In which language you talk?',
   ' I mostly talk in english'
]
trainer = ListTrainer(bot)
#now training the bot with the help of trainer
trainer.train(convo)

main=Tk()
main.geometry("500x650")
main.configure(background='grey')
main.option_add('*Font', 'Times 19')

main.title("My Chat bot")
img = PhotoImage(file="botg.png")
#photo=PhotoImage(file="ask_me.png")
photoL = Label(main, image=img ,width=2000,height=170)

photoL.pack(pady=5)

def takequery():
    sr=s.Recognizer()
    sr.pause_threshold=1
    print("yours")
    with s.Microphone() as m:
        try:
            audio=sr.listen(m)
            query=sr.recognize_google(audio,language='eng-in')
            print(query)
            textF.delete(0,END)
            textF.insert(0,query)
            ask_from_bot()
        except Exception as e:
            print(e)


def ask_from_bot():
    query = textF.get()
    answer_from_bot = bot.get_response(query)
    msgs.insert(END, "you : " + query)

    msgs.insert(END, "bot : " + str(answer_from_bot))
    #speak(answer_from_bot)
    textF.delete(0, END)
    msgs.yview(END)


frame=Frame(main)
sc=Scrollbar(frame)
sc1= Scrollbar(frame, orient=HORIZONTAL)
msgs=Listbox(frame,width=200,height=10,background="lightblue", foreground="blue",xscrollcommand=sc1.set,yscrollcommand=sc.set)
sc.pack(side=RIGHT, fill=Y)
sc1.pack(side=BOTTOM, fill=X)
msgs.pack(side=LEFT, fill=BOTH, pady=10)

frame.pack()

textF=Entry(main ,background="lightblue", foreground="blue")
textF.pack(fill=X,pady=10)

btn=Button(main,text="Ask from Bot",command=ask_from_bot,background="lightblue", foreground="blue" )
btn.pack()
def enter_function(event):
    btn.invoke()

main.bind("<Return>",enter_function)

def repeat():
    while TRUE:
        takequery()

t=threading.Thread(target=repeat)
t.start()
main.mainloop()