import json

PALETTE = ["#161b22", "#0e4429", "#006d32", "#26a641", "#39d353", "#69f0a0"]

with open("data/contributions.json") as f:
    data = json.load(f)

days = data.get("days", [])

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
    color = PALETTE[min(day["level"], len(PALETTE) - 1)]
    delay = (week + dow) * 0.1

    svg_lines.append(f'    <rect x="{x}" y="{y}" width="{BOX_SIZE}" height="{BOX_SIZE}" rx="2" fill="{color}">')
    svg_lines.append(f'      <animate attributeName="opacity" values="0.25;1;0.25" begin="{delay:.2f}s" dur="6s" repeatCount="indefinite" />')
    svg_lines.append(f'    </rect>')
    svg_lines.append('  </g>')
    svg_lines.append('</svg>')

with open("contrib-heatmap.svg", "w", encoding="utf-8") as f:
    f.write("\n".join(svg_lines))

print("Generated contrib-heatmap.svg successfully!")