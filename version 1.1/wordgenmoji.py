import tkinter as tk
from tkinter import filedialog, messagebox
from itertools import permutations
import tkinter.font as tkFont

# 
def generate_combinations(words):
    combos = set()
    for r in range(1, len(words) + 1):
        for perm in permutations(words, r):
            joined = ''.join(perm)
            combos.update([
                joined, joined.lower(), joined.upper(), joined.capitalize(),
                joined + "123", "123" + joined,
                "@" + joined, joined + "@",
                "!" + joined, joined + "!",
                "#" + joined, joined + "#" ,
                joined + "0", "0" + joined , "1" + joined , joined + "1" ,
                "2" + joined , joined + "2" ,
                "X" + joined , joined + "X" ,
                "00" + joined , joined + "00" ,
                "#@" + joined , joined + "#@" ,
                "@#" + joined , joined + "@#" ,
                "*" + joined , joined + "*" ,
                "0" + joined + "0" ,
                "00" + joined + "0" , "123" + joined + "321" ,
                "@" + joined + "@" ,
                "#" + joined + "#" ,
                "#" + joined + "@" ,
                "@" + joined + "#" ,
                "#" + joined + "!" , "@!" + joined + "#" , "@" + joined + "!"
            ])
    return sorted(combos)

# Save to file
def save_to_file(data):
    file_path = filedialog.asksaveasfilename(
        defaultextension=".txt",
        filetypes=[("Text files", "*.txt")]
    )
    if file_path:
        with open(file_path, 'w', encoding='utf-8') as f:
            for item in data:
                f.write(item + '\n')
        messagebox.showinfo("Success", f"Wordlist saved to:\n{file_path}")
        status.config(text=f"✅ Saved to: {file_path}")

# Generate and save
def generate():
    inputs = [entry.get() for entry in entries if entry.get().strip()]
    if not inputs:
        messagebox.showwarning("Input Error", "Please enter at least one word.")
        return
    result = generate_combinations(inputs)
    save_to_file(result)


# GUI Setup
root = tk.Tk()
root.title("🧠 Wordgen by Moji")
root.geometry("600x500")
root.configure(bg="#000000")  # Dark background

try:
    root.iconbitmap("logo.ico")  # Add your icon if available
except:
    pass

font_title = tkFont.Font(family="Helvetica", size=20, weight="bold")
font_label = tkFont.Font(family="Arial", size=15)
font_entry = tkFont.Font(family="Courier", size=15)

tk.Label(root, text="🔥 WordgenMoji", font=font_title, fg="#ff0033", bg="#1e1e1e").pack(pady=13)

frame = tk.Frame(root, bg="#000000")
frame.pack(pady=10)

entries = []
labels = ["Word", "Word", "Number"]

for i, label in enumerate(labels):
    tk.Label(frame, text=label, fg="white", bg="#000000", font=font_label).grid(row=i, column=0, sticky="w", pady=5, padx=10)
    e = tk.Entry(frame, width=30, font=font_entry, bg="#1e1e1e", fg="white", insertbackground="white")
    e.grid(row=i, column=1, padx=10)
    entries.append(e)

tk.Button(
    root,
    text="🚀 Generate Wordlist",
    command=generate,
    bg="#e60000",
    fg="black",
    font=font_label,
    relief=tk.GROOVE,
    activebackground="#009a00"
).pack(pady=25)

status = tk.Label(root, text="🔄 Ready", bd=1, relief=tk.SUNKEN, anchor=tk.W, bg="#2d2d2d", fg="white")
status.pack(fill=tk.X, side=tk.BOTTOM, ipady=2)

root.mainloop()
