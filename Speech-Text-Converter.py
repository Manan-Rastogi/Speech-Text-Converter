import textConverter as tc
import SpeechConverter as sc
from tkinter import *

# tc.TextConvertor("LOL")
# sc.Convert()

root = Tk()

root.title("Speech-Text Converter by UDM")

root.geometry("380x300+400+200")
root.resizable(False, False)
root.config(bg="black")


label1 = Label(root,state=DISABLED, text="Speech to Text",relief=SUNKEN, disabledforeground="grey", 
                 bg="white",font="times 14 bold",padx=5,pady=5)
label1.place(x=150, y = 60, width=200, height=50)

button1 = Button(root,text="Speak!",borderwidth=1, relief=SUNKEN, fg="white", 
                 bg="blue",font="times 16 bold",command=lambda:sc.Convert(label1))
button1.place(x = 50, y = 60, width=80, height=50)



enterText = StringVar()
enterText.set("Text to Speech")

entry2 = Entry(root, textvariable=enterText,relief=SUNKEN, fg="black", 
                 bg="white",font="times 14 bold")
entry2.place(x=50, y = 160, width=200, height=50)


button2 = Button(root,text="Convert",borderwidth=1, relief=SUNKEN, fg="white", 
                 bg="blue",font="times 16 bold",command=lambda:tc.TextConvertor(entry2))
button2.place(x = 270, y = 160, width=80, height=50)


root.mainloop()