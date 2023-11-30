import tkinter as tk
from tkinter import *
import customtkinter
import time
from tkinter import scrolledtext, simpledialog, messagebox
import threading  # Import threading module for voice input

def show_next_screen():
    # Destroy or hide the current screen
    root_tk.withdraw()  # Use withdraw to hide the current window

    # Create the next screen
    next_screen = Toplevel(root_tk)
    next_screen.geometry("500x400")
    next_screen.title("Kronos-Your Personal Assistant")

    # Add widgets to the next screen
    label = Label(next_screen, text="Welcome to KRONOS", bg="black", fg="white", font=("Helvetica", 16, "bold"))  # Dark mode label
    label.pack()

    # Create a scrolled text widget for the chat display
    chat_display = scrolledtext.ScrolledText(next_screen, wrap=tk.WORD, state=tk.DISABLED, width=40, height=10, font=("Helvetica", 12))
    chat_display.pack(expand=True, fill=tk.BOTH)

    # Create an entry widget for typing messages
    entry = tk.Text(next_screen, height=3, wrap=tk.WORD, font=("Helvetica", 12))
    entry.pack(expand=True, fill=tk.BOTH)

    # Create a button to send messages
    send_button = tk.Button(next_screen, text="Send", command=lambda: send_message(entry, chat_display), bg="#4CAF50", fg="white", font=("Helvetica", 12, "bold"))  # Green button
    send_button.pack(pady=10)

    # Create a button for voice input
    audio_button = tk.Button(next_screen, text="Audio", command=start_voice_input, bg="#1E90FF", fg="white", font=("Helvetica", 12, "bold"))  # Blue button
    audio_button.pack(pady=5)

    # Display an initial message in the chat console
    initial_message = "Hello! I'm Kronos, your personal assistant. How can I assist you today?"
    display_message("Kronus", initial_message, chat_display)

def go_back(screen):
    # Destroy or withdraw the current screen and show the main screen
    screen.destroy()
    root_tk.deiconify()  # Use deiconify to show the main window again

def send_message(entry, chat_display):
    message = entry.get("2.0", tk.END).strip()  # Get the message from the entry widget
    if message:
        # Display the sent message in the chat interface
        display_message("You", message, chat_display)

        # Send the message to the backend (replace this with your actual backend communication)
        send_message_to_backend(message)

        # Clear the entry widget for the next message
        entry.delete("1.0", tk.END)

def send_message_to_backend(message):
    # Placeholder function for backend communication
    # You should replace this function with your actual backend communication logic
    print(f"Message sent to backend: {message}")

def display_message(sender, message, chat_display):
    # Display a formatted message in the chat interface
    formatted_message = f"{sender}: {message}\n"
    chat_display.configure(state=tk.NORMAL)
    chat_display.insert(tk.END, formatted_message, "tag-right" if sender == "You" else "tag-left")
    chat_display.yview(tk.END)  # Scroll to the bottom of the chat display
    chat_display.configure(state=tk.DISABLED)

def start_voice_input():
    # This function should be replaced with your voice recognition logic
    # You can use a library like SpeechRecognition for voice input
    # For simplicity, we'll just print a message indicating that voice input is not implemented
    print("Voice input is not implemented yet. Integrate your voice recognition logic here.")

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
button = customtkinter.CTkButton(master=root_tk, corner_radius=10, command=show_next_screen, text="Let's get started", font=("Helvetica", 14, "bold"))  # Dark mode button
button.place(relx=0.5, rely=0.75, anchor=customtkinter.CENTER)

# Create and animate the "Welcome to KRONUS" text in three lines
welcome_text = " \nKRONOS"
text_id = background_canvas.create_text(300, 100, text=welcome_text, font=("Helvetica", 20), fill="white")
#animate_welcome_text(background_canvas, text_id)

# Define the chat message styles
#root_tk.option_add('*tag-right', foreground='white', justify='right')
#root_tk.option_add('*tag-left', foreground='white', justify='left')

# Main loop
root_tk.mainloop()
