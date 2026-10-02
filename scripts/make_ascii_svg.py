import cv2
import numpy as np

RAMP = " .`:-=+*cs#%@"
WIDTH = 100
CHAR_WIDTH = 6
LINE_HEIGHT = 10

img = cv2.imread("source-prepped.png", cv2.IMREAD_GRAYSCALE)
if img is None:
    print("Error: source-prepped.png not found!")
    exit(1)

aspect_ratio = img.shape[0] / img.shape[1]
height = int(WIDTH * aspect_ratio * 0.55)
resized = cv2.resize(img, (WIDTH, height))

num_chars = len(RAMP)
rows = []
for r in resized:
    line = "".join([RAMP[int((pixel / 255) * (num_chars - 1))] for pixel in r])
    line = line.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;").replace(" ", "&#160;")
    rows.append(line)

svg_w = WIDTH * CHAR_WIDTH + 20
svg_h = height * LINE_HEIGHT + 20

svg_lines = [
    f'<svg xmlns="http://www.w3.org/2000/svg" width="{svg_w}" height="{svg_h}" viewBox="0 0 {svg_w} {svg_h}">',
    '  <style>',
    '    .ascii-text { font-family: monospace; font-size: 10px; fill: #8b949e; white-space: pre; }',
    '  </style>',
    '  <rect width="100%" height="100%" fill="#0d1117" rx="6" />',
    '  <g transform="translate(10, 15)">'
]

for idx, row in enumerate(rows):
    y_pos = idx * LINE_HEIGHT
    delay = idx * 0.05
    svg_lines.append(f'    <text x="0" y="{y_pos}" class="ascii-text" opacity="0">{row}')
    svg_lines.append(f'      <animate attributeName="opacity" to="1" begin="{delay}s" dur="0.01s" fill="freeze" />')
    svg_lines.append(f'    </text>')

svg_lines.append('  </g>')
svg_lines.append('</svg>')

with open("avi-ascii.svg", "w", encoding="utf-8") as f:
    f.write("\n".join(svg_lines))

print("Generated avi-ascii.svg successfully!")