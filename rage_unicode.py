import tkinter as tk
from tkinter import messagebox
import re
import ctypes
import webbrowser  # Import to open URLs in a browser

# Attempt to enable dark title bar on Windows 10/11
def enable_dark_titlebar(window):
    try:
        hwnd = ctypes.windll.user32.GetParent(window.winfo_id())
        DWMWA_USE_IMMERSIVE_DARK_MODE = 20
        value = ctypes.c_int(1)
        ctypes.windll.dwmapi.DwmSetWindowAttribute(
            hwnd,
            DWMWA_USE_IMMERSIVE_DARK_MODE,
            ctypes.byref(value),
            ctypes.sizeof(value)
        )
    except Exception as e:
        print("Dark titlebar not supported:", e)

# Remove non-printable Unicode characters and CR, LF
def remove_non_printable(text):
    # Verwijder CR (\r) en LF (\n) tekens, evenals andere niet-afdrukbare Unicode tekens
    cleaned_text = re.sub(r'[\u200B-\u200F\u202A-\u202E\u2060-\u206F\r\n]', '', text)
    return cleaned_text

# Show detected hidden Unicode characters
def show_hidden(text):
    hidden_chars = []
    for index, char in enumerate(text):
        if re.match(r'[\u200B-\u200F\u202A-\u202E\u2060-\u206F]', char):
            hidden_chars.append(f"✔ Position {index}: U+{ord(char):04X} ({char.encode('unicode_escape').decode()})")
    return hidden_chars

# Function to open GitHub profile in browser
def open_github():
    webbrowser.open("https://github.com/Sirage7474")

# Process text input
def process_text():
    input_text = input_textbox.get("1.0", "end-1c")
    cleaned_text = remove_non_printable(input_text)
    hidden_chars = show_hidden(input_text)

    clean_textbox.delete("1.0", "end")
    clean_textbox.insert("1.0", cleaned_text)

    output_textbox.delete("1.0", "end")
    if hidden_chars:
        output_textbox.insert("1.0", "🕵️ Hidden Unicode Characters Found:\n\n" + "\n".join(hidden_chars))
    else:
        output_textbox.insert("1.0", "✅ No hidden Unicode characters found.")

# GUI setup
root = tk.Tk()
root.title("Unicode Cleaner & Revealer")
root.geometry("750x620")
root.configure(bg="#1e1e1e")
root.after(10, lambda: enable_dark_titlebar(root))

# Unicode Cleaner by Sirage7474
title_label = tk.Label(root, text="Unicode Cleaner by Sirage7474", font=("Segoe UI", 14, "bold"), fg="white", bg="#1e1e1e")
title_label.pack(pady=(10, 0))

# GitHub label at the top-right (clickable)
github_label = tk.Label(root, text="GitHub", font=("Segoe UI", 14), fg="white", bg="#555555", cursor="hand2")
github_label.place(x=670, y=10)
github_label.bind("<Button-1>", lambda e: open_github())  # Bind left-click to open GitHub

# Styles
label_style = {"bg": "#1e1e1e", "fg": "white", "font": ("Segoe UI", 10)}
text_style = {
    "bg": "#2e2e2e",
    "fg": "white",
    "insertbackground": "white",
    "font": ("Consolas", 10),
    "borderwidth": 1,
    "relief": "solid"
}

# Input
tk.Label(root, text="Enter text (may include hidden Unicode characters):", **label_style).pack(pady=(10, 0))
input_textbox = tk.Text(root, height=6, width=85, **text_style)
input_textbox.pack(pady=5)

# Process Button
process_button = tk.Button(
    root,
    text="🧹 Clean Text",
    command=process_text,
    bg="#3a3a3a",
    fg="white",
    activebackground="#555555",
    font=("Segoe UI", 10, "bold")
)
process_button.pack(pady=10)

# Cleaned Output
tk.Label(root, text="Cleaned Text (all hidden characters removed):", **label_style).pack(pady=(10, 0))
clean_textbox = tk.Text(root, height=6, width=85, **text_style)
clean_textbox.pack(pady=5)

# Hidden Character Output
tk.Label(root, text="Hidden Unicode Character Checks:", **label_style).pack(pady=(10, 0))
output_textbox = tk.Text(root, height=10, width=85, **text_style)
output_textbox.pack(pady=5)

root.mainloop()
