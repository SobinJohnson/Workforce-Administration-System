import tkinter as tk
from tkinter import messagebox
import pandas as pd
from PIL import ImageTk, Image

class Employee:
    def __init__(self, id, name, department, work_hour,efficiency):
        self.id = id
        self.name = name
        self.department = department
        self.work_hour = work_hour
        self.efficiency=efficiency

class LoginWindow:
    def __init__(self, master):
        self.master = master
        self.master.title("Login Page")
        self.master.geometry("300x225")

        # Set color palette
        self.bg_color = "#E4E4E4"  # light gray
        self.label_color = "#333333"  # dark gray
        self.entry_color = "#FFFFFF"  # white
        self.button_color = "#19825F"  # green

        # Set styles
        self.master.configure(bg=self.bg_color)
        self.label_style = {'bg': self.bg_color, 'fg': self.label_color, 'font': ('Helvetica', 12)}
        self.entry_style = {'bg': self.entry_color, 'fg': self.label_color, 'font': ('Helvetica', 12)}
        self.button_style = {'bg': self.button_color, 'fg': 'white', 'font': ('Helvetica', 12)}

        # Set padding and spacing
        self.label_padding = (10, 10)
        self.entry_padding = (0, 10)
        self.button_padding = (10, 10)
        self.spacing = 6

        # Username label and entry
        self.username_label = tk.Label(self.master, text="Username:", **self.label_style)
        self.username_label.pack(pady=self.label_padding[1], padx=self.label_padding[0])
        self.username_entry = tk.Entry(self.master, **self.entry_style,borderwidth=5, relief="flat")
        self.username_entry.pack(pady=self.entry_padding[1], padx=self.entry_padding[0])

        # Password label and entry
        self.password_label = tk.Label(self.master, text="Password:", **self.label_style)
        self.password_label.pack(pady=self.label_padding[1], padx=self.label_padding[0])
        self.password_entry = tk.Entry(self.master, show="*", **self.entry_style,borderwidth=5, relief="flat")
        self.password_entry.pack(pady=self.entry_padding[1], padx=self.entry_padding[0])

        # Login button
        self.login_button = tk.Button(self.master, text="Login", command=self.login, **self.button_style,activebackground="#126D55",borderwidth=5, relief="flat")
        self.login_button.pack(pady=self.button_padding[1], padx=self.button_padding[0])

        # Add spacing between elements
        for child in self.master.winfo_children():
            if isinstance(child, tk.Label) or isinstance(child, tk.Entry) or isinstance(child, tk.Button):
                child.pack_configure(pady=self.spacing, padx=self.spacing)


    def login(self):
        # Check if the credentials are valid
        username = self.username_entry.get()
        password = self.password_entry.get()
        if username == "admin" and password == "pass":
            # If the credentials are valid, close this window and open the main window
            self.master.destroy()
            MonthlyInputWindow()
        else:
            # If the credentials are invalid, show an error message
            messagebox.showerror("Error", "Invalid username or password")
    def run(self):
        self.master.mainloop()

