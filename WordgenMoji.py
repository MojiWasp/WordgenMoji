import tkinter as tk
from tkinter import filedialog, messagebox
from itertools import permutations, product
 # has a GUI [tkinter]

def generate_combinations(words):
    combos = set()
    for r in range(1, len(words) + 1):
        for perm in permutations(words, r):
            joined = ''.join(perm)
            combos.add(joined)
            combos.add(joined.lower())
            combos.add(joined.upper())
            combos.add(joined.capitalize())
            combos.add(joined + "123")
            combos.add("123" + joined)
            combos.add("@" + joined)
            combos.add(joined + "@")
            combos.add("!" + joined)
            combos.add(joined + "!")
            combos.add(joined + "#")
            combos.add("#" + joined)
    return sorted(combos)
    # compounds


def save_to_file(data):
    file_path = filedialog.asksaveasfilename(
        defaultextension=".txt",
        filetypes=[("Text files", "*.txt")]
    )
    if file_path:
        with open(file_path, 'w') as f:
            for item in data:
                f.write(item + '\n')
        messagebox.showinfo("Success", f"Wordlist saved to {file_path}")


def generate():
    inputs = [entry.get() for entry in entries if entry.get().strip()]
    if not inputs:
        messagebox.showwarning("Input Error", "Please enter at least one word.")
        return
    result = generate_combinations(inputs)
    save_to_file(result)


# GUI setup
root = tk.Tk()
root.title("Wordgen Moji")
root.geometry("500x400")

frame = tk.Frame(root)
frame.pack(pady=30)

entries = []
labels = ["1", "2", "3(usually number!)"]

for label in labels:
    tk.Label(frame, text=label).pack()
    e = tk.Entry(frame, width=30)
    e.pack()
    entries.append(e)

tk.Button(
    root,
    text="start Wordlist",
    command=generate,
    bg="#FA82AE",
    fg="black"
).pack(pady=20)

root.mainloop()
