import tkinter as tk
from tkinter import messagebox, PhotoImage
from student import StudentManagementApp
from department import Department
from course import Course
from instructor import Instructor

def w_close():
    result = messagebox.askokcancel("Close", "Do you really want to close the window?")
    if result:
        root.destroy()

root = tk.Tk()
root.title("Student Management System")
root.iconbitmap('icons/eul.ico')  # Change the path to your icon file

screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()

# Set the window dimensions to match the screen resolution
root.geometry(f"{screen_width}x{screen_height}+0+0")

# Set the background color to blue
root.protocol("WM_DELETE_WINDOW", w_close)

# Replace 'pic.png' with your image file path
background_image = PhotoImage(file="pic.png")
background_label = tk.Label(root, image=background_image)
background_label.place(relwidth=1, relheight=1)

def open_app(app_class):
    global close
    root.withdraw()
    app = app_class()

    # Wait for the app window to be closed
    app.root.wait_window(app.root)

    if app.r():
        root.deiconify()

def open_student_management():
    open_app(StudentManagementApp)

def open_course():
    open_app(Course)

def open_department():
    open_app(Department)

def open_instructor():
    open_app(Instructor)

main_frame = tk.Frame(root, bg="#2E4374")  # Use the dark blue color from the palette
main_frame.grid(row=1, column=0, padx=50, pady=50)

welcome_label = tk.Label(root, text="WELCOME TO THE STUDENT MANAGEMENT SYSTEM", font=("Arial", 20, "bold"), bg="#2E4374", fg="white")  # Use a larger, bold font
welcome_label.grid(row=0, column=0, pady=20)

btn_insert = tk.Button(main_frame, text="Student", command=open_student_management, bg="#7C81AD", fg="white", padx=20, pady=10, width=20, bd=2, relief=tk.GROOVE, cursor="hand2")  # Use a lighter blue color and add some styling
btn_insert.grid(row=0, column=0, pady=10)

btn_search = tk.Button(main_frame, text="Course", command=open_course, bg="#7C81AD", fg="white", padx=20, pady=10, width=20, bd=2, relief=tk.GROOVE, cursor="hand2")
btn_search.grid(row=1, column=0, pady=10)

btn_delete = tk.Button(main_frame, text="Department", command=open_department, bg="#7C81AD", fg="white", padx=20, pady=10, width=20, bd=2, relief=tk.GROOVE, cursor="hand2")
btn_delete.grid(row=2, column=0, pady=10)

btn_list = tk.Button(main_frame, text="Instructor", command=open_instructor, bg="#7C81AD", fg="white", padx=20, pady=10, width=20, bd=2, relief=tk.GROOVE, cursor="hand2")
btn_list.grid(row=3, column=0, pady=10)

root.mainloop()
