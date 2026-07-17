#DataFlair- import modules
from tkinter import *
import tkinter as tk
from tkinter import messagebox
import os
 
DB_FILE = "Proj_Database"
if not os.path.exists(DB_FILE):
    with open(DB_FILE, "w", encoding="utf-8"):
        pass

root = Tk()
root.title("Shop Managment System by DataFlair")
root.geometry("1500x600")
root.configure(bg="#e3f4f1")

#DataFlair- function to add items

def Add_Items():
    E1 = Entry_1.get().strip()
    E2 = Entry_2.get().strip()
    E3 = Entry_3.get().strip()
    E4 = Entry_4.get().strip()
    E5 = Entry_5.get().strip()
    if not E1 or not E2 or not E3 or not E4 or not E5:
        messagebox.showwarning("ADD ITEM", "Please fill in all fields before adding an item.")
        return

    with open(DB_FILE, "a", encoding="utf-8") as db:
        db.write(f"{E1} {E2} {E3} {E4} {E5}\n")

    Entry_1.delete(0, END)
    Entry_2.delete(0, END)
    Entry_3.delete(0, END)
    Entry_4.delete(0, END)
    Entry_5.delete(0, END)
    messagebox.showinfo("ADD ITEM", "ITEM ADDED SUCCESSFULLY....!!!!!")


#DataFlair- function to delete items

def Delete_Items():
    search_term = Entry_1.get().strip()
    if not search_term:
        messagebox.showwarning("DELETE ITEM", "Please enter the item name to delete.")
        return

    updated_lines = []
    deleted = False
    with open(DB_FILE, "r", encoding="utf-8") as db:
        for line in db:
            if search_term in line:
                deleted = True
                continue
            updated_lines.append(line)

    if not deleted:
        messagebox.showinfo("DELETE ITEM", "Item not found in the database.")
        return

    with open(DB_FILE, "w", encoding="utf-8") as db:
        db.writelines(updated_lines)

    Entry_1.delete(0, END)
    Entry_2.delete(0, END)
    Entry_3.delete(0, END)
    Entry_4.delete(0, END)
    Entry_5.delete(0, END)
    messagebox.showinfo("DELETE ITEM", "ITEM DELETED SUCCESSFULLY....!!!!!")


def view_database():
    root_1 = Tk()
    root_1.configure(bg="Gray")
    root_1.title("Stationary Store Database")
    scroll = Scrollbar(root_1)
    scroll.pack(side=RIGHT, fill=Y)
    My_text = Text(root_1, yscrollcommand=scroll.set, width=24, height=18, bg="gray", fg="black", font=("Times", 16))

    with open(DB_FILE, "r", encoding="utf-8") as db:
        string = db.read()

    My_text.insert(END, string)
    My_text.pack(side=LEFT, fill=BOTH)
    scroll.config(command=My_text.yview)


def Search_Item():
    Entry_1.delete(0, END)
    Entry_2.delete(0, END)
    Entry_3.delete(0, END)
    Entry_4.delete(0, END)
    Entry_5.delete(0, END)

    search_term = Entry_6.get().strip()
    if not search_term:
        messagebox.showwarning("SEARCH ITEM", "Please enter a search term.")
        return

    found = False
    with open(DB_FILE, "r", encoding="utf-8") as working:
        for line in working:
            if search_term in line:
                fields = line.strip().split(maxsplit=4)
                if len(fields) >= 5:
                    Entry_1.insert(0, fields[0])
                    Entry_2.insert(0, fields[1])
                    Entry_3.insert(0, fields[2])
                    Entry_4.insert(0, fields[3])
                    Entry_5.insert(0, fields[4])
                else:
                    messagebox.showinfo("SEARCH ITEM", "Corrupt or unexpected data format.")
                found = True
                break

    if not found:
        messagebox.showinfo("SEARCH ITEM", "NOT FOUND")


