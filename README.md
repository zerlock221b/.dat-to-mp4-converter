# 🖥️ DAT to MP4 Converter (GUI Version)

A simple desktop application built using **Python (Tkinter) + FFmpeg** that allows users to convert `.DAT` video files into `.MP4` format using a graphical interface — no terminal required.

---

## 🚀 Features

* 📂 File picker to select `.DAT` files
* ▶️ One-click conversion
* ✅ Success & error popups
* 📁 Output saved automatically as `.mp4`
* 🧠 Beginner-friendly and lightweight

---

## 🛠️ Tech Stack

* Python 3
* Tkinter (built-in GUI library)
* FFmpeg
* ffmpeg-python

---

## 📦 Installation & Setup (From Scratch)

---

### 🔹 1. Install Python

Download from: https://www.python.org/downloads/
✔️ Make sure to check **"Add Python to PATH"**

---

### 🔹 2. Install FFmpeg

1. Download FFmpeg (from GitHub builds or other trusted source)
2. Extract the ZIP
3. Move folder to:

   ```
   C:\ffmpeg
   ```
4. Add this to **System PATH**:

   ```
   C:\ffmpeg\...\bin
   ```

#### ✅ Verify installation:

```bash
ffmpeg -version
```

---

### 🔹 3. Install Required Package

Open terminal in VS Code:

```bash
pip install ffmpeg-python
```

---

### 🔹 4. Project Structure

```bash
dat_converter_gui/
│
├── gui_converter.py
└── README.md
```

---

## 🧠 How It Works

1. User selects a `.DAT` file using the file browser
2. App validates:

   * File exists
   * Correct `.dat` format
3. FFmpeg converts the file to `.MP4`
4. Output is saved in the same directory

---

## 💻 Full Code

```python
import ffmpeg
import os
import tkinter as tk
from tkinter import filedialog, messagebox

def select_file():
    file_path = filedialog.askopenfilename(
        title="Select DAT file",
        filetypes=[("DAT files", "*.dat")]
    )
    entry.delete(0, tk.END)
    entry.insert(0, file_path)

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

root = tk.Tk()
root.title("DAT to MP4 Converter")
root.geometry("500x200")
root.resizable(False, False)

title = tk.Label(root, text="DAT to MP4 Converter", font=("Arial", 16))
title.pack(pady=10)

entry = tk.Entry(root, width=50)
entry.pack(pady=5)

browse_btn = tk.Button(root, text="Browse File", command=select_file)
browse_btn.pack(pady=5)

convert_btn = tk.Button(root, text="Convert", command=convert_file, bg="green", fg="white")
convert_btn.pack(pady=10)

status_label = tk.Label(root, text="", font=("Arial", 10))
status_label.pack()

root.mainloop()
```

---

## ▶️ How to Run

1. Open project folder in VS Code
2. Open terminal
3. Run:

   ```bash
   python gui_converter.py
   ```
4. GUI window will open 🎉

---

## ⚠️ Common Errors & Fixes

---

### ❌ Error: `ModuleNotFoundError: No module named 'ffmpeg'`

✅ Fix:

```bash
python -m pip install ffmpeg-python
```

---

### ❌ Error: `can't open file`

👉 You're in the wrong directory

✅ Fix:

```bash
cd path\to\your\project
python gui_converter.py
```

---

### ❌ Error: `SyntaxError: invalid syntax`

👉 Caused by accidental line:

```python
python
```

✅ Fix:

* Remove that line from your `.py` file

---

## 📌 Notes

* `.DAT` file must contain video data
* FFmpeg must be properly installed
* Restart VS Code if commands don't work

---

## 🔮 Future Improvements

* Drag & drop support 🖱️
* Batch conversion 🔁
* Progress bar 📊
* Dark mode 🌙
* Convert to `.exe` app 📦

---

## 🙌 Acknowledgment

Powered by **FFmpeg**, a powerful open-source multimedia framework.

---

## ⭐ License

Free to use and modify.
