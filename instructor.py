import tkinter as tk
from tkinter import ttk, messagebox
import sqlite3
from time import sleep


class Instructor:
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

        # Create or open the database
        self.db = sqlite3.connect('test3.db')
        self.cursor = self.db.cursor()
        self.closew = False

        # Create or open the student table

        # GUI elements
        label_id_text = "          Instructor ID:"
        self.label_id = tk.Label(self.root, text=label_id_text, bg="#3498db", fg="white")
        self.label_id.grid(row=0, column=0, padx=10, pady=(30, 10))

        self.entry_id = tk.Entry(self.root, width=20)
        self.entry_id.grid(row=0, column=1, padx=10, pady=(30, 10))

        label_name_text = "     Instructor Name:"
        self.label_name = tk.Label(self.root, text=label_name_text, bg="#3498db", fg="white")
        self.label_name.grid(row=1, column=0, padx=10, pady=10)

        self.entry_name = tk.Entry(self.root, width=20)
        self.entry_name.grid(row=1, column=1, padx=10, pady=10)

        label_dept_text = "              Department:"
        self.label_dept = tk.Label(self.root, text=label_dept_text, bg="#3498db", fg="white")
        self.label_dept.grid(row=2, column=0, padx=10, pady=10)

        self.entry_dept = tk.Entry(self.root, width=20)
        self.entry_dept.grid(row=2, column=1, padx=10, pady=10)

        label_sal_text = "       Instructor Salary:"
        self.label_sal = tk.Label(self.root, text=label_sal_text, bg="#3498db", fg="white")
        self.label_sal.grid(row=3, column=0, padx=10, pady=10)

        self.entry_sal = tk.Entry(self.root, width=20)
        self.entry_sal.grid(row=3, column=1, padx=10, pady=10)

        self.btn_insert = tk.Button(self.root, text="Insert Instructors", command=self.insert_instructor, bg="#8e44ad",
                                    fg="white", padx=10, pady=5)
        self.btn_insert.grid(row=4, column=0, columnspan=2, pady=10)

        self.btn_search = tk.Button(self.root, text="Search Instructors", command=self.search_instructor, bg="#8e44ad",
                                    fg="white", padx=10, pady=5)
        self.btn_search.grid(row=5, column=0, columnspan=2, pady=10)

        self.btn_delete = tk.Button(self.root, text="Delete Instructors", command=self.delete_instructor, bg="#8e44ad",
                                    fg="white", padx=10, pady=5)
        self.btn_delete.grid(row=6, column=0, columnspan=2, pady=10)

        self.btn_list = tk.Button(self.root, text="List All Instructors", command=self.list_instructors, bg="#8e44ad",
                                  fg="white", padx=10, pady=5)
        self.btn_list.grid(row=8, column=0, columnspan=2, pady=10)

        self.btn_delete = tk.Button(self.root, text="Update Instructor", command=self.update_instructor, bg="#8e44ad",
                                    fg="white", padx=10, pady=5)
        self.btn_delete.grid(row=7, column=0, columnspan=2, pady=10)

        self.tree = ttk.Treeview(self.root, columns=("ID", "Name", "Department", "Salary"), show="headings")
        self.tree.heading("ID", text="ID")
        self.tree.heading("Name", text="Name")
        self.tree.heading("Department", text="Department")
        self.tree.heading("Salary", text="Salary")
        self.tree.grid(row=9, column=0, columnspan=2, padx=50, pady=50)

    def close(self):
        self.root.mainloop()
    def on_close(self):
        result = messagebox.askokcancel("Close", "Do you really want to close the window?")
        if result:
            self.closew = True
            self.root.destroy()

    def r(self):
        return self.closew
    def insert_instructor(self):
        # Get values from entry fields
        i_id = self.entry_id.get()
        i_name = self.entry_name.get()
        dept_name = self.entry_dept.get()
        i_salary = self.entry_sal.get()

        # Validate student ID
        if not i_id.isdigit() or len(i_id) != 6:
            messagebox.showerror("Error", "Instructor ID must be a 5-digit numeric value.")
            return

        # Validate total credit
        if not i_salary.isdigit() or int(i_salary) < 0:
            messagebox.showerror("Error", "Salary must be a non-negative numeric value.")
            return

        # Check for empty values
        if not i_name or not dept_name:
            messagebox.showerror("Error", "Please fill in all fields.")
            return

        # Check if the department exists
        self.cursor.execute("SELECT * FROM department WHERE dept_name=?", (dept_name,))
        existing_dept = self.cursor.fetchone()

        if not existing_dept:
            messagebox.showerror("Error", "Department does not exist. Please choose a valid department.")
            return

        # Check if the student ID already exists
        self.cursor.execute("SELECT * FROM instructor WHERE ID=?", (i_id,))
        existing_i = self.cursor.fetchone()

        if existing_i:
            messagebox.showerror("Error", "Instructor with the given ID already exists. Please choose a different ID.")
        else:
            # Insert the new student
            self.cursor.execute("INSERT INTO instructor VALUES (?, ?, ?, ?)",
                                (i_id, i_name, dept_name, i_salary))
            self.db.commit()

            messagebox.showinfo("Success", "Instructor inserted successfully!")
            self.clear_entries()
            self.list_instructors()

    def search_instructor(self):
        i_id = self.entry_id.get()

        self.cursor.execute("SELECT * FROM instructor WHERE ID=?", (i_id,))
        instructor = self.cursor.fetchone()

        if instructor:
            self.entry_name.delete(0, tk.END)
            self.entry_name.insert(0, instructor[1])

            self.entry_dept.delete(0, tk.END)
            self.entry_dept.insert(0, instructor[2])

            self.entry_sal.delete(0, tk.END)
            self.entry_sal.insert(0, instructor[3])
        else:
            messagebox.showinfo("Instructor Not Found", "Instructor with given ID not found.")
        # if student:
        #     info_message = f"Student ID: {student[0]}\nName: {student[1]}\nDepartment: {student[2]}\nCredits: {student[3]}"
        #     messagebox.showinfo("Student Information", info_message)
        # else:
        #     messagebox.showinfo("Student Not Found", "Student with given ID not found.")

    def delete_instructor(self):
        i_id = self.entry_id.get()

        # Check if the student ID is not specified
        if not i_id:
            messagebox.showerror("Error", "Please specify a Instructor ID for deletion.")
            return

        # Check if the student ID exists
        self.cursor.execute("SELECT * FROM instructor WHERE ID=?", (i_id,))
        existing_i = self.cursor.fetchone()

        if not existing_i:
            messagebox.showerror("Error", f"Instructor with ID {i_id} does not exist.")
            return

        # Ask for confirmation before deletion
        confirmation = messagebox.askyesno("Confirmation", f"Do you want to delete Instructor with ID {i_id}?")

        if confirmation:
            self.cursor.execute("DELETE FROM instructor  WHERE ID=?", (i_id,))
            self.db.commit()
            messagebox.showinfo("Success", "Instructor deleted successfully!")
            self.clear_entries()
            self.list_instructors()

    def update_instructor(self):
        i_id = self.entry_id.get()

        self.cursor.execute("SELECT * FROM instructor WHERE ID=?", (i_id,))
        instructor = self.cursor.fetchone()
        if instructor:
            new_id = self.entry_id.get()
            instructor_name = self.entry_name.get()
            dept_name = self.entry_dept.get()
            sal = self.entry_sal.get()
            self.cursor.execute("SELECT * FROM department WHERE dept_name=?", (dept_name,))
            existing_dept = self.cursor.fetchone()

            if not existing_dept:
                messagebox.showerror("Error", "Department does not exist. Please choose a valid department.")
                return

            self.cursor.execute("UPDATE instructor SET ID = ?, name = ?, dept_name = ?, salary = ?  WHERE ID = ? ",
                                (new_id, instructor_name, dept_name, sal, i_id))
            self.db.commit()

            messagebox.showinfo("Success", "    instructor updated successfully!")
            self.clear_entries()
            self.list_instructors()
        else:
            messagebox.showerror("Error", "you can not change the student id")

    def list_instructors(self):
        self.tree.delete(*self.tree.get_children())  # Clear existing data in the Treeview

        self.cursor.execute("SELECT * FROM instructor")
        instructors = self.cursor.fetchall()

        for instructor in instructors:
            self.tree.insert("", "end", values=instructor)

    def clear_entries(self):
        self.entry_id.delete(0, tk.END)
        self.entry_name.delete(0, tk.END)
        self.entry_dept.delete(0, tk.END)
        self.entry_sal.delete(0, tk.END)


if __name__ == "__main__":

    app = Instructor()
    app.close()
