# image_generation.py
import os
import sys
import random
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from PIL import Image, ImageDraw, ImageFont
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing.image import load_img, img_to_array

class ImageGeneration:
    def __init__(self):
        self.image_name = None
        self.image_quality = None
        self.image_model_path = "path/to/image/generation/model"
        self.image_model = self.load_image_model()
        self.amaryllis_theme_colors = ["#hex_color1", "#hex_color2", "#hex_color3"]

    def load_image_model(self):
        """
        Load the image generation model from the specified path.
        """
        try:
            return load_model(self.image_model_path)
        except Exception as e:
            print(f"Error loading image generation model: {e}")
            sys.exit(1)

    def generate_image(self, user_input, image_quality):
        """
        Generate a high-quality image based on the user input and specified image quality.
        """
        self.image_name = f"amaryllis_image_{random.randint(1000, 9999)}.png"
        self.image_quality = image_quality
        # Preprocess user_input for image generation model
        preprocessed_input = self.preprocess_input(user_input)
        # Generate image using the image generation model
        generated_image = self.image_model.predict(preprocessed_input)
        # Postprocess the generated image
        final_image = self.postprocess_image(generated_image)
        # Save the generated image
        self.save_image(final_image)
        return self.image_name

    def preprocess_input(self, user_input):
        """
        Preprocess the user input for the image generation model.
        """
        return np.array([user_input])

    def postprocess_image(self, generated_image):
        """
        Postprocess the generated image to enhance its quality and apply the Amaryllis theme.
        """
        final_image = Image.fromarray(generated_image)
        # Apply Amaryllis theme colors
        final_image = self.apply_amaryllis_theme(final_image)
        return final_image

    def apply_amaryllis_theme(self, image):
        """
        Apply the Amaryllis theme colors to the generated image.
        """
        amaryllis_colored_image = image.convert("RGB")
        color_map = list(zip(range(3), self.amaryllis_theme_colors))
        for i, color in color_map:
            amaryllis_colored_image.paste(color, [0, i * image.height // 3, image.width, (i + 1) * image.height // 3])
        return amaryllis_colored_image

    def save_image(self, image):
        """
        Save the generated image with the specified quality.
        """
        try:
            image.save(self.image_name, quality=self.image_quality)
        except Exception as e:
            print(f"Error saving generated image: {e}")
            sys.exit(1)

    def display_image(self, image_name):
        """
        Display the generated image.
        """
        try:
            image = Image.open(image_name)
            image.show()
        except Exception as e:
            print(f"Error displaying generated image: {e}")
            sys.exit(1)


if __name__ == "__main__":
    image_generator = ImageGeneration()
    user_input = "Sample user input for image generation"
    image_quality = 95
    generated_image_name = image_generator.generate_image(user_input, image_quality)
    image_generator.display_image(generated_image_name)
