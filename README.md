# .dat-to-mp4-converter
This picks up your dat video files and turns them into simple mp4 files so that your decades old videos are not lost. 


# 🎬 DAT to MP4 Converter (Python + FFmpeg)

This project provides a simple and efficient way to convert `.DAT` video files into `.MP4` format using Python and FFmpeg. It is designed for beginners working in VS Code and helps automate video conversion with minimal setup.

---

## 🚀 Features

* Convert `.DAT` video files to `.MP4`
* Works with FFmpeg (highly reliable for video processing)
* Beginner-friendly Python script
* Runs directly in VS Code terminal
* Handles invalid file paths and formats gracefully

---

## 🛠️ Tech Stack

* Python 3
* FFmpeg
* ffmpeg-python (Python wrapper for FFmpeg)
* VS Code

---

## 📦 Installation & Setup

### 1. Install Python

Download and install Python from:
https://www.python.org/downloads/

> أثناء installation, ensure **"Add Python to PATH"** is checked.

---

### 2. Install FFmpeg

1. Download FFmpeg from a trusted source (e.g., GitHub FFmpeg builds)
2. Extract the ZIP file
3. Move the folder to:

   ```
   C:\ffmpeg
   ```
4. Copy the path of the `bin` folder, e.g.:

   ```
   C:\ffmpeg\ffmpeg-xxxx\bin
   ```
5. Add it to **System Environment Variables → Path**

#### ✅ Verify installation:

```bash
ffmpeg -version
```

---

### 3. Install Required Python Package

Open terminal in VS Code and run:

```bash
pip install ffmpeg-python
```

---

## 📁 Project Structure

```
dat_to_mp4_converter/
│
├── convert.py
├── sample.dat
└── README.md
```

---

## 🧠 How the Code Works

The script uses `ffmpeg-python` to call FFmpeg internally and convert the video format.

### 🔍 Key Steps:

1. **Input Validation**

   * Checks if file exists
   * Ensures file has `.dat` extension

2. **Output Handling**

   * Automatically generates `.mp4` filename if not provided

3. **Conversion**

   * Uses FFmpeg to process video:

     ```python
     ffmpeg.input(input_path).output(output_path).run()
     ```

4. **Error Handling**

   * Displays readable errors if conversion fails

---

## 🧾 Full Code

```python
import ffmpeg
import os

def convert_dat_to_mp4(input_path, output_path=None):
    if not os.path.exists(input_path):
        print(f"❌ File not found: {input_path}")
        return

    if not input_path.lower().endswith('.dat'):
        print("❌ Input file must have a .dat extension.")
        return

    if output_path is None:
        output_path = os.path.splitext(input_path)[0] + '.mp4'

    try:
        ffmpeg.input(input_path).output(output_path).run(overwrite_output=True)
        print(f"✅ Conversion successful! MP4 saved as: {output_path}")
    except ffmpeg.Error as e:
        print("⚠️ An error occurred during conversion:")
        print(e.stderr.decode())

if __name__ == "__main__":
    input_file = input("Enter the full path of the .dat file: ")
    convert_dat_to_mp4(input_file)
```

---

## ▶️ How to Run

1. Open project folder in VS Code
2. Open terminal
3. Run:

   ```bash
   python convert.py
   ```
4. Enter the full path of your `.dat` file when prompted

---

## 📌 Example

```
Input:
C:\Users\User\Videos\sample.dat

Output:
C:\Users\User\Videos\sample.mp4
```

---

## ⚠️ Notes

* `.DAT` files must contain video data (e.g., VCD files)
* FFmpeg must be properly added to system PATH
* Restart VS Code if FFmpeg is not recognized

---

## 🔮 Future Improvements

* Drag-and-drop file support
* GUI-based interface (Tkinter / PyQt)
* Batch conversion for multiple files
* File explorer integration

---

## 🙌 Acknowledgment

This project uses FFmpeg, a powerful open-source multimedia framework for handling video, audio, and other media files.

---

## 📬 Contributing

Feel free to fork the repo, raise issues, or submit pull requests to improve the project.

---

## ⭐ License

This project is open-source and free to use.
