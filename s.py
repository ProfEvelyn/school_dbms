import tkinter as tk
from tkinter import ttk, messagebox
import sqlite3
from time import sleep
#
# colors:
# 2E4374
# 4B527E
# 7C81AD
# 7C81AD
class StudentManagementApp:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Student Management System")
        self.root.iconbitmap('icons/eul.ico')
        screen_width = self.root.winfo_screenwidth()
        screen_height = self.root.winfo_screenheight()

        # Set the window dimensions to match the screen resolution
        self.root.geometry(f"{screen_width}x{screen_height}+0+0")
        self.root.protocol("WM_DELETE_WINDOW", self.on_close)
        # self.root.geometry("1000x600")
        self.root.configure(bg="#2E4374")
        self.frame = tk.Frame(self.root, bg="#2E4374", bd=2, relief=tk.GROOVE)
        self.frame.pack(padx=20, pady=20, fill=tk.BOTH, expand=True)

        # Create or open the databas
        self.db = sqlite3.connect('test3.db')
        self.cursor = self.db.cursor()
        self.closew = False
        # Create or open the student table

        labels_bg_color = "#4B527E"
        entry_bg_color = "#7C81AD"
        buttons_bg_color = "#4B527E"

        self.label_id = tk.Label(self.frame, text="Student ID:", bg=labels_bg_color, fg="white")
        self.label_id.grid(row=0, column=0, padx=10, pady=(10, 10), sticky='w')

        self.entry_id = tk.Entry(self.frame, width=20, bg=entry_bg_color)
        self.entry_id.grid(row=0, column=1, padx=50, pady=(30, 10))

        self.label_name = tk.Label(self.frame, text="Student Name:", bg=labels_bg_color, fg="white")
        self.label_name.grid(row=1, column=0, padx=10, pady=10)

        self.entry_name = tk.Entry(self.frame, width=20, bg=entry_bg_color)
        self.entry_name.grid(row=1, column=1, padx=10, pady=10)

        self.label_dept = tk.Label(self.frame, text="Department:", bg=labels_bg_color, fg="white")
        self.label_dept.grid(row=2, column=0, padx=10, pady=10)

        self.entry_dept = tk.Entry(self.frame, width=20, bg=entry_bg_color)
        self.entry_dept.grid(row=2, column=1, padx=10, pady=10)

        self.label_cred = tk.Label(self.frame, text="Total Credits:", bg=labels_bg_color, fg="white")
        self.label_cred.grid(row=3, column=0, padx=10, pady=10)

        self.entry_cred = tk.Entry(self.frame, width=20, bg=entry_bg_color)
        self.entry_cred.grid(row=3, column=1, padx=10, pady=10)

        # Buttons
        button_fg_color = "white"
        self.btn_insert = tk.Button(self.frame, text="Insert Student", command=self.insert_student, bg=buttons_bg_color,
                                    fg=button_fg_color, relief=tk.GROOVE, bd=2, padx=10, pady=5, borderwidth=2,
                                    highlightthickness=0, cursor="hand2")
        self.btn_insert.grid(row=4, column=0, columnspan=2, pady=10)

        self.btn_search = tk.Button(self.frame, text="Search Student", command=self.search_student, bg=buttons_bg_color,
                                    fg=button_fg_color, relief=tk.GROOVE, bd=2, padx=10, pady=5, borderwidth=2,
                                    highlightthickness=0, cursor="hand2")
        self.btn_search.grid(row=5, column=0, columnspan=2, pady=10)

        self.btn_delete = tk.Button(self.frame, text="Delete Student", command=self.delete_student, bg=buttons_bg_color,
                                    fg=button_fg_color, relief=tk.GROOVE, bd=2, padx=10, pady=5, borderwidth=2,
                                    highlightthickness=0, cursor="hand2")
        self.btn_delete.grid(row=6, column=0, columnspan=2, pady=10)

        self.btn_list = tk.Button(self.frame, text="List All Students", command=self.list_students, bg=buttons_bg_color,
                                  fg=button_fg_color, relief=tk.GROOVE, bd=2, padx=10, pady=5, borderwidth=2,
                                  highlightthickness=0, cursor="hand2")
        self.btn_list.grid(row=8, column=0, columnspan=2, pady=10)

        self.btn_delete = tk.Button(self.frame, text="Update Student", command=self.update_student, bg=buttons_bg_color,
                                    fg=button_fg_color, relief=tk.GROOVE, bd=2, padx=10, pady=5, borderwidth=2,
                                    highlightthickness=0, cursor="hand2")
        self.btn_delete.grid(row=7, column=0, columnspan=2, pady=10)

        # Treeview
        self.tree = ttk.Treeview(self.frame, columns=("ID", "Name", "Department", "Total Credits"), show="headings",
                                 height=40)
        self.tree.heading("ID", text="ID")
        self.tree.heading("Name", text="Name")
        self.tree.heading("Department", text="Department")
        self.tree.heading("Total Credits", text="Total Credits")
        self.tree.grid(row=0, column=2,columnspan = 2, rowspan=20,padx = (200,0), pady = 10, sticky='e')

            # Configure column weights
        self.root.grid_columnconfigure(0, weight=1)
        self.root.grid_columnconfigure(2, weight=1)

        # Add a vertical line

    def close(self):
        self.root.mainloop()

    def insert_student(self):
        # Get values from entry fields
        student_id = self.entry_id.get()
        student_name = self.entry_name.get()
        dept_name = self.entry_dept.get()
        tot_cred = self.entry_cred.get()


        # Validate student ID
        if not student_id.isdigit() or len(student_id) != 5:
            messagebox.showerror("Error", "Student ID must be a 5-digit numeric value.")
            return

        # Validate total credit
        if not tot_cred.isdigit() or int(tot_cred) < 0:
            messagebox.showerror("Error", "Total credits must be a non-negative numeric value.")
            return

        # Check for empty values
        if not student_name or not dept_name:
            messagebox.showerror("Error", "Please fill in all fields.")
            return

        # Check if the department exists
        self.cursor.execute("SELECT * FROM department WHERE dept_name=?", (dept_name,))
        existing_dept = self.cursor.fetchone()

        if not existing_dept:
            messagebox.showerror("Error", "Department does not exist. Please choose a valid department.")
            return

        # Check if the student ID already exists
        self.cursor.execute("SELECT * FROM student WHERE ID=?", (student_id,))
        existing_student = self.cursor.fetchone()

        if existing_student:
            messagebox.showerror("Error", "Student with the given ID already exists. Please choose a different ID.")
        else:
            # Insert the new student
            self.cursor.execute("INSERT INTO student VALUES (?, ?, ?, ?)",
                                (student_id, student_name, dept_name, tot_cred))
            self.db.commit()

            messagebox.showinfo("Success", "Student inserted successfully!")
            self.clear_entries()
            self.list_students()

    def search_student(self):
        student_id = self.entry_id.get()

        self.cursor.execute("SELECT * FROM student WHERE ID=?", (student_id,))
        student = self.cursor.fetchone()

        if student:
            self.entry_name.delete(0, tk.END)
            self.entry_name.insert(0, student[1])

            self.entry_dept.delete(0, tk.END)
            self.entry_dept.insert(0, student[2])

            self.entry_cred.delete(0, tk.END)
            self.entry_cred.insert(0, student[3])
        else:
            messagebox.showinfo("Student Not Found", "Student with given ID not found.")
        # if student:
        #     info_message = f"Student ID: {student[0]}\nName: {student[1]}\nDepartment: {student[2]}\nCredits: {student[3]}"
        #     messagebox.showinfo("Student Information", info_message)
        # else:
        #     messagebox.showinfo("Student Not Found", "Student with given ID not found.")

    def delete_student(self):
        student_id = self.entry_id.get()

        # Check if the student ID is not specified
        if not student_id:
            messagebox.showerror("Error", "Please specify a Student ID for deletion.")
            return

        # Check if the student ID exists
        self.cursor.execute("SELECT * FROM student WHERE ID=?", (student_id,))
        existing_student = self.cursor.fetchone()

        if not existing_student:
            messagebox.showerror("Error", f"Student with ID {student_id} does not exist.")
            return

        # Ask for confirmation before deletion
        confirmation = messagebox.askyesno("Confirmation", f"Do you want to delete student with ID {student_id}?")

        if confirmation:
            self.cursor.execute("DELETE FROM student WHERE ID=?", (student_id,))
            self.db.commit()
            messagebox.showinfo("Success", "Student deleted successfully!")
            self.clear_entries()
            self.list_students()
    def update_student(self):
        student_id = self.entry_id.get()

        self.cursor.execute("SELECT * FROM student WHERE ID=?", (student_id,))
        student = self.cursor.fetchone()
        if student:
            new_id = self.entry_id.get()
            student_name = self.entry_name.get()
            dept_name = self.entry_dept.get()
            tot_cred = self.entry_cred.get()

            self.cursor.execute("SELECT * FROM department WHERE dept_name=?", (dept_name,))
            existing_dept = self.cursor.fetchone()

            if not existing_dept:
                messagebox.showerror("Error", "Department does not exist. Please choose a valid department.")
                return

            self.cursor.execute("UPDATE student SET ID = ?, name = ?, dept_name = ?, tot_cred = ?  WHERE ID = ? ",
                                (new_id, student_name, dept_name, tot_cred, student_id))
            self.db.commit()

            messagebox.showinfo("Success", "Student updated successfully!")
            self.clear_entries()
            self.list_students()
        else:
            messagebox.showerror("Error", "you can not change the student id")
            return

    def list_students(self):
        self.tree.delete(*self.tree.get_children())  # Clear existing data in the Treeview

        self.cursor.execute("SELECT * FROM student")
        students = self.cursor.fetchall()

        for student in students:
            self.tree.insert("", "end", values=student)

    def clear_entries(self):
        self.entry_id.delete(0, tk.END)
        self.entry_name.delete(0, tk.END)
        self.entry_dept.delete(0, tk.END)
        self.entry_cred.delete(0, tk.END)

    def on_close(self):
        result = messagebox.askokcancel("Close", "Do you really want to close the window?")
        if result:
            self.closew = True
            self.root.destroy()

    def r(self):
        return self.closew

if __name__ == "__main__":
    app = StudentManagementApp()
    app.close()

