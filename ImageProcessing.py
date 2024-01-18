from PIL import Image, ImageFilter, ImageChops, ImageOps

class ImageProcessor:
    def __init__(self, image_path='girl_coffee.jpg'):
        with Image.open(image_path) as img:
            self.img = img.copy()

    def add(self, image_path='girl_coffee.jpg', scale=2, offset=0):
        with Image.open(image_path) as img2:
            result_img = ImageChops.add(self.img, img2, scale, offset)
        self.img = result_img.copy()
        return result_img

    def reverse(self):
        result_img = ImageOps.invert(self.img)
        self.img = result_img.copy()
        return result_img

    def gaussian_blur(self, intensity=8):
        """
        Apply Gaussian blur to the image.

        :param intensity: Intensity of the blur.
        :return: Resulting image after blur.
        """
        result_img = self.img.filter(ImageFilter.GaussianBlur(intensity))
        self.img = result_img.copy()
        return result_img

    def contrast(self):
        """
        Apply contrast enhancement to the image.

        :return: Resulting image after contrast enhancement.
        """
        result_img = self.img.filter(ImageFilter.EDGE_ENHANCE)
        self.img = result_img.copy()
        return result_img

    def find_edges(self):
        """
        Detect edges in the image.

        :return: Resulting image after edge detection.
        """
        result_img = self.img.filter(ImageFilter.FIND_EDGES)
        self.img = result_img.copy()
        return result_img

    def brightness(self, intensity):
        """
        Adjust the brightness of the image.

        :param intensity: Intensity of the brightness adjustment.
        :return: Resulting image after brightness adjustment.
        """
        result_img = ImageChops.add(self.img, self.img, 2, intensity)
        self.img = result_img.copy()
        return result_img

    def crop(self, x1, y1, x2, y2):
        """
        Crop the image.

        :param x1: x-coordinate of the top-left corner.
        :param y1: y-coordinate of the top-left corner.
        :param x2: x-coordinate of the bottom-right corner.
        :param y2: y-coordinate of the bottom-right corner.
        :return: Resulting cropped image.
        """
        result_img = self.img.crop((x1, y1, x2, y2))
        self.img = result_img.copy()
        return result_img

    def set_image(self, image_path='girl_coffee.jpg'):
        """
        Set the image to a new image file.

        :param image_path: Path to the new image file.
        """
        with Image.open(image_path) as img2:
            self.img = img2.copy()

    def get_image(self):
        """
        Get the current image.

        :return: Image object.
        """
        return self.img.copy()

    def show(self):
        """
        Show the image.
        """
        self.img.show()


# Example Usage:
processor = ImageProcessor('girl_coffee.jpg')
processor.add('girl_coffee.jpg')
processor.show()
