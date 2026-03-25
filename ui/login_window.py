import tkinter as tk
from tkinter import messagebox


# Note: Ensure your local imports (services/database) are in the same folder
# from services.auth_service import login_user, register_user
# from ui.dashboard import dashboard
# from database.queries import show_account

class BankingApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Bank | Secure Portal")
        self.root.geometry("800x600")
        self.root.configure(bg="#0f172a")  # Deep Navy Background

        # Colors
        self.bg_color = "#0f172a"
        self.card_bg = "#1e293b"
        self.primary_blue = "#3b82f6"
        self.hover_blue = "#2563eb"
        self.text_white = "#f8fafc"
        self.text_dim = "#94a3b8"
        self.danger_red = "#ef4444"

        # Main Container
        self.main_container = tk.Frame(self.root, bg=self.bg_color)
        self.main_container.place(relx=0.5, rely=0.5, anchor="center")

        self.show_main_menu()

    def clear_frame(self):
        for widget in self.main_container.winfo_children():
            widget.destroy()

    def create_card(self, width=350):
        card = tk.Frame(
            self.main_container,
            bg=self.card_bg,
            padx=40,
            pady=40,
            highlightbackground="#334155",
            highlightthickness=1
        )
        card.pack(expand=True)
        return card

    # ---------- COMPONENTS ----------

    def create_label(self, parent, text, size=10, bold=False, color=None):
        color = color if color else self.text_white
        font = ("Segoe UI", size, "bold" if bold else "normal")
        lbl = tk.Label(parent, text=text, font=font, bg=self.card_bg, fg=color)
        lbl.pack(anchor="w", pady=(10, 2))
        return lbl

    def create_entry(self, parent, placeholder, is_password=False):
        entry_frame = tk.Frame(parent, bg="#334155", padx=2, pady=2)
        entry_frame.pack(fill="x", pady=(0, 15))

        entry = tk.Entry(
            entry_frame,
            font=("Segoe UI", 11),
            bg="#1e293b",
            fg="white",
            insertbackground="white",
            relief="flat",
            borderwidth=0,
            show="*" if is_password else ""
        )
        entry.pack(fill="x", ipady=8, padx=5)
        return entry

    def create_button(self, parent, text, command, color=None, secondary=False):
        bg = color if color else self.primary_blue
        if secondary: bg = "#334155"

        btn = tk.Button(
            parent,
            text=text,
            command=command,
            bg=bg,
            fg="white",
            font=("Segoe UI", 11, "bold"),
            relief="flat",
            activebackground=self.hover_blue,
            activeforeground="white",
            cursor="hand2",
            bd=0,
            width=20
        )
        btn.pack(fill="x", ipady=8, pady=10)

        # Simple Hover Effect
        btn.bind("<Enter>", lambda e: btn.config(bg=self.hover_blue if not secondary else "#475569"))
        btn.bind("<Leave>", lambda e: btn.config(bg=bg))
        return btn

    # ---------- SCREENS ----------

    def show_main_menu(self):
        self.clear_frame()

        # Logo/Title area
        title_label = tk.Label(
            self.main_container,
            text="BANK",
            font=("Segoe UI", 28, "bold"),
            fg=self.primary_blue,
            bg=self.bg_color
        )
        title_label.pack(pady=(0, 30))

        card = self.create_card()

        tk.Label(
            card, text="Welcome Back",
            font=("Segoe UI", 18, "bold"),
            bg=self.card_bg, fg=self.text_white
        ).pack(pady=(0, 10))

        tk.Label(
            card, text="Select an option to continue",
            font=("Segoe UI", 10),
            bg=self.card_bg, fg=self.text_dim
        ).pack(pady=(0, 25))

        self.create_button(card, "Login to Account", self.show_login)
        self.create_button(card, "Open New Account", self.show_register, secondary=True)

        exit_btn = tk.Label(card, text="Exit System", fg=self.text_dim, bg=self.card_bg, cursor="hand2")
        exit_btn.pack(pady=(15, 0))
        exit_btn.bind("<Button-1>", lambda e: self.root.destroy())

    def show_login(self):
        self.clear_frame()
        card = self.create_card()

        tk.Label(card, text="Login", font=("Segoe UI", 20, "bold"), bg=self.card_bg, fg="white").pack(anchor="w")
        tk.Label(card, text="Enter your credentials", font=("Segoe UI", 9), bg=self.card_bg, fg=self.text_dim).pack(
            anchor="w", pady=(0, 20))

        self.create_label(card, "Email Address", size=9)
        self.login_email = self.create_entry(card, "email@example.com")

        self.create_label(card, "Password", size=9)
        self.login_password = self.create_entry(card, "••••••••", is_password=True)

        self.create_button(card, "Sign In", self.login_action)
        self.create_button(card, "Go Back", self.show_main_menu, secondary=True)

    def show_register(self):
        self.clear_frame()
        card = self.create_card()

        tk.Label(card, text="Register", font=("Segoe UI", 20, "bold"), bg=self.card_bg, fg="white").pack(anchor="w")
        tk.Label(card, text="Join our secure banking network", font=("Segoe UI", 9), bg=self.card_bg,
                 fg=self.text_dim).pack(anchor="w", pady=(0, 20))

        self.create_label(card, "Full Name", size=9)
        self.reg_name = self.create_entry(card, "John Doe")

        self.create_label(card, "Email Address", size=9)
        self.reg_email = self.create_entry(card, "email@example.com")

        self.create_label(card, "Create Password", size=9)
        self.reg_password = self.create_entry(card, "••••••••", is_password=True)

        self.create_button(card, "Create Account", self.register_action)
        self.create_button(card, "Go Back", self.show_main_menu, secondary=True)

    # ---------- ACTIONS (Placeholders) ----------
    def login_action(self):
        # Your original logic here
        email = self.login_email.get()
        if not email:
            messagebox.showwarning("Input Error", "Please enter your email")
            return
        messagebox.showinfo("Success", f"Attempting login for {email}")

    def register_action(self):
        # Your original logic here
        name = self.reg_name.get()
        if not name:
            messagebox.showwarning("Input Error", "Please enter your name")
            return
        messagebox.showinfo("Success", "Registration Logic Triggered")


if __name__ == "__main__":
    root = tk.Tk()
    # High DPI awareness for Windows (makes text sharp)
    try:
        from ctypes import windll

        windll.shcore.SetProcessDpiAwareness(1)
    except:
        pass

    app = BankingApp(root)
    root.mainloop()