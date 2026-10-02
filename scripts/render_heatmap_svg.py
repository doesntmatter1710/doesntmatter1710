import json
import os

PALETTE = ["#161b22", "#0e4429", "#006d32", "#26a641", "#39d353", "#69f0a0"]

# Ensure data file exists and load it safely
days = []
if os.path.exists("data/contributions.json"):
    try:
        with open("data/contributions.json", "r", encoding="utf-8") as f:
            data = json.load(f)
            days = data.get("days", [])
    except Exception as e:
        print(f"Error reading JSON: {e}")

BOX_SIZE = 11
GAP = 3

svg_w = 860
svg_h = 160

svg_lines = [
    f'<svg xmlns="http://www.w3.org/2000/svg" width="{svg_w}" height="{svg_h}" viewBox="0 0 {svg_w} {svg_h}">',
    '  <rect width="100%" height="100%" fill="#0d1117" rx="6" stroke="#30363d" stroke-width="1" />',
    '  <text x="20" y="20" font-family="monospace" font-size="12" font-weight="bold" fill="#8b949e">Contribution Activity</text>',
    '  <g transform="translate(20, 35)">'
]

for idx, day in enumerate(days):
    week = idx // 7
    dow = idx % 7
    x = week * (BOX_SIZE + GAP)
    y = dow * (BOX_SIZE + GAP)
    
    level = min(max(day.get("level", 0), 0), len(PALETTE) - 1)
    color = PALETTE[level]
    delay = round((week + dow) * 0.08, 2)

    rect_element = (
        f'    <rect x="{x}" y="{y}" width="{BOX_SIZE}" height="{BOX_SIZE}" rx="2" fill="{color}" opacity="0">\n'
        f'      <animate attributeName="opacity" to="1" begin="{delay}s" dur="0.8s" fill="freeze" />\n'
        f'    </rect>'
    )
    svg_lines.append(rect_element)

svg_lines.append('  </g>')
svg_lines.append('</svg>')

with open("contrib-heatmap.svg", "w", encoding="utf-8") as f:
    f.write("\n".join(svg_lines))

print("Generated contrib-heatmap.svg successfully!")