import ffmpeg
import os
import tkinter as tk
from tkinter import filedialog, messagebox

# Function to select file
def select_file():
    file_path = filedialog.askopenfilename(
        title="Select DAT file",
        filetypes=[("DAT files", "*.dat")]
    )
    entry.delete(0, tk.END)
    entry.insert(0, file_path)

# Function to convert
def convert_file():
    input_path = entry.get().strip()

    if not input_path:
        messagebox.showerror("Error", "Please select a file first!")
        return

    if not os.path.exists(input_path):
        messagebox.showerror("Error", "File does not exist!")
        return

    if not input_path.lower().endswith(".dat"):
        messagebox.showerror("Error", "Please select a .dat file!")
        return

    output_path = os.path.splitext(input_path)[0] + ".mp4"

    try:
        status_label.config(text="⏳ Converting...", fg="blue")
        root.update()

        (
            ffmpeg
            .input(input_path)
            .output(output_path)
            .run(overwrite_output=True)
        )

        status_label.config(text="✅ Conversion Successful!", fg="green")
        messagebox.showinfo("Success", f"Saved as:\n{output_path}")

    except ffmpeg.Error as e:
        status_label.config(text="❌ Conversion Failed", fg="red")
        messagebox.showerror("Error", e.stderr.decode())

# GUI setup
root = tk.Tk()
root.title("DAT to MP4 Converter")
root.geometry("500x200")
root.resizable(False, False)

# Title
title = tk.Label(root, text="DAT to MP4 Converter", font=("Arial", 16))
title.pack(pady=10)

# Entry box
entry = tk.Entry(root, width=50)
entry.pack(pady=5)

# Browse button
browse_btn = tk.Button(root, text="Browse File", command=select_file)
browse_btn.pack(pady=5)

# Convert button
convert_btn = tk.Button(root, text="Convert", command=convert_file, bg="green", fg="white")
convert_btn.pack(pady=10)

# Status label
status_label = tk.Label(root, text="", font=("Arial", 10))
status_label.pack()

# Run app
root.mainloop()
