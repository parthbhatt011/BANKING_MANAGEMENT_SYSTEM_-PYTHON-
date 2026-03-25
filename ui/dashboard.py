import tkinter as tk
from tkinter import messagebox


# from ui.transaction_window import deposit_ui, withdraw_ui, showbalance_ui

class Dashboard:
    def __init__(self, root, user):
        self.root = root
        self.user = user
        self.root.title(f"Bank | {user['name']}")
        self.root.geometry("900x600")
        self.root.configure(bg="#0f172a")

        # Theme Colors
        self.bg_dark = "#0f172a"
        self.sidebar_color = "#1e293b"
        self.accent_blue = "#3b82f6"
        self.text_white = "#f8fafc"
        self.text_dim = "#94a3b8"

        self.setup_layout()

    def setup_layout(self):
        # --- SIDEBAR ---
        self.sidebar = tk.Frame(self.root, bg=self.sidebar_color, width=220)
        self.sidebar.pack(side="left", fill="y")
        self.sidebar.pack_propagate(False)

        # Brand Label
        tk.Label(
            self.sidebar, text="BANK", font=("Segoe UI", 22, "bold"),
            bg=self.sidebar_color, fg=self.accent_blue
        ).pack(pady=(40, 40))

        # Nav Buttons
        self.create_nav_item("Dashboard", self.show_home)
        self.create_nav_item("Deposit", self.handle_deposit)
        self.create_nav_item("Withdraw", self.handle_withdraw)
        self.create_nav_item("Balance", self.handle_balance)

        # Logout at bottom
        logout_btn = tk.Button(
            self.sidebar, text="Logout", font=("Segoe UI", 10, "bold"),
            bg="#ef4444", fg="white", bd=0, relief="flat",
            command=self.root.destroy, cursor="hand2"
        )
        logout_btn.pack(side="bottom", fill="x", padx=20, pady=30, ipady=8)

        # --- MAIN CONTENT ---
        self.content_area = tk.Frame(self.root, bg=self.bg_dark, padx=50, pady=50)
        self.content_area.pack(side="right", expand=True, fill="both")

        self.show_home()

    def create_nav_item(self, text, command):
        btn = tk.Button(
            self.sidebar, text=text, font=("Segoe UI", 11),
            bg=self.sidebar_color, fg=self.text_dim, bd=0, relief="flat",
            anchor="w", padx=30, pady=15, activebackground="#334155",
            activeforeground="white", cursor="hand2", command=command
        )
        btn.pack(fill="x")
        btn.bind("<Enter>", lambda e: btn.config(fg="white", bg="#334155"))
        btn.bind("<Leave>", lambda e: btn.config(fg=self.text_dim, bg=self.sidebar_color))

    def clear_content(self):
        for widget in self.content_area.winfo_children():
            widget.destroy()

    # ---------- NAVIGATION HANDLERS ----------

    def show_home(self):
        self.clear_content()

        # Welcome Message
        tk.Label(
            self.content_area, text=f"Welcome, {self.user['name']}",
            font=("Segoe UI", 24, "bold"), bg=self.bg_dark, fg="white"
        ).pack(anchor="w")

        tk.Label(
            self.content_area, text="What would you like to do today?",
            font=("Segoe UI", 12), bg=self.bg_dark, fg=self.text_dim
        ).pack(anchor="w", pady=(5, 30))

        # Quick Actions Card
        card = tk.Frame(self.content_area, bg=self.sidebar_color, padx=30, pady=30, highlightthickness=1,
                        highlightbackground="#334155")
        card.pack(fill="x")

        tk.Label(card, text="ACCOUNT STATUS", font=("Segoe UI", 9, "bold"), bg=self.sidebar_color,
                 fg=self.accent_blue).pack(anchor="w")
        tk.Label(card, text="ACTIVE", font=("Segoe UI", 18, "bold"), bg=self.sidebar_color, fg="#22c55e").pack(
            anchor="w", pady=(5, 0))

    def handle_deposit(self):
        # Trigger your existing deposit logic
        # deposit_ui()
        messagebox.showinfo("Deposit", "Opening Deposit Interface...")

    def handle_withdraw(self):
        # Trigger your existing withdraw logic
        # withdraw_ui()
        messagebox.showinfo("Withdraw", "Opening Withdrawal Interface...")

    def handle_balance(self):
        # Trigger your existing balance logic
        # showbalance_ui()
        messagebox.showinfo("Balance", "Fetching current balance...")


# Function to launch from login
def dashboard(user):
    dash_window = tk.Toplevel()
    Dashboard(dash_window, user)