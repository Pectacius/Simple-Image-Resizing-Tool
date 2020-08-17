from PIL import Image
from tkinter import IntVar

import custom_errors


class ImageEditor:
    """stores and modifies uploaded images"""
    VALID_FILE_TYPES = (("Bitmap files", "*.bmp*"),
                        ("JPEG files", "*.jpg*"),
                        ("PNG files", "*.png*"),
                        ("SVG files", "*.svg*"),
                        ("TIFF files", "*.tiff*"))

    REPLACE_MODES = (("Match Exact", 1), ("Match Not", 2))

    def __init__(self):
        self.mode = IntVar()
        self.mode.set(1)
        self.edited_img = None
        self.loaded_img = None

    def open_file(self, filename: str) -> None:
        self.loaded_img = Image.open(filename)
        self.edited_img = None

    def resize(self, x_ratio: str, y_ratio: str):
        """resizes image based on given x and y ratios if valid, else throw ValueError. edited_img cannot be created
        without an existing loaded_img. No existing loaded_img throws NoImageError. First searches for edited_img before
        loaded_img to resize"""

        # successfully parses entry or throws ValueError if fails
        x_value = float(x_ratio)
        y_value = float(y_ratio)

        # successfully resizes image or throws NoImageError if no image found
        if self.edited_img:
            self.edited_img = self.edited_img.resize((round(self.edited_img.size[0] * x_value),
                                                      round(self.edited_img.size[1] * y_value)))
        elif self.loaded_img:
            self.edited_img = self.loaded_img.resize((round(self.loaded_img.size[0] * x_value),
                                                      round(self.loaded_img.size[1] * y_value)))
        else:
            raise custom_errors.NoImageError()

    def replace_color(self, **kwargs) -> None:
        """replace specific pixel with another specific pixel, throws InvalidRGBAError if invalid RGBA input"""
        # check if all inputs are valid
        for arg in kwargs.values():
            if not ImageEditor.valid_color(arg):
                raise custom_errors.InvalidRGBAError()

        old_color = tuple(map(lambda x: int(x), (kwargs["ro"], kwargs["go"], kwargs["bo"], kwargs["ao"])))
        new_color = tuple(map(lambda x: int(x), (kwargs["rn"], kwargs["gn"], kwargs["bn"], kwargs["an"])))

        if self.edited_img:
            image = self.edited_img
        elif self.loaded_img:
            image = self.loaded_img
        else:
            raise custom_errors.NoImageError()

        replace_method = self.get_replace_method()
        self.edited_img = replace_method(image, old_color, new_color)

    def get_replace_method(self):
        """gets the replace method based on the selected mode"""
        mode = self.mode.get()
        if mode == 1:
            return ImageEditor.replace_exact
        elif mode == 2:
            return ImageEditor.replace_not

    @staticmethod
    def replace_exact(image, old_color, new_color) -> Image:
        """Replaces all pixels that have the same value as old_color with new_color and returns the edited image"""
        img = image.convert("RGBA")
        pixel_data = img.load()
        width, height = img.size
        for y in range(height):
            for x in range(width):
                if pixel_data[x, y] == old_color:
                    pixel_data[x, y] = new_color
        return img

    @staticmethod
    def replace_not(image, old_color, new_color) -> Image:
        """Replaces all pixels that do not have the same value as old_color with new_color
         and returns the edited image"""
        img = image.convert("RGBA")
        pixel_data = img.load()
        width, height = img.size
        for y in range(height):
            for x in range(width):
                if pixel_data[x, y] != old_color:
                    pixel_data[x, y] = new_color
        return img

    @staticmethod
    def valid_color(value) -> bool:
        """Check if value is a valid RGBA value, will also return false for empty string"""
        try:
            return 0 <= int(value) <= 255
        except ValueError:
            return False

    def unique_colors_loaded(self) -> set:
        """returns a set of unique colors in the loaded image"""
        if self.loaded_img:
            return ImageEditor.unique_colors(self.loaded_img)
        else:
            raise custom_errors.NoImageError()

    def unique_colors_edited(self) -> set:
        """returns a set of unique colors in the edited image"""
        if self.edited_img:
            return ImageEditor.unique_colors(self.edited_img)
        else:
            raise custom_errors.NoImageError()

    @staticmethod
    def unique_colors(image) -> set:
        """returns a set of unique colors in an image"""
        img = image.convert("RGBA")
        pixel_data = img.load()
        width, height = img.size
        list_of_pixels = []
        for y in range(height):
            for x in range(width):
                list_of_pixels.append(pixel_data[x, y])
        return set(list_of_pixels)
