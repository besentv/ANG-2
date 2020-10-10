from tkinter import *
import Idd
import datetime

window = Tk()
iddShow = Text(window)
labelBirthday = Label(window)
lableExpirationDay = Label(window)

def generateIdd():
    idd = Idd.Idd.createRandom()
    iddShow.config(state=NORMAL)
    iddShow.delete('1.0', END)
    iddShow.insert('end', str(idd))
    iddShow.config(state=DISABLED)
    labelBirthday.config(text = "Birthday: " + idd.birthdate.strftime("%d.%m.%Y"))
    lableExpirationDay.config(text = "Expiration Day: " + idd.expirationDate.strftime("%d.%m.%Y"))
    return

generateButton = Button(window, text="Generate IDD", command=generateIdd)


def main():
    window.title("ANG2")
    window.geometry("600x600")

    generateButton.pack()
    labelBirthday.pack()
    lableExpirationDay.pack()
    iddShow.pack()
    iddShow.config(state=DISABLED)

    window.mainloop()

main()