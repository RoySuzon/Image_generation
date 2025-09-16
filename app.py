from flask import Flask, send_file, request
from PIL import Image, ImageDraw, ImageFont
import random
import os

app = Flask(__name__)

class TextAvatarGenerator:
    def __init__(self):
        # Default avatar size
        self.default_width = 200
        self.default_height = 200
        self.bg_colors = ["#FF5733", "#33FF57", "#5733FF", "#FFC300", "#C70039", "#900C3F"]
        self.font_path = "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf"  # Adjust as needed for the Docker container

    def generate_avatar(self, text="Avatar", output_path="generated/generated_avatar.png", width=200, height=200):
        # If width or height is missing, make the image square
        if not width:
            width = height
        if not height:
            height = width
        
        # Ensure the generated directory exists
        os.makedirs(os.path.dirname(output_path), exist_ok=True)

        # Choose a random background color
        bg_color = random.choice(self.bg_colors)

        # Create a blank image with the chosen background color
        image = Image.new("RGB", (width, height), color=bg_color)

        # Initialize drawing context
        draw = ImageDraw.Draw(image)

        # Adjust font size based on the size of the image
        font_size = self.get_font_size(text, width, height)
        font = ImageFont.truetype(self.font_path, font_size)

        # Calculate the size of the text to be drawn
        text_width, text_height = draw.textsize(text, font=font)

        # Calculate position to center the text
        text_position = ((width - text_width) // 2, (height - text_height) // 2)

        # Draw the text
        draw.text(text_position, text, font=font, fill="white")

        # Save the generated avatar
        image.save(output_path)

    def get_font_size(self, text, width, height):
        """
        Adjust the font size based on the size of the image.
        """
        base_font_size = int(min(width, height) / 5)  # Font size is proportional to the image size

        # Adjust the font size based on the length of the text
        text_length = len(text)
        
        # Scale the font size down if the text is too long
        scaling_factor = 1 - (text_length - 1) * 0.05  # Scale by 5% per character beyond the first
        
        # Ensure font size is within limits
        font_size = int(base_font_size * scaling_factor)
        font_size = max(font_size, 20)  # Minimum font size is 20
        return font_size


@app.route('/generate-avatar', methods=['GET'])
def generate_avatar():
    # Get custom text, first name, last name from query parameters
    first_name = request.args.get('first_name', '')
    last_name = request.args.get('last_name', '')
    
    # If no last name is provided, combine first name with first two letters of the first name
    if not last_name:
        text = (first_name[:2] if first_name else 'AV')
    else:
        # Use first letter of first name and first letter of last name
        text = first_name[0].upper() + last_name[0].upper()

    # Optionally allow user to adjust the size of the avatar through query parameters
    width = request.args.get('width', default=None, type=int)
    height = request.args.get('height', default=None, type=int)

    # Auto adjust width and height to make the avatar square if one of them is missing
    if width is None and height is None:
        width, height = self.default_width, self.default_height
    elif width is None:
        width = height
    elif height is None:
        height = width

    # Create avatar image
    generator = TextAvatarGenerator()
    avatar_path = "generated/generated_avatar.png"
    generator.generate_avatar(text, avatar_path, width, height)

    # Return the generated avatar image as a response
    return send_file(avatar_path, mimetype='image/png')


if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=5000)
