from tkinter import *


def collect_data():
  username = entry1.get()
  password = entry3.get()
  output_lable.config(text=f'{username}: {password}')


win = Tk()

win.geometry("450x270")
win.configure(bg = "#fff")
win.title("Text Widget")

name = Label(win, text="username",bg= "#fff",fg= "#000",font =("Agency FB", 14)).place(x=30, y=40)
email = Label(win, text="Email",bg= "#fff",fg= "#000",font =("Agency FB", 14)).place(x=30, y=80)
password = Label(win, text="password",bg= "#fff",fg= "#000",font =("Agency FB", 14)).place(x=30, y=120)


submitbtn = Button(win, text="Submit",font =("Agency FB", 11), command=collect_data).place(x=30, y=170)

entry1 = Entry(win).place(x=100, y=50)

entry2 = Entry(win).place(x=100, y=90)

entry3 = Entry(win).place(x=100, y=130)



output_label = Label(win, text="")
output_label.pack()


win.mainloop()