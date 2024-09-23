import os
import time
from PIL import Image, ImageDraw, ImageFont

def create_text_to_image(width, height, countdown_time, background_color="black", font_path=None, font_size=58, text_color=255, output_file="text_to_image.png", fill_amount = 0):
    image = Image.new("L", (width, height), color=0)
    draw = ImageDraw.Draw(image)
    
    if font_path:
        font = ImageFont.truetype(font_path, font_size)
    else:
        font = ImageFont.load_default()
    
    text_bbox = draw.textbbox((0, 0), countdown_time, font=font)
    text_width = text_bbox[2] - text_bbox[0]
    text_height = text_bbox[3] - text_bbox[1]
    
    text_x = (width - text_width) // 2
    text_y = (height - text_height - 30) // 2
    
    draw.text((text_x, text_y), countdown_time, font=font, fill=text_color)

    padding = 20
    circle_radius = 110
    fill_degree = -90 + fill_amount

    center_x = 120
    center_y = 140

    outer_circle_bbox = [
        center_x - 5 - circle_radius, center_y - 5 - circle_radius, 
        center_x + 5 + circle_radius, center_y + 5 + circle_radius 
    ]

    inner_circle_bbox = [
        center_x + 4 - circle_radius, center_y + 4 - circle_radius, 
        center_x - 4 + circle_radius, center_y - 4 + circle_radius 
    ]

    fill_circle_bbox = [
        center_x - 5 - circle_radius, center_y - 5 - circle_radius, 
        center_x + 5 + circle_radius, center_y + 5 + circle_radius 
    ]

    arc_fill_bbox = [
        center_x - 5 - circle_radius, center_y - 5 - circle_radius, 
        center_x + 5 + circle_radius, center_y + 5 + circle_radius 
    ]

    draw.ellipse(outer_circle_bbox, outline="white", width=1)
    draw.arc(arc_fill_bbox, -90, fill_degree, fill="white", width = 9)
    
    image.save(output_file)

def generate_last_10_images(font_path, output_dir, countdown_time_sec, countdown_type):
    one_second_fill = 360 / countdown_time_sec
    generated_files = []
    for seconds_remaining in range(9, -1, -1):
        countdown_display = f"00:{seconds_remaining:02d}"
        file_name = f"{countdown_type}_00_{seconds_remaining:02d}.png"
        output_file = f"{output_dir}://{file_name}"
        fill_amount = (countdown_time_sec - seconds_remaining) * one_second_fill
        create_text_to_image(width=240, height=280, countdown_time=countdown_display, font_path=font_path, output_file=output_file, fill_amount = fill_amount)
        generated_files.append(output_file)

    return generated_files

def delete_generated_files(files):
    for file in files:
        if os.path.exists(file):
            try:
                os.remove(file)
            except OSError as e:
                print(f"Error deleting file {file}: {e}")