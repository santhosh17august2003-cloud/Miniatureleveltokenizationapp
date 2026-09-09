import os
from pathlib import Path
from PIL import Image, ImageDraw, ImageFont

def generate_app_icon(output_dir: Path):
    output_dir.mkdir(parents=True, exist_ok=True)
    size = 512
    img = Image.new("RGBA", (size, size), (0, 0, 0, 0))
    draw = ImageDraw.Draw(img)

    # Background rounded rectangle with gradient effect
    bg_color_start = (30, 41, 59)     # Deep Slate #1E293B
    bg_color_end = (37, 99, 235)      # Royal Blue #2563EB
    accent_cyan = (6, 182, 212)       # Cyan #06B6D4
    accent_emerald = (16, 185, 129)   # Emerald #10B981

    # Draw rounded background
    corner_radius = 110
    draw.rounded_rectangle(
        [(20, 20), (size - 20, size - 20)],
        radius=corner_radius,
        fill=(15, 23, 42, 255),
        outline=(59, 130, 246, 220),
        width=12
    )

    # Inner glowing card representing a token box
    draw.rounded_rectangle(
        [(80, 80), (size - 80, size - 80)],
        radius=70,
        fill=(30, 41, 59, 230),
        outline=accent_cyan,
        width=8
    )

    # Draw token brackets: [  ]
    bracket_color = accent_cyan
    b_thickness = 18
    # Left bracket
    draw.line([(140, 150), (190, 150)], fill=bracket_color, width=b_thickness)
    draw.line([(140, 150), (140, 360)], fill=bracket_color, width=b_thickness)
    draw.line([(140, 360), (190, 360)], fill=bracket_color, width=b_thickness)

    # Right bracket
    draw.line([(size - 140, 150), (size - 190, 150)], fill=bracket_color, width=b_thickness)
    draw.line([(size - 140, 150), (size - 140, 360)], fill=bracket_color, width=b_thickness)
    draw.line([(size - 140, 360), (size - 190, 360)], fill=bracket_color, width=b_thickness)

    # Letter 'T' for Tokenization in center
    # Center crossbar of T
    draw.rounded_rectangle(
        [(200, 180), (312, 215)],
        radius=8,
        fill=(255, 255, 255, 255)
    )
    # Stem of T
    draw.rounded_rectangle(
        [(238, 215), (274, 330)],
        radius=8,
        fill=(255, 255, 255, 255)
    )

    # Digital neural vector dots at bottom representing embeddings [0.82, -0.41, ...]
    dot_y = 395
    dot_positions = [170, 215, 256, 297, 342]
    colors = [accent_cyan, accent_emerald, (245, 158, 11), (168, 85, 247), accent_cyan]
    for x, col in zip(dot_positions, colors):
        r = 14
        draw.ellipse([(x - r, dot_y - r), (x + r, dot_y + r)], fill=col)

    # Save PNG
    png_path = output_dir / "app_icon.png"
    img.save(png_path, format="PNG")
    print(f"Saved PNG to {png_path}")

    # Generate ICO with multiple resolutions
    ico_path = output_dir / "app_icon.ico"
    sizes = [(16, 16), (24, 24), (32, 32), (48, 48), (64, 64), (128, 128), (256, 256)]
    img.save(ico_path, format="ICO", sizes=sizes)
    print(f"Saved ICO to {ico_path}")

if __name__ == "__main__":
    current_dir = Path(__file__).resolve().parent
    assets_dir = current_dir / "assets"
    generate_app_icon(assets_dir)
