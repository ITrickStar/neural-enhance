import sys
from PIL import Image

def compare_images(image1_path, image2_path):
    """
    Сравнивает два изображения пиксель за пикселем.

    :param image1_path: Путь к первому изображению.
    :param image2_path: Путь ко второму изображению.
    :return: True, если изображения идентичны, False в противном случае.
    """
    image1 = Image.open(image1_path)
    image2 = Image.open(image2_path)

    if image1.size != image2.size:
        return False

    for y in range(image1.height):
        for x in range(image1.width):
            pixel1 = image1.getpixel((x, y))
            pixel2 = image2.getpixel((x, y))
            if pixel1 != pixel2:
                return False
    return True

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python script.py image1_path image2_path")
        sys.exit(1)

    image1_path = sys.argv[1]
    image2_path = sys.argv[2]

    if compare_images(image1_path, image2_path):
        print("Изображения идентичны.")
    else:
        print("Изображения отличаются.")
