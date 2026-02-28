
import os
import glob
from PIL import Image

try:
    from pillow_heif import register_heif_opener
    register_heif_opener()
except ImportError:
    print("Warning: pillow_heif not installed. Attempting to install...")
    os.system("pip install pillow-heif")
    try:
        from pillow_heif import register_heif_opener
        register_heif_opener()
    except Exception as e:
        print("Failed to setup HEIC support: ", e)

base_dir = r"C:\Users\Zonia\Desktop\JB Woodworks\Jah Images"
heic_files = glob.glob(os.path.join(base_dir, "**", "*.[hH][eE][iI][cC]"), recursive=True)

print(f"Found {len(heic_files)} HEIC files.")

for f in heic_files:
    try:
        img = Image.open(f)
        # Convert to RGB in case it has an alpha channel or is CMYK
        img = img.convert("RGB")
        target = os.path.splitext(f)[0] + ".jpg"
        if not os.path.exists(target):
            img.save(target, format="JPEG", quality=85)
            print("Converted:", f, "->", target)
        else:
            print("Already exists:", target)
    except Exception as e:
        print(f"Error converting {f}: {e}")

# What about MOV? We can try ffmpeg if available.
mov_files = glob.glob(os.path.join(base_dir, "**", "*.[mM][oO][vV]"), recursive=True)
print(f"Found {len(mov_files)} MOV files.")
for f in mov_files:
    target = os.path.splitext(f)[0] + ".mp4"
    if not os.path.exists(target):
        print(f"Attempting to convert {f} to mp4 using ffmpeg...")
        # -y to overwrite, -vcodec h264, -acodec aac
        cmd = f'ffmpeg -i "{f}" -vcodec libx264 -acodec aac -y "{target}"'
        res = os.system(cmd)
        if res == 0:
             print("Success")
        else:
             print("ffmpeg failed for", f)
    else:
        print("Already exists:", target)
