import mysql.connector
from tkinter import *
from tkinter import messagebox

# Connect to the LibraryDB database
def connect_to_db():
    try:
        conn = mysql.connector.connect(
            host="localhost",
            user="root",   # Replace with your MySQL username
            password="MySQLpassword4321",  # Replace with your MySQL password
            database="LibraryDB"
        )
        return conn
    except mysql.connector.Error as err:
        messagebox.showerror("Database Connection Error", str(err))
        return None

# Function to add a new member
def add_member():
    conn = connect_to_db()
    if conn:
        cursor = conn.cursor()
        sql = "INSERT INTO Members (MemberID, FullName, Email, Phone, Address) VALUES (%s, %s, %s, %s, %s)"
        values = (entry_member_id.get(), entry_name.get(), entry_email.get(), entry_phone.get(), entry_address.get())
        cursor.execute(sql, values)
        conn.commit()
        cursor.close()
        conn.close()
        messagebox.showinfo("Success", "Member added successfully!")
        clear_fields()

# Function to search for a member by MemberID
def search_member():
    conn = connect_to_db()
    if conn:
        cursor = conn.cursor()
        sql = "SELECT * FROM Members WHERE MemberID = %s"
        cursor.execute(sql, (entry_member_id.get(),))
        result = cursor.fetchone()
        if result:
            entry_name.delete(0, END)
            entry_email.delete(0, END)
            entry_phone.delete(0, END)
            entry_address.delete(0, END)
            entry_name.insert(END, result[1])
            entry_email.insert(END, result[2])
            entry_phone.insert(END, result[3])
            entry_address.insert(END, result[4])
        else:
            messagebox.showinfo("Not Found", "Member not found.")
        cursor.close()
        conn.close()

# Function to clear all input fields
def clear_fields():
    entry_member_id.delete(0, END)
    entry_name.delete(0, END)
    entry_email.delete(0, END)
    entry_phone.delete(0, END)
    entry_address.delete(0, END)

# Setting up the Tkinter UI
root = Tk()
root.title("Library Database UI")
root.geometry("400x300")

# MemberID field
Label(root, text="Member ID").grid(row=0, column=0, padx=10, pady=10)
entry_member_id = Entry(root)
entry_member_id.grid(row=0, column=1, padx=10, pady=10)

# Full Name field
Label(root, text="Full Name").grid(row=1, column=0, padx=10, pady=10)
entry_name = Entry(root)
entry_name.grid(row=1, column=1, padx=10, pady=10)

# Email field
Label(root, text="Email").grid(row=2, column=0, padx=10, pady=10)
entry_email = Entry(root)
entry_email.grid(row=2, column=1, padx=10, pady=10)

# Phone field
Label(root, text="Phone").grid(row=3, column=0, padx=10, pady=10)
entry_phone = Entry(root)
entry_phone.grid(row=3, column=1, padx=10, pady=10)

# Address field
Label(root, text="Address").grid(row=4, column=0, padx=10, pady=10)
entry_address = Entry(root)
entry_address.grid(row=4, column=1, padx=10, pady=10)

# Buttons for Add, Search, and Clear actions
Button(root, text="Add Member", command=add_member).grid(row=5, column=0, padx=10, pady=20)
Button(root, text="Search Member", command=search_member).grid(row=5, column=1, padx=10, pady=20)
Button(root, text="Clear", command=clear_fields).grid(row=6, column=0, columnspan=2, pady=10)

root.mainloop()
