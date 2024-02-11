from tkinter import *
from tkinter import ttk
from tkinter import messagebox

import pymysql
import re


class Student:
    # -------- Create the main window of the application --------
    def __init__(self, app):
        self.app = app
        self.app.geometry("1368x768")
        self.app.title("Student Management Application")
        self.app.configure(background="#0B132B")
        self.app.resizable(False, False)
        title = Label(
            self.app,
            text="(Student Registration Application)",
            bg="#3A506B",
            font=("GillSans", 18),
            fg="white",
        )
        title.pack(fill=X)

        # -------- Variables --------
        self.id = StringVar()
        self.name = StringVar()
        self.email = StringVar()
        self.phone = StringVar()
        self.gender = StringVar()
        self.address = StringVar()
        self.delete = StringVar()
        self.search = StringVar()
        self.search_by = StringVar()

        # -------- Application control tools --------
        Frame_Control = Frame(self.app, bg="#1C2541")
        Frame_Control.place(x=15, y=50, width=200, height=350)

        label_id = Label(Frame_Control, text="Student ID", fg="#FFFFFF", bg="#1C2541")
        label_id.pack()
        id_entry = Entry(Frame_Control, textvariable=self.id, bd="3", justify="left")
        id_entry.pack()

        label_name = Label(
            Frame_Control, fg="#FFFFFF", bg="#1C2541", text="Student Name"
        )
        label_name.pack()
        name_entry = Entry(Frame_Control, textvariable=self.name, bd="3")
        name_entry.pack()

        label_email = Label(
            Frame_Control, fg="#FFFFFF", bg="#1C2541", text="Student Email"
        )
        label_email.pack()
        email_entry = Entry(Frame_Control, textvariable=self.email, bd="3")
        email_entry.pack()

        label_phone = Label(
            Frame_Control, fg="#FFFFFF", bg="#1C2541", text="Student Phone"
        )
        label_phone.pack()
        phone_entry = Entry(Frame_Control, textvariable=self.phone, bd="3")
        phone_entry.pack()

        label_gender = Label(Frame_Control, fg="#FFFFFF", bg="#1C2541", text="Gender")
        label_gender.pack()
        combo_gender = ttk.Combobox(Frame_Control, textvariable=self.gender)
        combo_gender["value"] = ("Male", "Female")
        combo_gender.pack()

        label_address = Label(
            Frame_Control,
            fg="#FFFFFF",
            bg="#1C2541",
            text="Student Address",
        )
        label_address.pack()
        address_entry = Entry(
            Frame_Control, textvariable=self.address, bd="3", justify="center"
        )
        address_entry.pack()

        label_delete = Label(
            Frame_Control, fg="black", bg="#5BC0BE", text="Delete Student By Name"
        )
        label_delete.pack(pady=10)
        delete_entry = Entry(Frame_Control, textvariable=self.delete, bd="3")
        delete_entry.pack(pady=0)

        # -------- Buttons --------
        btn_frame = Frame(self.app, bg="#1C2541")
        btn_frame.place(x=15, y=410, width=200, height=260)
        title1 = Label(
            btn_frame, text="Dashboard", font=("GillSans", 18), fg="white", bg="#3A506B"
        )
        title1.pack(fill=X)

        # Add a Student
        add_btn = Button(
            btn_frame, text="Add a student", bg="#5BC0BE", command=self.add_student
        )
        add_btn.place(x=35, y=40, width=130, height=30)

        # Delete a Student
        delete_btn = Button(
            btn_frame,
            text="Delete a student",
            bg="#5BC0BE",
            command=self.delete_student,
        )
        delete_btn.place(x=35, y=74, width=130, height=30)

        # update Student data
        update_btn = Button(
            btn_frame,
            text="Update student data",
            bg="#5BC0BE",
            command=self.update_student_data,
        )
        update_btn.place(x=35, y=108, width=130, height=30)

        # Empty fields
        clear_btn = Button(
            btn_frame, text="Dump fields", bg="#5BC0BE", command=self.clear
        )
        clear_btn.place(x=35, y=142, width=130, height=30)

        # About us
        about_btn = Button(
            btn_frame, text="About us", bg="#5BC0BE", command=self.about_us
        )
        about_btn.place(x=35, y=176, width=130, height=30)

        # Exit the program
        exit_btn = Button(btn_frame, text="Exit", bg="#5BC0BE", command=self.exit)
        exit_btn.place(x=35, y=210, width=130, height=30)

        # -------- Searching --------
        search_frame = Frame(self.app, bg="#1C2541")
        search_frame.place(x=230, y=50, width=1110, height=50)

        label_search = Label(
            search_frame, text="Search for a student", bg="#1C2541", fg="#FFFFFF"
        )
        label_search.place(x=10, y=10)

        combo_search = ttk.Combobox(
            search_frame, textvariable=self.search_by, justify="left"
        )
        combo_search["value"] = ("ID", "Name", "Phone", "Email")
        combo_search.place(x=130, y=10)

        search_entry = Entry(
            search_frame, justify="left", textvariable=self.search, bd=3
        )
        search_entry.place(x=280, y=10, width=150)

        search_btn = Button(
            search_frame, text="Search", bg="#5BC0BE", command=self.search_function
        )
        search_btn.place(x=450, y=10, width=80)

        # -------- Where the data is displayed --------
        data_frame = Frame(self.app, bg="#1C2541")
        data_frame.place(x=230, y=110, width=1110, height=560)

        scroll_x = Scrollbar(data_frame, orient=HORIZONTAL)
        scroll_y = Scrollbar(data_frame, orient=VERTICAL)

        # Tree View
        self.student_table = ttk.Treeview(
            data_frame,
            columns=("ID", "Name", "Email", "Phone", "Gender", "Address"),
            xscrollcommand=scroll_x.set,
            yscrollcommand=scroll_y.set,
        )
        self.student_table.place(x=0, y=0, width=1090, height=540)
        scroll_x.pack(side=BOTTOM, fill=X)
        scroll_y.pack(side=RIGHT, fill=Y)
        # scroll_x.config(command=self.student_table.xview)
        # scroll_y.config(command=self.student_table.yview)

        self.student_table["show"] = "headings"
        self.student_table.heading("ID", text="ID")
        self.student_table.heading("Name", text="Student Name")
        self.student_table.heading("Email", text="Email")
        self.student_table.heading("Phone", text="Phone")
        self.student_table.heading("Gender", text="Gender")
        self.student_table.heading("Address", text="Address")

        self.student_table.column("ID", width=10)
        self.student_table.column("Name", width=100)
        self.student_table.column("Email", width=100)
        self.student_table.column("Phone", width=65)
        self.student_table.column("Gender", width=20)
        self.student_table.column("Address", width=120)
        self.student_table.bind("<ButtonRelease-1>", self.get_cursor)
        self.fetch_all()

    # Connecting the database and entering data
    def add_student(self):

        # Verify that the email is valid
        email = self.email.get()
        if not re.match(r"^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$", email):
            messagebox.showerror("Error", "Please enter a valid email address")
            return

        connection = pymysql.Connect(
            host="localhost", user="root", password="", database="students"
        )
        cursor = connection.cursor()
        cursor.execute(
            "insert into stu values(%s,%s,%s,%s,%s,%s)",
            (
                self.id.get(),
                self.name.get().title(),
                email,
                self.phone.get(),
                self.gender.get(),
                self.address.get(),
            ),
        )
        connection.commit()
        self.fetch_all()
        self.clear()
        connection.close()

    def fetch_all(self):
        connection = pymysql.connect(
            host="localhost", user="root", password="", database="students"
        )
        cursor = connection.cursor()
        cursor.execute("select * from stu")
        rows = cursor.fetchall()
        if len(rows) != 0:
            self.student_table.delete(*self.student_table.get_children())
            for row in rows:
                self.student_table.insert("", END, value=row)
            connection.commit()
        connection.close()

    # Delete a student from the database
    def delete_student(self):
        connection = pymysql.connect(
            host="localhost", user="root", password="", database="students"
        )
        cursor = connection.cursor()
        cursor.execute("delete from stu where name=%s", self.delete.get())
        connection.commit()
        self.fetch_all()
        connection.close()

    def clear(self):
        self.id.set("")
        self.name.set("")
        self.email.set("")
        self.phone.set("")
        self.gender.set("")
        self.address.set("")
        self.delete.set("")

    def get_cursor(self, event):
        cursor_row = self.student_table.focus()
        contents = self.student_table.item(cursor_row)
        row = contents["values"]
        self.id.set(row[0])
        self.name.set(row[1])
        self.email.set(row[2])
        self.phone.set(row[3])
        self.gender.set(row[4])
        self.address.set(row[5])

    # Update student data in the database
    def update_student_data(self):
        connection = pymysql.Connect(
            host="localhost", user="root", password="", database="students"
        )
        cursor = connection.cursor()
        cursor.execute(
            "update stu set name=%s,email=%s,phone=%s,gender=%s,address=%s where id=%s",
            (
                self.name.get().title(),
                self.email.get(),
                self.phone.get(),
                self.gender.get(),
                self.address.get(),
                self.id.get(),
            ),
        )
        connection.commit()
        self.fetch_all()
        self.clear()
        connection.close()

    def search_function(self):
        connection = pymysql.connect(
            host="localhost", user="root", password="", database="students"
        )
        cursor = connection.cursor()
        cursor.execute(
            "select * from stu where "
            + str(self.search_by.get())
            + " LIKE '%"
            + str(self.search.get())
            + "%'"
        )

        rows = cursor.fetchall()
        if len(rows) != 0:
            self.student_table.delete(*self.student_table.get_children())
            for row in rows:
                self.student_table.insert("", END, value=row)
            connection.commit()
        connection.close()

    def about_us(self):
        messagebox.showinfo("About Us", "Developer Rashed Sari\n***Version 1.0***")

    def exit(self):
        app.quit()


app = Tk()
object = Student(app)
app.mainloop()
