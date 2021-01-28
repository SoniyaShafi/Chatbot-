from chatterbot import ChatBot
from tkinter import *
import speech_recognition as s
import threading

bot = ChatBot('My Bot',
              logic_adapters=[
                  "chatterbot.logic.BestMatch",
                  "chatterbot.logic.MathematicalEvaluation",
                  "chatterbot.logic.TimeLogicAdapter",
                  {"import_path": "chatterbot.logic.BestMatch",
                   "default_response":"sorry!I can't understand",
                   "maximum_similarity_threshold": 0.90}
    ])


from chatterbot.trainers import ChatterBotCorpusTrainer

trainer = ChatterBotCorpusTrainer(bot)

trainer.train(
    "chatterbot.corpus.english.greetings",
    "chatterbot.corpus.english.ai",
    "chatterbot.corpus.english.botprofile",
    )

main=Tk()
main.geometry("500x650")
main.configure(background='grey')
main.option_add('*Font', 'Times 19')

main.title("My Chat bot")
img = PhotoImage(file="botg.png")
photoL = Label(main, image=img ,width=2000,height=170)

photoL.pack(pady=5)
# take query : it takes audio as input from user and convert it to string..

def takequery():
    sr=s.Recognizer()
    sr.pause_threshold=1
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
    textF.delete(0, END)
    msgs.yview(END)


frame=Frame(main)
sc=Scrollbar(frame)
sc1= Scrollbar(frame, orient=HORIZONTAL)
msgs=Listbox(frame,width=200,height=10,background="lightblue", foreground="blue",xscrollcommand=sc1.set)
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