import sys
import cv2
import numpy as np

# Character density ramp (from bright/empty to dark/dense)
RAMP = " .`:-=+*cs#%@"

if len(sys.argv) < 2:
    print("Usage: python scripts/preview_ascii.py <image_path> [width]")
    sys.exit(1)

img_path = sys.argv[1]
width = int(sys.argv[2]) if len(sys.argv) > 2 else 80

# Load image in grayscale
img = cv2.imread(img_path, cv2.IMREAD_GRAYSCALE)
if img is None:
    print(f"Error: Could not load image '{img_path}'. Make sure prep_photo.py ran successfully first!")
    sys.exit(1)

# Aspect ratio correction (terminal characters are roughly twice as tall as wide)
aspect_ratio = img.shape[0] / img.shape[1]
height = int(width * aspect_ratio * 0.55)

resized = cv2.resize(img, (width, height))

# Map brightness (0-255) to character ramp index
num_chars = len(RAMP)
ascii_rows = []

for row in resized:
    line = "".join([RAMP[int((pixel / 255) * (num_chars - 1))] for pixel in row])
    ascii_rows.append(line)

print("\n" + "="*width)
print("\n".join(ascii_rows))
print("="*width + "\n")