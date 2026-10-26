import customtkinter as ctk

# Initialize the main window
app = ctk.CTk()
app.geometry("400x150")
app.title("Slider Value Example")

# Create a frame to keep the slider and label grouped together nicely
frame = ctk.CTkFrame(app, fg_color="transparent")
frame.pack(pady=40, padx=20, fill="x")

# 1. Callback function that triggers when the slider moves
def slider_event(value):
    # Convert float value to integer (or round it if needed) and update label
    value_label.configure(text=f"Value: {int(value)}")

# 2. Create the Slider
slider = ctk.CTkSlider(
    master=frame, 
    from_=0, 
    to=100, 
    command=slider_event
)
# Place slider in row 0, column 0 and let it expand horizontally
slider.grid(row=0, column=0, padx=(0, 10), sticky="ew")
slider.set(0) # Set initial value

# 3. Create the Label to display the value next to the slider
value_label = ctk.CTkLabel(master=frame, text="Value: 0")
# Place label in row 0, column 1
value_label.grid(row=0, column=1, sticky="w")

# Configure the frame's grid layout columns
frame.grid_columnconfigure(0, weight=1) # The slider column takes up remaining space
frame.grid_columnconfigure(1, weight=0) # The label column only takes up the space it needs

app.mainloop()
