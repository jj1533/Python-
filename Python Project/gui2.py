import tkinter as tk
from tkinter import Frame, Label, Entry, Button
from PIL import Image, ImageTk


def calculatecost():
    try:
        distance = float(distancevalue.get())
        electricprice = float(electricpricevalue.get())
        mileage = float(mileagevalue.get())

        totalcost = distance / mileage * electricprice

        resultlabel1.config(text="Total cost is ₹{:.2f}".format(totalcost))
    except ValueError:
        resultlabel1.config(text="Invalid values.")

def evgui():
    root2=tk.Toplevel()
    root2.geometry("1000x500")
    root2.title("Calculator")

    image = Image.open("ev.jpg")
    image = image.resize((180, 150), Image.BICUBIC)
    photo = ImageTk.PhotoImage(image)
    mylabel = Label(root2,image=photo)
    mylabel.grid(row=0, column=0, padx=20, pady=30, rowspan=2)

    f1 = Frame(root2)
    f1.grid(row=0, column=1, sticky="ew")
    label1 = Label(f1, text="ELECTRIC VEHICLE CHARGE COST CALCULATOR", fg="red", font="Helvetica 20 bold")
    label1.grid(row=0,column=0)

    f2 = Frame(root2)
    f2.grid(row=1, column=1, padx=40, pady=(5,0), sticky="ew")
    distance = Label(f2, text="Distance to be covered (Km): ", font="Roboto 13 bold")
    distance.grid(row=0, column=0, padx=5, pady=(5,0), sticky="w")

    global distancevalue, electricpricevalue, mileagevalue, resultlabel1
    
    distancevalue = tk.DoubleVar()
    distanceentry = Entry(f2, textvariable=distancevalue, justify="right")
    distanceentry.grid(row=0, column=1, padx=5, pady=5, sticky="e")

    f3 = Frame(root2)
    f3.grid(row=2, column=1, padx=40, pady=(0,10), sticky="ew")
    electricprice=Label(f3, text="Electricity Rate (kWh): ", font="Roboto 13 bold")
    electricprice.grid(row=0, column=0, padx=(0,5), pady=5, sticky="w")

    electricpricevalue=tk.DoubleVar()
    electricpriceentry=Entry(f3, textvariable=electricpricevalue, justify="right")
    electricpriceentry.grid(row=0, column=1, padx=5, pady=5, sticky="e")

    f4 = Frame(root2)
    f4.grid(row=3, column=1, padx=40, pady=10, sticky="ew")
    mileage = Label(f4, text="Vehicle's efficiency (Km/kWh): ", font="Roboto 13 bold")
    mileage.grid(row=0, column=0, padx=5, pady=5, sticky="w")

    mileagevalue = tk.DoubleVar()
    mileageentry = Entry(f4, textvariable=mileagevalue, justify="right")
    mileageentry.grid(row=0, column=1, padx=5, pady=5, sticky="e")

    button1 = Button(root2, text="Calculate", font="Roboto 13 bold", command=calculatecost, bg="Darkgreen", fg="white")
    button1.grid(row=7, column=1)

    f5 = Frame(root2)
    f5.grid(row=9, column=1, padx=40, pady=10)
    resultlabel1 = Label(f5, text="", fg="coral", font="Roboto 13 bold")
    resultlabel1.grid(row=0, column=0)



    distancevalue.set('')
    electricpricevalue.set('')
    mileagevalue.set('')

    root2.mainloop()



