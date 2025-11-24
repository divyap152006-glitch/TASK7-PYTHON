import os
from PIL import Image

INPUT_FOLDER = "input_images"
OUTPUT_FOLDER = "output_images"
NEW_WIDTH = 800
NEW_HEIGHT = 800
OUTPUT_FORMAT = "JPEG"   # change to "PNG" if you want transparency

def resize_and_convert():
    if not os.path.exists(OUTPUT_FOLDER):
        os.makedirs(OUTPUT_FOLDER)

    for filename in os.listdir(INPUT_FOLDER):
        file_path = os.path.join(INPUT_FOLDER, filename)

        if not filename.lower().endswith((".jpg", ".jpeg", ".png", ".webp", ".bmp")):
            continue

        img = Image.open(file_path)

        # ⭐ FIX FOR RGBA → RGB    
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