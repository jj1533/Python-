from tkinter import *
root=Tk()
from gui1 import fuelgui
from gui2 import evgui


def main():
    root.title("Main GUI")
    root.geometry("300x200")
    button1 = Button(root, text="Fuel Cost Calculator", command=fuelgui,font="Arial 13 bold",fg="Dark Green")
    button1.grid(row=0,column=1,padx=60,pady=40)

    button2 = Button(root, text="EV Charge Cost Calculator", command=evgui,font="Arial 13 bold",fg="Dark Blue")
    button2.grid(row=3,column=1,padx=40)

    root.mainloop()

if __name__ == "__main__":
    main()