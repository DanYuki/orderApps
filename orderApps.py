from tkinter import *
import sqlite3
from tkinter import messagebox
from datetime import date

#Creating the apps/Defining the apps meta
root = Tk()
root.title("OrderApps")
root.iconbitmap("assets/icon/shopbag.ico")
root.geometry("400x400")

#Establish connection into DB
connect = sqlite3.connect("database.db")
cursor = connect.cursor()


today = date.today()

#Variables defining section
menuList = {
    "Minyak 1Kg" : 8000,
    "Gula 1Kg" : 8000,
    "Kopi sachet" : 1500}
ordered_item = []
ordered_quantity = []
paired_order = {}

#Adding item into cart
def add(itemName):
    if itemName == "Minyak 1Kg":
        q = int(entry1.get())
        ordered_item.append(itemName)
        ordered_quantity.append(q)
        entry1.delete(0, END)
    elif itemName == "Gula 1Kg":
        q = int(entry2.get())
        ordered_item.append(itemName)
        ordered_quantity.append(q)
        entry2.delete(0, END)
    elif itemName == "Kopi sachet":
        q = int(entry3.get())
        ordered_item.append(itemName)
        ordered_quantity.append(q)
        entry3.delete(0, END)

#Show item that in the cart
def show():
    price = 0
    for x in range(len(ordered_item)):
        x - 1
        if ordered_item[x] in paired_order:
            paired_order[ordered_item[x]] += ordered_quantity[x]
        else:
            paired_order.update({ordered_item[x]:ordered_quantity[x]})
    Label(container_belanjaan, text="Daftar Belanjaan").pack()
    for y in paired_order: 
        price = menuList[y] * paired_order[y]
        Label(container_belanjaan, text=f"{y} {paired_order[y]} buah => Rp.{price}", bg='white').pack()
    totalPrice = 0
    for y in paired_order: 
        totalPrice += menuList[y] * paired_order[y]
    Label(container_belanjaan, text=f'Total pembayaran : Rp.{totalPrice}').pack()         

#Input transaction information, and update the item stock
def pay():
    messagebox.showinfo("Pembayaran", "Pembelian sukses")
    connect = sqlite3.connect("database.db")
    cursor = connect.cursor()
    items = ""
    quantity = ""
    totalPrice = 0
    for y in paired_order: 
        totalPrice += menuList[y] * paired_order[y]
    for item in paired_order:
        items += f'{item}' + ' '
        quantity += f'{paired_order[item]}' + ' '
        Q = paired_order[item]
        #Update item stock
        cursor.execute("""update items set stokBarang = stokBarang - ?
            where namaBarang = ?""", (Q, item))
       
    trDate = today.strftime("%d/%m/%Y")

    #Inserting transaction record
    cursor.execute("""insert into orderan(itemList, quantity, totalPrice, transactionDate)
        values(?, ?, ?, ?);""", (items, quantity, totalPrice, trDate))

    connect.commit()
    connect.close()

    root.destroy()


Label(root, text="Daftar Menu").grid(row=0, column=0)

row = 1

#Create the menu list/item list
for x in menuList: 
    Label(root, text=x).grid(row=row, column=0)
    row += 1

#Create entry for inputting item quantity
entry1 = Entry(root)
entry1.grid(row=1, column=1)
entry2 = Entry(root)
entry2.grid(row=2, column=1)
entry3 = Entry(root)
entry3.grid(row=3, column=1)

#Create add to cart button
Button(root, text="+", command=lambda:add("Minyak 1Kg")).grid(row=1, column=2, padx=10)
Button(root, text="+", command=lambda:add("Gula 1Kg")).grid(row=2, column=2, padx=10)
Button(root, text="+", command=lambda:add("Kopi sachet")).grid(row=3, column=2, padx=10)

#Button for showing the list of items that in the cart
Button(root, text="Show Belanjaan", command=show, width=15).grid(row=4, column=0, pady=5)
container_belanjaan = Frame(root, bg='white', bd=3)
container_belanjaan.grid(row=5, column=0, columnspan=3)
Button(root, text="Bayar", command=pay, width=15).grid(row=6, column=0)

#closing the DB
connect.close()

root.mainloop()