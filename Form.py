from tkinter import *
import re
import cx_Oracle
from tkinter import messagebox

root = Tk()

# database
def database_submit():
    firstname_db = first_name_entry.get()
    lastname_db = last_name_entry.get()
    gender_db = gender_variable.get().strip()
    email_db = email_entry.get()

    try:
        con = cx_Oracle.connect('hr/hr@localhost:1521/orclpdb')
        cur = con.cursor()
        cur.execute(f"insert into form_details(First_name, last_name, gender, email) values(:1, :2, :3, :4)",
                    (firstname_db, lastname_db, gender_db, email_db))
        con.commit()
        data_submit_message = messagebox.showinfo("Databse", "Data Submitted Successfully")
    except cx_Oracle.DatabaseError as e:
        print(e)
    finally:
        cur.close()
        con.close()

# check email logic
def check_email_function():
    email_variable = email_entry.get()
    pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    if re.match(pattern, email_variable):
        return True
    else:
        return False

# validate checked email logic
def validate_email_function():
    if check_email_function():
        validate_label.config(text="VALID", fg="green")
        enabled_function()
    else:
        validate_label.config(text="INVALID", fg="red")
        submit_button["state"] = "disabled"

# required logic
def enabled_function():
    f_name_r = first_name_entry.get()
    l_name_r = last_name_entry.get()
    gender_r = gender_variable.get().strip()

    first_name_required_label.config(text="*required" if not f_name_r else "", fg="red")
    last_name_required_label.config(text="*required" if not l_name_r else "", fg="red")
    gender_required_label.config(text="*required" if not gender_r else "", fg="red")

    if check_email_function() and f_name_r and l_name_r and gender_r:
        submit_button["state"] = "normal"
    else:
        submit_button["state"] = "disabled"

# clear button logic
def clear_function():
    first_name_entry.delete(0,END)
    last_name_entry.delete(0,END)
    gender_variable.set(" ")
    email_entry.delete(0, END)

    validate_label.config(text="")
    first_name_required_label.config(text="")
    last_name_required_label.config(text="")
    gender_required_label.config(text="")

    submit_button["state"] = "disabled"

# first name label
first_name = Label(root, text="FIRST NAME : ")
first_name.grid(row=0, column=0, padx=4)

# first name entry
first_name_entry = Entry(root)
first_name_entry.grid(row=0, column=1, pady=10)

# last name label
last_name = Label(root, text="LAST NAME : ")
last_name.grid(row=1, column=0, padx=4)

# last name entry
last_name_entry = Entry(root)
last_name_entry.grid(row=1, column=1, pady=10)

# gender label
gender = Label(root, text="GENDER : ")
gender.grid(row=2, column=0, pady=10)

# gender radio button
gender_variable = StringVar()
gender_variable.set(" ")

male_radiobutton = Radiobutton(root, text="Male", variable=gender_variable, value="Male")
male_radiobutton.grid(row=2, column=1)

female_radiobutton = Radiobutton(root, text="Female", variable=gender_variable, value="Female")
female_radiobutton.grid(row=3, column=1)

# email label
email = Label(root, text="EMAIL : ")
email.grid(row=4, column=0, pady=10)

# email entry
email_entry = Entry(root)
email_entry.grid(row=4, column=1)

# email validate button
email_validate_button = Button(root, text="Validate", command=validate_email_function)
email_validate_button.grid(row=4, column=2, padx=5)

# clear button
clear = Button(root, text="CLEAR", command=clear_function)
clear.grid(row=6, column=2)

# submit button
submit_button = Button(root, text="SUBMIT", command=database_submit, state="disabled")
submit_button.grid(row=6, column=1, pady=5)

# validate label
validate_label = Label(root)
validate_label.grid(row=5, column=1)

# first name required label
first_name_required_label = Label(root)
first_name_required_label.grid(row=0,column=2)

# second name required label
last_name_required_label = Label(root)
last_name_required_label.grid(row=1,column=2)

# gender required label
gender_required_label = Label(root)
gender_required_label.grid(row=2,column=2)

# ----------------------------------------------------
owner_name = Label(root,text="Abhishek Manojkumar", font="Ariel 8", fg="yellow", bg="gray")
owner_name.grid(row=7, column=0, columnspan=3, pady=5)

root.mainloop()