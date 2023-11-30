import tkinter as tk
from tkinter import *
import customtkinter
import time



def show_next_screen():
    # Destroy or hide the current screen
    root_tk.withdraw()  # Use withdraw to hide the current window

    # Create the next screen
    next_screen = Toplevel(root_tk)
    next_screen.geometry("500x400")
    next_screen.title("Kronus-Your Personel Assistant")

    # Add widgets to the next screen
    label = Label(next_screen, text="Welcome to KRONUS", bg="black", fg="white")  # Dark mode label
    label.pack()

    # Example: Add a button to go back to the main screen
    back_button = Button(next_screen, text="Go Back", command=lambda: go_back(next_screen), bg="black", fg="white")  # Dark mode button
    back_button.pack()

def go_back(screen):
    # Destroy or withdraw the current screen and show the main screen
    screen.destroy()
    root_tk.deiconify()  # Use deiconify to show the main window again

def animate_welcome_text(canvas, text_id):
    for i in range(10):
        canvas.itemconfig(text_id, font=("Helvetica", 20 + i*2))
        root_tk.update_idletasks()
        time.sleep(0.1)

root_tk = tk.Tk()
root_tk.geometry("600x400")
root_tk.title("KRONUS")
root_tk.configure(bg="black")  # Dark mode background color

# Specify the path to your icon file
icon_path = r"C:\Users\Arun\OneDrive\Pictures\Desktop\zara\ZARA\kronusimage.ico"

try:
    root_tk.iconbitmap(icon_path)
except tk.TclError as e:
    print(f"Error setting icon: {e}")

# Create a Canvas widget for the background
background_canvas = Canvas(root_tk, width=600, height=440, bg="black")
background_canvas.pack()

# Use CTkButton instead of tkinter Button
button = customtkinter.CTkButton(master=root_tk, corner_radius=10, command=show_next_screen, text="Let's get started")  # Dark mode button
button.place(relx=0.5, rely=0.75, anchor=customtkinter.CENTER)


# Create and animate the "Welcome to KRONUS" text in three lines
welcome_text = " \nKRONUS"
text_id = background_canvas.create_text(300, 100, text=welcome_text, font=("Helvetica", 20), fill="white")
animate_welcome_text(background_canvas, text_id)

root_tk.mainloop()
