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

# ✏️ Ask user for the .dat file path
if __name__ == "__main__":
    input_file = input("Enter the full path of the .dat file: ")
    convert_dat_to_mp4(input_file)
