import tkinter as tk
from tkinter import filedialog, messagebox
import pyautogui
from PIL import ImageGrab
import time
import os
import logging
from datetime import datetime

# ==========================
# Logging Setup
# ==========================

logging.basicConfig(
    filename="screenshot_log.txt",
    level=logging.INFO,
    format="%(asctime)s - %(message)s"
)

SAVE_FOLDER = "screenshots"

if not os.path.exists(SAVE_FOLDER):
    os.makedirs(SAVE_FOLDER)

# ==========================
# Screenshot Logic
# ==========================

def generate_filename():
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    return f"screenshot_{timestamp}.png"


def take_full_screenshot(delay):
    time.sleep(delay)
    filename = generate_filename()
    path = os.path.join(SAVE_FOLDER, filename)
    screenshot = pyautogui.screenshot()
    screenshot.save(path)
    logging.info(f"Full Screenshot Saved: {path}")
    messagebox.showinfo("Success", f"Screenshot saved:\n{path}")


def select_region():
    root.withdraw()
    time.sleep(1)
    messagebox.showinfo("Instructions", "Drag to select region.")

    screenshot = ImageGrab.grab()
    screenshot.show()

    root.deiconify()


def take_region_screenshot(delay):
    root.withdraw()
    time.sleep(delay)
    try:
        # Take full screenshot first
        full_screenshot = ImageGrab.grab()
        # For now, save the full screenshot as region screenshot
        # A proper region selector would require additional GUI implementation
        filename = generate_filename()
        path = os.path.join(SAVE_FOLDER, filename)
        full_screenshot.save(path)
        logging.info(f"Region Screenshot Saved: {path}")
        root.deiconify()
        messagebox.showinfo("Success", f"Screenshot saved:\n{path}")
    except Exception as e:
        root.deiconify()
        messagebox.showerror("Error", f"Failed to capture region: {str(e)}")
        logging.error(f"Region Capture Failed: {str(e)}")


# ==========================
# GUI Setup
# ==========================

root = tk.Tk()
root.title("Screenshot Tool PRO")
root.geometry("400x300")
root.configure(bg="#1e293b")

title = tk.Label(root, text="📸 Screenshot Tool PRO",
                 font=("Segoe UI", 16),
                 bg="#1e293b", fg="white")
title.pack(pady=15)

delay_label = tk.Label(root, text="Delay (seconds):",
                       bg="#1e293b", fg="white")
delay_label.pack()

delay_entry = tk.Entry(root)
delay_entry.insert(0, "0")
delay_entry.pack(pady=5)


def full_capture():
    delay = int(delay_entry.get())
    take_full_screenshot(delay)


def region_capture():
    delay = int(delay_entry.get())
    take_region_screenshot(delay)


btn_full = tk.Button(root, text="Full Screen Capture",
                     command=full_capture,
                     bg="#22c55e", fg="white")
btn_full.pack(pady=10)

btn_region = tk.Button(root, text="Region Capture",
                       command=region_capture,
                       bg="#3b82f6", fg="white")
btn_region.pack(pady=10)

btn_exit = tk.Button(root, text="Exit",
                     command=root.quit,
                     bg="#ef4444", fg="white")
btn_exit.pack(pady=20)

root.mainloop()