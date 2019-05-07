from tkinter import *
m = Tk()
m.title("Running Pace Calculator")
m.configure(padx=20, pady=20, bg="#D2B48C")
lab1 = Label(m, text ="Running Pace Calculator",bg="#D2B48C",fg= "blue", font=("Cambria",24)).grid(row=0, column=1, sticky=W)
lab2 = Label(m, text="Minutes:",bg="#D2B48C", font=("Cambria",18)).grid(row=1, column=0, sticky=W)
lab3 = Label(m, text="Seconds:",bg="#D2B48C", font=("Cambria",18)).grid(row=2, column=0, sticky= W)
lab4 = Label(m, text="Miles:",bg="#D2B48C",font=("Cambria",18)).grid(row=3, column=0, sticky=E)
lab5 = Label(m, text="Date:",bg="#D2B48C",font=("Cambria",18)).grid(row=4, column=0, sticky=E)
lab6 = Label(m, text="Or Enter Past Date:",bg="#D2B48C",font=("Cambria",12)).grid(row=5, column=1, sticky=W)
lab7 = Label(m, text="Month:",bg="#D2B48C",font=("Cambria",12)).grid(row=6, column=1, sticky= W)
lab8 = Label(m, text="Day:",bg="#D2B48C",font=("Cambria",12)).grid(row=6, column=2, sticky = W)
lab9 = Label(m, text="Year:",bg="#D2B48C",font=("Cambria",12)).grid(row=6, column=3, sticky= W)


btn1 = Button(m, pady=6, text="USE TODAY", width=25).grid(row=4, column=1, sticky=W)

e1 = Entry(m, width=5,font=("Cambria",24))
e2 = Entry(m, width=5,font=("Cambria",24))
e3 = Entry(m, width=5,font=("Cambria",24))
e1.grid(row=1, column=1, sticky=W, pady= 10)
e2.grid(row=2, column=1, sticky=W, pady= 10)
e3.grid(row=3, column=1, sticky=W, pady= 10)
m.mainloop()