class MonthlyInputWindow:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Monthly Input")
        self.root.geometry("300x300")

        # Set color palette
        self.bg_color = "#E4E4E4"  # light gray
        self.label_color = "#333333"  # dark gray
        self.entry_color = "#FFFFFF"  # white
        self.button_color = "#19825F"  # green

        # Set styles
        self.root.configure(bg=self.bg_color)
        self.label_style = {'bg': self.bg_color, 'fg': self.label_color, 'font': ('Helvetica', 12)}
        self.entry_style = {'bg': self.entry_color, 'fg': self.label_color, 'font': ('Helvetica', 12)}
        self.button_style = {'bg': self.button_color, 'fg': 'white', 'font': ('Helvetica', 13)}

        # Set padding and spacing
        self.label_padding = (10, 10)
        self.entry_padding = (0, 10)
        self.button_padding = (10, 12)
        self.spacing = 6

        self.MONTHS = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]

        # Month label and dropdown
        self.month_label = tk.Label(self.root, text="Month:", **self.label_style)
        self.month_label.pack(pady=self.label_padding[1], padx=self.label_padding[0])
        self.month_var = tk.StringVar(value=self.MONTHS[0])
        self.month_dropdown = tk.OptionMenu(self.root, self.month_var, *self.MONTHS)
        self.month_dropdown.configure(width=15,bg=self.entry_color,font=('Helvetica', 12), fg=self.label_color, activebackground=self.button_color, activeforeground="white", bd=1, relief="flat")
        self.month_dropdown['menu'].config(bg=self.entry_color, fg=self.label_color, font=('Helvetica', 12))
        self.month_dropdown.pack(pady=self.entry_padding[1], padx=self.entry_padding[0])

        # Year label and entry
        self.year_label = tk.Label(self.root, text="Year (e.g. 2022):", **self.label_style)
        self.year_label.pack(pady=self.label_padding[1], padx=self.label_padding[0])
        self.year_entry = tk.Entry(self.root, **self.entry_style,borderwidth=5, relief="flat")
        self.year_entry.pack(pady=self.entry_padding[1], padx=self.entry_padding[0])

        # Work hours label and entry
        self.work_hours_label = tk.Label(self.root, text="Number of work hours:", **self.label_style)
        self.work_hours_label.pack(pady=self.label_padding[1], padx=self.label_padding[0])
        self.work_hours_entry = tk.Entry(self.root, **self.entry_style,borderwidth=5, relief="flat")
        self.work_hours_entry.pack(pady=self.entry_padding[1], padx=self.entry_padding[0])

        # Submit button
        self.submit_button = tk.Button(self.root, width=15,text="Submit", command=self.submit, **self.button_style,borderwidth=5, relief="flat",activebackground="#126D55")
        self.submit_button.pack(pady=self.button_padding[1], padx=self.button_padding[0])

        # Add spacing between elements
        for child in self.root.winfo_children():
            if isinstance(child, tk.Label) or isinstance(child, tk.Entry) or isinstance(child, tk.Button):
                child.pack_configure(pady=self.spacing, padx=self.spacing)

    def submit(self):
        # Get the input values
        month = self.month_var.get()
        year = self.year_entry.get()
        work_hours = self.work_hours_entry.get()
        self.root.destroy()
        # Send the input values to the WorkforceAdministrationSystem
        WorkforceAdministrationSystem(month=month, year=year, m_work_hours=work_hours)

        # Close the window
        self.root.destroy()

    def run(self):
        self.root.mainloop()


