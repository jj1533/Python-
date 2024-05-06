import tkinter as tk
from tkinter import Frame, Label, Entry, Button
from PIL import Image, ImageTk


def calculatecost():
    try:
        distance=float(distancevalue.get())
        fuelprice=float(fuelpricevalue.get())
        mileage=float(mileagevalue.get())

        totalcost=distance/mileage*(fuelprice)
        totalfuel=distance/mileage

        resultlabel1.config(text="Total cost for the fuel is ₹{:.2f}".format(totalcost))
        resultlabel2.config(text="Total fuel required is: {:.2f}L".format(totalfuel))
    except:
        resultlabel1.config(text="Invalid values.")

def fuelgui():
    root1=tk.Toplevel()
    root1.geometry("700x500")
    root1.title("calculator")



    image=Image.open("FuelPriceCalculator.jpg")
    image=image.resize((120,150),Image.BICUBIC)
    photo=ImageTk.PhotoImage(image)
    mylabel=Label(root1,image=photo)
    mylabel.grid( row=0,column=0,padx=20, pady=30, rowspan=2)

    f1=Frame(root1)
    f1.grid(row=0, column=1, sticky="ew")
    label1=Label(f1,text="FUEL COST CALCULATOR",fg="red",font="Helvetica 20 bold")
    label1.grid(row=0,column=0)


    f2=Frame(root1)
    f2.grid(row=1, column=1,padx=40, pady=(5,0), sticky="ew")
    distance=Label(f2,text="Distance to be covered (Km): ",font="Roboto 13 bold")
    distance.grid(row=0, column=0,padx=5,pady=(5,0),sticky="w")

    global distancevalue, fuelpricevalue, mileagevalue, resultlabel1, resultlabel2
    
    distancevalue=tk.DoubleVar()
    distanceentry=Entry(f2,textvariable=distancevalue,justify="right")
    distanceentry.grid(row=0, column=1,padx=5, pady=5, sticky="e")

    f3=Frame(root1)
    f3.grid(row=2, column=1,padx=40, pady=(0,10), sticky="ew")
    fuelprice=Label(f3,text="Fuel price per liter (INR): ",font="Roboto 13 bold")
    fuelprice.grid(row=0, column=0, padx=(0,5), pady=5, sticky="w")

    fuelpricevalue=tk.DoubleVar()
    fuelpriceentry=Entry(f3,textvariable=fuelpricevalue,justify="right")
    fuelpriceentry.grid(row=0, column=1,padx=5, pady=5, sticky="e")

    f4=Frame(root1)
    f4.grid(row=3,column=1,padx=40,pady=10, sticky="ew")
    mileage=Label(f4,text="Vehicle's mileage (Km/L): ",font="Roboto 13 bold")
    mileage.grid(row=0,column=0, padx=5, pady=5, sticky="w")

    mileagevalue=tk.DoubleVar()
    mileageentry=Entry(f4,textvariable=mileagevalue,justify="right")
    mileageentry.grid(row=0, column=1,padx=5, pady=5,  sticky="e")


    button1=Button(root1,text="Calculate",font="Roboto 13 bold",command=calculatecost,bg="Darkgreen",fg="white")
    button1.grid(row=7,column=1)

    f5=Frame(root1)
    f5.grid(row=9,column=1,padx=40,pady=10)
    resultlabel1=Label(f5,text="",fg="coral",font="Roboto 13 bold")
    resultlabel1.grid(row=0,column=0)

    f6=Frame(root1)
    f6.grid(row=11,column=1,padx=40,pady=10)
    resultlabel2=Label(f6,text="",fg="maroon",font="Roboto 13 bold")
    resultlabel2.grid(row=0,column=0)


    distancevalue.set('')
    fuelpricevalue.set('')
    mileagevalue.set('')



    

    root1.mainloop()



