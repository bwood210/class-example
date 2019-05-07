from tkinter import *

def changepurple():
    lab1.config(bg="purple")
    lab1.config(text="Purple Label")
def returnred():
    lab1.config(bg="red")
    lab1.config(text="Red Label")
m = Tk()
m.title("Tkinter Color Labels")

fr1 = Frame(m)
fr2 = Frame(m, pady=12)
#labels
lab1 = Label(fr1, text = "Red Label", fg="white", bg="red", width=12, height=6, font=("Cambria", 24))
lab2 = Label(fr1, text = "Green Label", fg="white", bg="green", width=12, height=6, font=("Cambria", 24))
lab3 = Label(fr1, text = "Blue Label", fg="white", bg="blue", width=12, height=6, font=("Cambria", 24))
#buttons
btn1 = Button(fr2, text="Change Purple", padx= 6, font=("none", 16), command=changepurple)
btn2 = Button(fr2, text="Change Red", padx= 6, font=("none", 16), command=returnred)
btn3 = Button(fr2, text="Quit", padx= 6, font=("none", 16), command=quit)
#packing
fr1.pack()
fr2.pack()
lab1.pack(side = LEFT, fill=Y)
lab2.pack(side = LEFT, fill=Y)
lab3.pack(side = LEFT, fill=Y)
btn1.pack(side = LEFT)
btn2.pack(side = LEFT)
btn3.pack(side = LEFT)
m.mainloop()