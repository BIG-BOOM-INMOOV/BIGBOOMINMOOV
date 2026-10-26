import customtkinter as ctk

class HeadManualView(ctk.CTkFrame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        self.controller = controller

        # Motors
        # self.horizontal_mtr = self.controller.horizontal_mtr
        # self.vertical_mtr = self.controller.vertical_mtr
        # self.mouth_mtr = self.controller.mouth_mtr

        # Angle Sliders

        # Horizontal Slider
        self.horizontal_label = ctk.CTkLabel(self, text="Horizontal Head Mech")
        self.horizontal_label.grid(row=0, column=0, padx=10, sticky="ew")

        self.horizontal_slider = ctk.CTkSlider(self, from_=0, to=180, command=lambda value: self.rot_mtr(value, "horizontal"))
        self.horizontal_slider.set(90)
        self.horizontal_slider.grid(row=1, column=0, padx=10, sticky="ew")

        self.horizontal_value = ctk.CTkLabel(self, text=f"{int(self.horizontal_slider.get()):03d}")
        self.horizontal_value.grid(row=1, column=1, padx=10, sticky="w")

        # Vertical Slider
        self.vertical_label = ctk.CTkLabel(self, text="Vertical Head Mech")
        self.vertical_label.grid(row=2, column=0, padx=10, sticky="ew")

        self.vertical_slider = ctk.CTkSlider(self, from_=0, to=180, command=lambda value: self.rot_mtr(value, "vertical"))
        self.vertical_slider.set(90)
        self.vertical_slider.grid(row=3, column=0, padx=10, sticky="ew")

        self.vertical_value = ctk.CTkLabel(self, text=f"{int(self.vertical_slider.get()):03d}")
        self.vertical_value.grid(row=3, column=1, padx=10, sticky="w")

        # Mouth Slider
        self.mouth_label = ctk.CTkLabel(self, text="Mouth Head Mech")
        self.mouth_label.grid(row=4, column=0, padx=10, sticky="ew")

        self.mouth_slider = ctk.CTkSlider(self, from_=0, to=180, command=lambda value: self.rot_mtr(value, "mouth"))
        self.mouth_slider.set(90)
        self.mouth_slider.grid(row=5, column=0, padx=10, sticky="ew")

        self.mouth_value = ctk.CTkLabel(self, text=f"{int(self.mouth_slider.get()):03d}")
        self.mouth_value.grid(row=5, column=1, padx=10, sticky="w")

        self.grid_columnconfigure(0, weight=1)
        self.grid_columnconfigure(1, weight=0)

    def rot_mtr(self, value, slider_name):
        match slider_name:
            case "horizontal":
                # self.horizontal_mtr.write(value)
                self.horizontal_value.configure(text=f"{int(value):03d}")
            case "vertical":
                # self.vertical_mtr.write(value)
                self.vertical_value.configure(text=f"{int(value):03d}")
            case "mouth":
                # self.mouth_mtr.write(value)
                self.mouth_value.configure(text=f"{int(value):03d}")
            case _:
                print("motor not connected to slider")