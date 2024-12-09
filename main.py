from pynput.mouse import Button, Controller
from pynput import keyboard
import time
import threading
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox

mouse = Controller()

running = True

def StartClicker():
    time.sleep(1)

    global running
    try:
        delay = float(delay_input.get())
    except ValueError:
        root.attributes('-topmost', True)
        messagebox.showerror("Invalid Input", "Please enter a valid number for the delay.", parent=root)
        root.attributes('-topmost', False)
        return

    selected_button = dropdown_var.get()
    if selected_button == "Left Mouse Button":
        button = Button.left
    elif selected_button == "Right Mouse Button":
        button = Button.right
    else:
        root.attributes('-topmost', True)
        messagebox.showerror("Invalid Selection", "Please select a valid mouse button.", parent=root)
        root.attributes('-topmost', False)
        return

    def AutoClicker():
        global running
        
        while running:
            mouse.click(button, 1)
            time.sleep(delay)

    def ExitKey(key):
        global running

        try:
            if key.char == 'x':
                running = False
                return False
        except AttributeError:
            pass

    clickThread = threading.Thread(target=AutoClicker)
    clickThread.start()

    with keyboard.Listener(on_press=ExitKey) as listener:
        listener.join()

    clickThread.join()
    root.attributes('-topmost', True)
    messagebox.showinfo("Info", "Clicker stopped. Press OK to exit.", parent=root)
    root.attributes('-topmost', False)
    root.quit()

root = tk.Tk()
root.title("Milch Autoclicker")

frame_0 = tk.Frame(root)
frame_0.pack(pady=0, side="top",padx=0)

tk.Label(frame_0, text="Click Delay in Seconds:  ").pack(side="left", pady=0, padx=5)
tk.Label(frame_0, text="  Choose Mouse Button:").pack(side="left", pady=0, padx=5)

input_frame = tk.Frame(root)
input_frame.pack(pady=5)

delay_input = tk.Entry(input_frame)
delay_input.pack(side="left", pady=5, padx=5)

dropdown_var = tk.StringVar()
dropdown = ttk.Combobox(input_frame, textvariable=dropdown_var)
dropdown['values'] = ("Left Mouse Button", "Right Mouse Button")
dropdown.current(0)
dropdown.pack(side="left", pady=5, padx=5)

start_button = tk.Button(root, text="Start", command=StartClicker)
start_button.pack(pady=20)

root.mainloop()