class WorkforceAdministrationSystem:
    def __init__(self,month,year,m_work_hours):
        self.employee_data = []

        self.root = tk.Tk()
        self.root.title("Workforce Administration System")
        self.root.geometry("500x550")
        self.month=month
        self.year=year
        self.m_work_hours=m_work_hours
        

        # Set color palette
        self.bg_color = "#E4E4E4"  # light gray
        self.label_color = "#333333"  # dark gray
        self.entry_color = "#FFFFFF"  # white
        self.button_color = "#19825F"  # green

        # Set styles
        self.label_style = {'bg': self.bg_color, 'fg': self.label_color, 'font': ('Helvetica', 12)}
        self.entry_style = {'bg': self.entry_color, 'fg': self.label_color, 'font': ('Helvetica', 12)}
        self.button_style = {'bg': self.button_color, 'fg': 'white','font': ('Helvetica', 12)}

        # Set padding and spacing
        self.label_padding = (10, 10)
        self.entry_padding = (0, 10)
        self.button_padding = (10, 10)
        self.spacing = 6
        
        self.image_file = "bg_image.png"
        self.image = Image.open("bg_image.png")
        self.photo = ImageTk.PhotoImage(self.image)

        # Create label with background image
        self.background_label = tk.Label(self.root, image=self.photo)
        self.background_label.place(x=0, y=0, relwidth=1, relheight=1)
        self.background_label.image = self.photo
        self.background_label.lower()
        

        # Employee ID label and entry
        self.employee_id_label = tk.Label(self.root, text="Employee ID:", **self.label_style)
        self.employee_id_label.pack(side="top", padx=self.spacing, pady=self.spacing)

        self.employee_id_entry = tk.Entry(self.root, **self.entry_style,borderwidth=5, relief="flat")
        self.employee_id_entry.pack(side="top", padx=self.spacing, pady=self.spacing)

        # Employee Name label and entry
        self.employee_name_label = tk.Label(self.root, text="Employee Name:", **self.label_style)
        self.employee_name_label.pack(side="top", padx=self.spacing, pady=self.spacing)

        self.employee_name_entry = tk.Entry(self.root, **self.entry_style, borderwidth=5, relief="flat")
        self.employee_name_entry.pack(side="top", padx=self.spacing, pady=self.spacing)

        # Department label and entry
        self.department_label = tk.Label(self.root, text="Department:", **self.label_style)
        self.department_label.pack(side="top", padx=self.spacing, pady=self.spacing)

        self.department_entry = tk.Entry(self.root, **self.entry_style,borderwidth=5, relief="flat")
        self.department_entry.pack(side="top", padx=self.spacing, pady=self.spacing)

        # Work hour label and entry
        self.work_hour_label = tk.Label(self.root, text="Work Hours:", **self.label_style)
        self.work_hour_label.pack(side="top", padx=self.spacing, pady=self.spacing)

        self.work_hour_entry = tk.Entry(self.root, **self.entry_style,borderwidth=5, relief="flat")
        self.work_hour_entry.pack(side="top", padx=self.spacing, pady=(self.spacing+10))

        # Add Employee button
        self.add_employee_button = tk.Button(self.root,width=20, text="    Add Employee    ",activebackground="#126D55", command=self.add_employee, **self.button_style,borderwidth=5, relief="flat")
        self.add_employee_button.pack(side="top", padx=self.spacing, pady=self.spacing)

        # Generate Report button
        self.generate_report_button = tk.Button(self.root,width=20, text="    Generate Report    ",activebackground="#126D55", command=self.generate_report, **self.button_style,borderwidth=5, relief="flat")
        self.generate_report_button.pack(side="top", padx=self.spacing, pady=self.spacing)

        # top_performers button
        self.top_performers_button = tk.Button(self.root,width=20, text="    Top-Performers    ",activebackground="#126D55", command=self.top_performers, **self.button_style,borderwidth=5, relief="flat")
        self.top_performers_button.pack(side="top", padx=self.spacing, pady=self.spacing)

        # Quit button
        self.quit_button = tk.Button(self.root,width=20, text="            Quit            ",activebackground="#126D55", command=self.root.quit, **self.button_style,borderwidth=5, relief="flat")
        self.quit_button.pack(side="top", padx=self.spacing, pady=self.spacing)

        

    def add_employee(self):
        id = int(self.employee_id_entry.get())
        name = self.employee_name_entry.get()
        department = self.department_entry.get()
        work_hour = float(self.work_hour_entry.get())
        efficiency = round(float(work_hour*100/float(self.m_work_hours)),3)
        employee = Employee(id, name, department, work_hour,efficiency)
        self.employee_data.append([employee.id, employee.name, employee.department, employee.work_hour,employee.efficiency])
        self.employee_id_entry.delete(0, tk.END)
        self.employee_name_entry.delete(0, tk.END)
        self.department_entry.delete(0, tk.END)
        self.work_hour_entry.delete(0, tk.END)

    def generate_report(self):
        df = pd.DataFrame(self.employee_data, columns=['ID', 'Name', 'Department', 'Work Hours', 'Efficiency'])
        report_window = tk.Toplevel(self.root)
        report_window.title("Efficiency Report "+self.month+" "+self.year)
        report_text = tk.Text(report_window)
        report_text.insert(tk.END, df.to_string(index=False))
        report_text.pack()

    def top_performers(self):
        df = pd.DataFrame(self.employee_data, columns=['ID', 'Name', 'Department', 'Work Hours','Efficiency'])
        mean_work_hour = df['Work Hours'].mean()
        top_performers = df[df['Work Hours'] >= mean_work_hour].sort_values(by='Work Hours', ascending=False)
        top_performers_window = tk.Toplevel(self.root)
        top_performers_window.title("Top Performers "+self.month+" "+self.year)
        top_performers_text = tk.Text(top_performers_window)
        top_performers_text.insert(tk.END, top_performers.to_string(index=False))
        top_performers_text.pack()
    
    def run(self):
        self.root.mainloop()
    def quit(self):
        self.root.destroy()
        
def main():
    
    root = tk.Tk()
    login_window = LoginWindow(root)
    login_window.run()
    
if __name__ == "__main__":
    main()
