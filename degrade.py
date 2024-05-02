import os
import sys
from PIL import Image

def reduce_image_quality(input_image_path, output_image_path=None, quality=85):
    """
    Уменьшает качество изображения.

    :param input_image_path: Путь к исходному изображению.
    :param output_image_path: Путь к создаваемому изображению с пониженным качеством.
    :param quality: Качество изображения (от 0 до 100, где 100 - максимальное качество).
    """
    image = Image.open(input_image_path)
    rgb_image = image.convert('RGB')
    rgb_image.save(output_image_path, quality=quality)

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python script.py input_image_path [output_image_path] [quality]")
        sys.exit(1)

    input_image_path = sys.argv[1]
    output_image_path = os.path.splitext(input_image_path)[0] + "_reduced.jpg"
    quality = 10

    if len(sys.argv) > 2:
        output_image_path = sys.argv[2]
    if len(sys.argv) > 3:
        quality = int(sys.argv[3])

    reduce_image_quality(input_image_path, output_image_path, quality)
