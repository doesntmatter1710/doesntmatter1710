import sys
import cv2
import numpy as np
from PIL import Image
from rembg import remove, new_session

if len(sys.argv) < 2:
    print("Usage: python scripts/prep_photo.py <input_image>")
    sys.exit(1)

input_path = sys.argv[1]

print("Removing background using u2net model...")
# Create session with the smaller 170 MB u2net model
session = new_session("u2net")

with open(input_path, 'rb') as i:
    input_data = i.read()
    output_data = remove(input_data, session=session)

nparr = np.frombuffer(output_data, np.uint8)
img = cv2.imdecode(nparr, cv2.IMREAD_UNCHANGED)

# Convert transparency (PNG alpha channel) to solid white background
if img.shape[2] == 4:
    alpha = img[:, :, 3]
    rgb = img[:, :, :3]
    white_bg = np.ones_like(rgb, dtype=np.uint8) * 255
    alpha_factor = alpha[:, :, np.newaxis] / 255.0
    base = (rgb * alpha_factor + white_bg * (1 - alpha_factor)).astype(np.uint8)
else:
    base = img

# Convert to grayscale and apply CLAHE contrast enhancement
gray = cv2.cvtColor(base, cv2.COLOR_BGR2GRAY)
clahe = cv2.createCLAHE(clipLimit=3.0, tileGridSize=(8,8))
enhanced = clahe.apply(gray)

cv2.imwrite("source-prepped.png", enhanced)
print("Done! Prepped image saved as 'source-prepped.png'.")