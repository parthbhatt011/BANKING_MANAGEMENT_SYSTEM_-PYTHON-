import tkinter as tk
from tkinter import messagebox
from tkinter import ttk

# your existing imports (unchanged)
from services.auth_service import login_user, register_user
from ui.dashboard import dashboard
from database.queries import show_account


class BankingApp:

    def __init__(self, root):
        self.root = root
        self.root.title("Banking Management System")
        self.root.geometry("500x400")
        self.root.resizable(False, False)

        self.main_frame = tk.Frame(root)
        self.main_frame.pack(fill="both", expand=True)

        self.show_main_menu()

    # ---------------- MAIN MENU ----------------
    def show_main_menu(self):
        self.clear_frame()

        tk.Label(
            self.main_frame,
            text="BANKING MANAGEMENT SYSTEM",
            font=("Arial", 16, "bold"),
            fg="blue"
        ).pack(pady=20)

        tk.Button(
            self.main_frame,
            text="Login",
            width=20,
            command=self.show_login
        ).pack(pady=10)

        tk.Button(
            self.main_frame,
            text="Register",
            width=20,
            command=self.show_register
        ).pack(pady=10)

        tk.Button(
            self.main_frame,
            text="Exit",
            width=20,
            command=self.root.quit
        ).pack(pady=10)

    # ---------------- LOGIN ----------------
    def show_login(self):
        self.clear_frame()

        tk.Label(self.main_frame, text="Login", font=("Arial", 14, "bold")).pack(pady=10)

        tk.Label(self.main_frame, text="Email").pack()
        self.login_email = tk.Entry(self.main_frame, width=30)
        self.login_email.pack()

        tk.Label(self.main_frame, text="Password").pack()
        self.login_password = tk.Entry(self.main_frame, show="*", width=30)
        self.login_password.pack()

        tk.Button(
            self.main_frame,
            text="Login",
            command=self.login_action
        ).pack(pady=10)

        tk.Button(
            self.main_frame,
            text="Back",
            command=self.show_main_menu
        ).pack()

    def login_action(self):
        email = self.login_email.get()
        password = self.login_password.get()

        try:
            user = login_user(email, password)
            messagebox.showinfo("Success", "Login successful")
            dashboard(user)

        except Exception as e:
            messagebox.showerror("Error", str(e))

    # ---------------- REGISTER ----------------
    def show_register(self):
        self.clear_frame()

        tk.Label(self.main_frame, text="Register", font=("Arial", 14, "bold")).pack(pady=10)

        tk.Label(self.main_frame, text="Name").pack()
        self.reg_name = tk.Entry(self.main_frame, width=30)
        self.reg_name.pack()

        tk.Label(self.main_frame, text="Email").pack()
        self.reg_email = tk.Entry(self.main_frame, width=30)
        self.reg_email.pack()

        tk.Label(self.main_frame, text="Password").pack()
        self.reg_password = tk.Entry(self.main_frame, show="*", width=30)
        self.reg_password.pack()

        tk.Button(
            self.main_frame,
            text="Register",
            command=self.register_action
        ).pack(pady=10)

        tk.Button(
            self.main_frame,
            text="Back",
            command=self.show_main_menu
        ).pack()

    def register_action(self):
        name = self.reg_name.get()
        email = self.reg_email.get()
        password = self.reg_password.get()

        try:
            register_user(name, email, password)
            account = show_account(email)

            messagebox.showinfo(
                "Success",
                f"User registered successfully\n\nAccount Details:\n{account}"
            )

        except Exception as e:
            messagebox.showerror("Error", str(e))

    # ---------------- UTIL ----------------
    def clear_frame(self):
        for widget in self.main_frame.winfo_children():
            widget.destroy()


# ---------------- RUN APP ----------------
if __name__ == "__main__":
    root = tk.Tk()
    app = BankingApp(root)
    root.mainloop()