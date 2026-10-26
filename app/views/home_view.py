import customtkinter as ctk
from app.views.head_manual_view import HeadManualView
from app.views.head_lookat_view import HeadLookAtView

class HomeView(ctk.CTkFrame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        self.controller = controller

        # Side Menu
        self.side_menu = ctk.CTkFrame(self, width=200)
        self.side_menu.pack(side='left', fill='y', padx=10, pady=10)

        self.side_menu_font = ctk.CTkFont(family="Arial", size=16, weight="bold")

        # Side Menu Label
        self.side_menu_label = ctk.CTkLabel(self.side_menu, text="Big Boom InMoov", font=self.side_menu_font)
        self.side_menu_label.pack(padx=10, pady=10)

        # Side Menu Buttons
        self.btn_home = ctk.CTkButton(self.side_menu, text="Home", command=self.show_home)
        self.btn_home.pack(padx=10, pady=10)

        self.btn_head_manual = ctk.CTkButton(self.side_menu, text="Head Manual", command=self.show_head_manual)
        self.btn_head_manual.pack(padx=10, pady=10)

        self.btn_head_lookat = ctk.CTkButton(self.side_menu, text="Head Look At", command=self.show_head_lookat)
        self.btn_head_lookat.pack(padx=10, pady=10)

        # Content Frame
        self.content_frame = ctk.CTkFrame(self)
        self.content_frame.pack(side='left', fill='both', expand=True, padx=10, pady=10)

        self.show_home()

    def clear_content(self):
        for widget in self.content_frame.winfo_children():
            widget.destroy()

    def show_home(self):
        self.clear_content()
        test_label = ctk.CTkLabel(self.content_frame, text="Test")
        test_label.pack(pady=20)

    def show_head_manual(self):
        self.clear_content()
        self.head_manual_view = HeadManualView(self.content_frame, self.controller)
        self.head_manual_view.pack(fill="both", expand=True)

    def show_head_lookat(self):
        self.clear_content()
        self.head_lookat_view = HeadLookAtView(self.content_frame, self.controller)
        self.head_lookat_view.pack(fill="both", expand=True)