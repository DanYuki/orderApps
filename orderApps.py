from tkinter import *
import sqlite3
from tkinter import messagebox
from datetime import date

root = Tk()
root.title("OrderApps")
root.iconbitmap("assets/icon/shopbag.ico")
root.geometry("400x400")

connect = sqlite3.connect("database.db")
cursor = connect.cursor()

today = date.today()

menuList = ["Minyak 1Kg", "Gula 1Kg", "Kopi sachet"]
menuPrice = {
    "Minyak 1Kg" : 8000,
    "Gula 1Kg" : 8000,
    "Kopi sachet" : 1500
}
ordered_item = []
ordered_quantity = []
paired_order = {}
items = ""
quantity = ""

def add(name):
    if name == "Minyak 1Kg":
        q = int(entry1.get())
        ordered_item.append(name)
        ordered_quantity.append(q)
        entry1.delete(0, END)
    elif name == "Gula 1Kg":
        q = int(entry2.get())
        ordered_item.append(name)
        ordered_quantity.append(q)
        entry2.delete(0, END)
    elif name == "Kopi sachet":
        q = int(entry3.get())
        ordered_item.append(name)
        ordered_quantity.append(q)
        entry3.delete(0, END)

def show():
    global price
    for x in range(len(ordered_item)):
        x - 1
        if ordered_item[x] in paired_order:
            paired_order[ordered_item[x]] += ordered_quantity[x]
        else:
            paired_order.update({ordered_item[x]:ordered_quantity[x]})
    for y in paired_order: 
        price = menuPrice[y] * paired_order[y]
        Label(container_belanjaan, text=f"{y} : {paired_order[y]} = Rp.{price}", bg='white').pack()         

def pay():
    messagebox.showinfo("Pembayaran", "Pembelian sukses")
    connect = sqlite3.connect("database.db")
    cursor = connect.cursor()
    
    for item in paired_order:
        global items, quantity
        items += f'{item}, '
        quantity += f'{paired_order[item]}, '
       
    trDate = today.strftime("%d/%m/%Y")

    print(items)
    cursor.execute("""insert into orderan(itemList, quantity, totalPrice, transactionDate)
        values(:items, :quantity, :price, :trDate) 
        """)

    connect.commit()
    connect.close()

    root.destroy()

Label(root, text="Daftar Menu").grid(row=0, column=0)

row = 1

for x in menuList : 
    Label(root, text=x).grid(row=row, column=0)
    row += 1

entry1 = Entry(root)
entry1.grid(row=1, column=1)
entry2 = Entry(root)
entry2.grid(row=2, column=1)
entry3 = Entry(root)
entry3.grid(row=3, column=1)

Button(root, text="+", command=lambda:add("Minyak 1Kg")).grid(row=1, column=2, padx=10)
Button(root, text="+", command=lambda:add("Gula 1Kg")).grid(row=2, column=2, padx=10)
Button(root, text="+", command=lambda:add("Kopi sachet")).grid(row=3, column=2, padx=10)

Button(root, text="Show Belanjaan", command=show, width=15).grid(row=4, column=0, pady=5)
container_belanjaan = Frame(root, bg='white', bd=3)
container_belanjaan.grid(row=5, column=0, columnspan=3)
Button(root, text="Bayar", command=pay, width=15).grid(row=6, column=0)

connect.close()

root.mainloop()