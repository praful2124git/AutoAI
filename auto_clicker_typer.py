import pyautogui
import tkinter as tk
import threading
import time
import subprocess
from tkinter import ttk

def open_notepad():
    subprocess.run("notepad")

def auto_type():
    global running
    while running:
        pyautogui.press("q")
        time.sleep(float(type_interval.get()))

def auto_click():
    global running
    for _ in range(int(click_count.get())):
        if not running:
            break
        pyautogui.click()
        time.sleep(float(click_interval.get()))

def start_action():
    global running, thread
    running = True
    if mode.get() == "Typing":
        thread = threading.Thread(target=auto_type)
    else:
        thread = threading.Thread(target=auto_click)
    thread.start()

def stop_action():
    global running
    running = False

# GUI Setup
root = tk.Tk()
root.title("Auto Clicker & Typer")
root.geometry("500x400")
root.resizable(True, True)

ttk.Label(root, text="Select Mode:").pack()
mode = tk.StringVar(value="Typing")
ttk.Radiobutton(root, text="Typing", variable=mode, value="Typing").pack()
ttk.Radiobutton(root, text="Clicking", variable=mode, value="Clicking").pack()

ttk.Label(root, text="Typing Interval (seconds):").pack()
type_interval = ttk.Entry(root)
type_interval.pack()
type_interval.insert(0, "1")

ttk.Label(root, text="Click Interval (seconds):").pack()
click_interval = ttk.Entry(root)
click_interval.pack()
click_interval.insert(0, "1")

ttk.Label(root, text="Number of Clicks:").pack()
click_count = ttk.Entry(root)
click_count.pack()
click_count.insert(0, "10")

btn_open = ttk.Button(root, text="Open Notepad", command=open_notepad)
btn_open.pack()
btn_start = ttk.Button(root, text="Start", command=start_action)
btn_start.pack()
btn_stop = ttk.Button(root, text="Stop", command=stop_action)
btn_stop.pack()

# Enable window maximization
root.state('zoomed')

root.mainloop()
