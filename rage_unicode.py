import tkinter as tk
from tkinter import messagebox
import re

# Functie om niet-afdrukbare Unicode-tekens te verwijderen
def remove_non_printable(text):
    # Verwijdert zero-width en andere niet-afdrukbare tekens
    cleaned_text = re.sub(r'[\u200B\u200C\u200D\u200E\u200F\u202A\u202B\u202C\u202D\u202E\u2060\u2061\u2062\u2063\u2064\u2065\u2066\u2067\u2068\u2069\u206A\u206B\u206C\u206D\u206E\u206F]', '', text)
    return cleaned_text

# Functie om verborgen Unicode-tekens te tonen
def show_hidden(text):
    hidden_chars = []
    for index, char in enumerate(text):
        if re.match(r'[\u200B\u200C\u200D\u200E\u200F\u202A\u202B\u202C\u202D\u202E\u2060\u2061\u2062\u2063\u2064\u2065\u2066\u2067\u2068\u2069\u206A\u206B\u206C\u206D\u206E\u206F]', char):
            hidden_chars.append(f"[pos {index}] U+{ord(char):04X} ({char})")
    return hidden_chars

# Functie om tekst van de GUI te verwerken
def process_text():
    input_text = input_textbox.get("1.0", "end-1c")
    cleaned_text = remove_non_printable(input_text)
    hidden_chars = show_hidden(input_text)

    # Toon de opgeschoonde tekst en verborgen Unicode-tekens
    output_textbox.delete("1.0", "end")
    output_textbox.insert("1.0", cleaned_text)

    if hidden_chars:
        hidden_output = "\nHidden Unicode Characters:\n" + "\n".join(hidden_chars)
        output_textbox.insert("end", hidden_output)
    else:
        output_textbox.insert("end", "\nNo hidden Unicode characters found.")

# GUI configuratie
root = tk.Tk()
root.title("Unicode Cleaner & Revealer")
root.geometry("600x400")

# Invoerveld voor tekst
input_label = tk.Label(root, text="Enter text (with possible hidden Unicode characters):")
input_label.pack(pady=10)

input_textbox = tk.Text(root, height=8, width=70)
input_textbox.pack(pady=5)

# Verwerkingsknop
process_button = tk.Button(root, text="Process Text", command=process_text)
process_button.pack(pady=10)

# Uitvoerveld voor opgeschoonde tekst
output_label = tk.Label(root, text="Processed Text (without hidden Unicode characters):")
output_label.pack(pady=10)

output_textbox = tk.Text(root, height=8, width=70)
output_textbox.pack(pady=5)

# Hoofdloop van de GUI
root.mainloop()
