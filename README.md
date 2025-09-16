# Auto Clicker & Typer (Educational Demo)

A simple Python GUI tool built with **Tkinter** and **PyAutoGUI** that can either:
- Press the `q` key at a chosen interval (**Typing mode**), or
- Perform a defined number of mouse clicks at a chosen interval (**Clicking mode**).

Includes a **PyInstaller** spec for bundling into a standalone app and a helper to open Notepad (Windows-only).

> ⚠️ **Educational Purposes Only**  
> This project is provided solely to demonstrate GUI programming, threading, and automation basics with Python.  
> **Do not misuse** this code for spamming, cheating, bypassing restrictions, or violating terms of service.  
> You are solely responsible for how you use it.

---

## ✨ Features
- Clean **Tkinter** interface (resizable, starts maximized).  
- Two modes: **Typing** (`q` key) or **Clicking** (mouse).  
- Adjustable **intervals** and **click count**.  
- Button to **open Notepad** (Windows).  
- **PyInstaller** spec included for packaging.

---

## 🔧 Requirements
- Python 3.8+ (tested on 3.10+)
- [pyautogui](https://pypi.org/project/PyAutoGUI/)
- [pillow](https://pypi.org/project/Pillow/) (PyAutoGUI dependency)
- Tkinter (comes with standard Python)

Install with:
```bash
pip install pyautogui pillow
