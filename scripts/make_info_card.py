title = "doesntmatter1710@github ~ $"
info_items = [
    ("OS", "Windows / WSL (Ubuntu)"),
    ("Languages", "C++, Python, JavaScript"),
    ("Stack", "Node.js, Express, MongoDB, React, Tailwind"),
    ("Focus", "Full-Stack Dev, OSINT & Security Tools"),
    ("Tools", "VS Code, Git, DaVinci Resolve")
]

svg_w, svg_h = 490, 300

svg_content = [
    f'<svg xmlns="http://www.w3.org/2000/svg" width="{svg_w}" height="{svg_h}" viewBox="0 0 {svg_w} {svg_h}">',
    '  <style>',
    '    .title { font-family: monospace; font-size: 14px; font-weight: bold; fill: #58a6ff; }',
    '    .label { font-family: monospace; font-size: 12px; font-weight: bold; fill: #79c0ff; }',
    '    .value { font-family: monospace; font-size: 12px; fill: #c9d1d9; }',
    '    .prompt { font-family: monospace; font-size: 12px; fill: #7ee787; }',
    '  </style>',
    '  <rect width="100%" height="100%" fill="#0d1117" rx="6" stroke="#30363d" stroke-width="1" />',
    '  <g transform="translate(20, 30)">',
    f'    <text class="title">{title}</text>',
    '    <line x1="0" y1="12" x2="450" y2="12" stroke="#30363d" stroke-width="1" />'
]

y_offset = 40
for idx, (label, val) in enumerate(info_items):
    delay = idx * 0.15
    svg_content.append(f'    <g opacity="0" transform="translate(0, {y_offset})">')
    svg_content.append(f'      <text class="prompt">&gt; </text>')
    svg_content.append(f'      <text x="15" class="label">{label}:</text>')
    svg_content.append(f'      <text x="120" class="value">{val}</text>')
    svg_content.append(f'      <animate attributeName="opacity" to="1" begin="{delay}s" dur="0.2s" fill="freeze" />')
    svg_content.append(f'    </g>')
    y_offset += 35

svg_content.append('  </g>')
svg_content.append('</svg>')

with open("info-card.svg", "w", encoding="utf-8") as f:
    f.write("\n".join(svg_content))

print("Generated info-card.svg successfully!")