def Clear_Item():
    Entry_1.delete(0, END)
    Entry_2.delete(0, END)
    Entry_3.delete(0, END)
    Entry_4.delete(0, END)
    Entry_5.delete(0, END)
    Entry_6.delete(0, END)


def Exit():
    Exit= messagebox.askyesno("Exit the System","Do you want to Exit(y/n)?")
    if Exit > 0:
        root.destroy()
        return


#All labels Entrys Button grid place
Label_0= Label(root,text="SHOP MANAGEMENT SYSTEM BY DATAFLAIR ",fg="black",font=("Times new roman", 30, 'bold'))
Label_0.grid(columnspan=6)

Label_1=Label(root,text="ENTER ITEM NAME",bg="#e8c1c7",fg="black",bd=8,font=("Times new roman", 12, 'bold'),width=25)
Label_1.grid(row=1,column=0)
Entry_1=Entry(root, font=("Times new roman", 14),bd=8,width=25)
Entry_1.grid(row=1,column=1)

Label_2=Label(root, text="ENTER ITEM PRICE",height="1",bg="#e8c1c7",bd=8,fg="black", font=("Times new roman", 12, 'bold'),width=25)
Label_2.grid(row=2,column=0)
Entry_2= Entry(root, font=("Times new roman", 14),bd=8,width=25)
Entry_2.grid(row=2,column=1)

Label_3=Label(root, text="ENTER ITEM QUANTITY",bg="#e8c1c7",bd=8,fg="black", font=("Times new roman", 12, 'bold'),width=25)
Label_3.grid(row=3,column=0)
Entry_3= Entry(root, font=("Times new roman", 14),bd=8,width=25)
Entry_3.grid(row=3,column=1)

Label_4=Label(root, text="ENTER ITEM CATEGORY",bg="#e8c1c7",bd=8,fg="black", font=("Times new roman", 12, 'bold'),width=25)
Label_4.grid(row=4,column=0)
Entry_4= Entry(root, font=("Times new roman", 14),bd=8,width=25)
Entry_4.grid(row=4,column=1)

Label_5=Label(root, text="ENTER ITEM DISCOUNT",bg="#e8c1c7",fg="black",bd=8, font=("Times new roman", 12, 'bold'),width=25)
Label_5.grid(row=5,column=0, padx=10, pady=10)
Entry_5= Entry(root, font=("Times new roman", 14),bd=8,width=25)
Entry_5.grid(row=5,column=1, padx=10, pady=10)


Button_1= Button(root,text="ADD ITEM",bd=8, bg="#49D810", fg="black", width=25, font=("Times new roman", 12),command=Add_Items)
Button_1.grid(row=6,column=0, padx=10, pady=10)
Button_2= Button(root, text="DELETE ITEM",bd=8, bg="#49D810", fg="black", width =25, font=("Times new roman", 12),command=Delete_Items)
Button_2.grid(row=6,column=1, padx=40, pady=10)
Button_3= Button(root, text="VIEW DATABASE",bd=8, bg="#49D810", fg="black", width =25, font=("Times new roman", 12),command=view_database)
Button_3.grid(row=3,column=3, padx=40, pady=10)
Button_4= Button(root, text="SEARCH ITEM",bd=8, bg="#49D810", fg="black", width =25, font=("Times new roman", 12),command=Search_Item)
Button_4.grid(row=2,column=3, padx=40, pady=10)
Button_5= Button(root, text="CLEAR SCREEN",bd=8, bg="#49D810", fg="black", width=25, font=("Times new roman", 12),command=Clear_Item)
Button_5.grid(row=4,column=3, padx=40, pady=10)
Button_6= Button(root,highlightcolor="blue",activebackground="red", text="Exit",bd=8, bg="#FF0000", fg="#EEEEF1", width=25, font=("Times", 40),command=Exit)
Button_6.place(x=635,y=337,height= 102,width=245)
Entry_6= Entry(root, font=("Times new roman", 14),justify='left',bd=8,width=25)
Entry_6.grid(row=1,column=3, padx=10, pady=10)

root.mainloop()
