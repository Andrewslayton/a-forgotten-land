import tkinter as tk
import os
os.environ["SDL_VIDEODRIVER"]="x11"

def get_player_name():
    name = entry.get()
    label.config(text=f"Welcome, {name}! Your name will be displayed on your card.")
    entry.delete(0, tk.END)  # Clear the entry field

# Create the main window
root = tk.Tk()
root.title("Eldritch Realms: Enter Your Name")

# Load the background image
bg_image = tk.PhotoImage(file="gui/photos/charCreation.jfif")  # Adjust the path as needed

# Create a label to hold the background image
bg_label = tk.Label(root, image=bg_image)
bg_label.place(relwidth=1, relheight=1)

# Create a label and an entry field
label = tk.Label(root, text="Enter your name:")
label.pack(pady=10)
entry = tk.Entry(root, width=30)
entry.pack(pady=10)

# Create a button to submit the name
button = tk.Button(root, text="Submit", command=get_player_name)
button.pack(pady=10)

# Run the main loop
root.mainloop()

