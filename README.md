# TASK7-PYTHON
# Image Resizer & Converter Tool

This project allows you to batch resize and convert images using Python and the Pillow library.

## 🚀 Features
- Resize all images in a folder
- Convert images to JPEG/PNG/WebP
- Fixes RGBA transparency errors
- Automatically saves output images in a separate folder
- Supports JPG, JPEG, PNG, BMP, WEBP formats

---

## 📁 Folder Structure
```
your_project/
│── image_resizer.py
│── input_images/
│      ├── photo1.jpg
│      ├── image.png
│      ├── dog.webp
│
└── output_images/
        ├── photo1_resized.jpg
        ├── image_resized.jpg
        ├── dog_resized.jpg
```

---

## 🛠 Requirements
Install Pillow:
```
pip install pillow
```

---

## ▶ How to Use
1. Create a folder named `input_images`
2. Put all images you want to resize inside it
3. Run the script:
```
python image_resizer.py
```
4. Resized images will appear in `output_images` folder

---

## 🧩 Code Used
```
import os
from PIL import Image

INPUT_FOLDER = "input_images"
OUTPUT_FOLDER = "output_images"
NEW_WIDTH = 800
NEW_HEIGHT = 800
OUTPUT_FORMAT = "JPEG"

def resize_and_convert():
    if not os.path.exists(OUTPUT_FOLDER):
        os.makedirs(OUTPUT_FOLDER)

    for filename in os.listdir(INPUT_FOLDER):
        file_path = os.path.join(INPUT_FOLDER, filename)

        if not filename.lower().endswith((".jpg", ".jpeg", ".png", ".webp", ".bmp")):
            continue

        img = Image.open(file_path)

        if img.mode == "RGBA":
            img = img.convert("RGB")

        img = img.resize((NEW_WIDTH, NEW_HEIGHT))

        base_name = os.path.splitext(filename)[0]
        output_file = f"{base_name}_resized.jpg"
        output_path = os.path.join(OUTPUT_FOLDER, output_file)

        img.save(output_path, "JPEG")

        print(f"Saved: {output_file}")

    print("\n✔ All images processed successfully!")

if __name__ == "__main__":
    resize_and_convert()
```

---

## ✅ Output Example
Inside `output_images`, you will get something like:
```
photo1_resized.jpg
dog_resized.jpg
image_resized.jpg
```

---

## ✔ Troubleshooting
### ❗ Error: **cannot write mode RGBA as JPEG**
Solution: Convert to RGB before saving  
Already included in the script:
```
if img.mode == "RGBA":
    img = img.convert("RGB")
```

---

## 📜 License
This project is free to use.
