from typing import Union

import PIL
from tkinter import IntVar


class ImageEditor:
    """stores and modifies uploaded images"""
    VALID_FILE_TYPES = (("Bitmap files", "*.bmp*"),
                        ("JPEG files", "*.jpg*"),
                        ("PNG files", "*.png*"),
                        ("SVG files", "*.svg*"),
                        ("TIFF files", "*.tiff*"))

    REPLACE_MODES = (("Match Exact", 1), ("Match Not", 2))

    edited_img = None
    loaded_img = None

    def __init__(self):
        self.mode = IntVar()
        self.mode.set(1)

    def open_file(self, filename: str) -> None:
        self.loaded_img = PIL.Image.open(filename)
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
            raise NoImageError()


class NoImageError(Exception):
    """represents no loaded image"""
    pass
