import customtkinter as ctk
import pyfirmata2

from app.views.home_view import HomeView

class AppController:
    def __init__(self):
        self.app = ctk.CTk()
        # self.app.attributes('-fullscreen', True)
        self.app.geometry("1280x720")
        self.app.title('Big Boom InMoov')
        self.app.bind('<Escape>', lambda event: self.app.destroy())

        self.board = pyfirmata2.Arduino('COM3')

        # Head Motors
        self.horizontal_mtr = self.board.get_pin('d:11:s')
        self.vertical_mtr = self.board.get_pin('d:12:s')
        self.mouth_mtr = self.board.get_pin('d:13:s')

        self.show_home()

    def show_home(self):
        self.home_view = HomeView(self.app, self)
        self.home_view.pack(fill="both", expand=True)

    def run(self):
        self.app.mainloop()