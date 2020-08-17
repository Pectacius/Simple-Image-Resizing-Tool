import tkinter as tk

import custom_errors
import popup as pop


class Resize(tk.Frame):
    """Frame that holds resizing tool utilities"""

    def __init__(self, editor, **kw):
        super().__init__(highlightbackground="grey", highlightthickness=1, width=480, height=100, **kw)
        self.editor = editor

        validate = (self.register(lambda p: Resize.is_number(p) or p == ""))

        tk.Label(self, text="Resize Tool", borderwidth=2, relief="ridge").place(x=0, y=0)

        resize = tk.Button(self, text="Resize", command=self.resize)
        resize.place(x=380, y=60, width=80)

        clear = tk.Button(self, text="Clear", command=self.clear)
        clear.place(x=290, y=60, width=80)

        self.x_input = tk.Entry(self, validate="all", validatecommand=(validate, '%P'))
        self.y_input = tk.Entry(self, validate="all", validatecommand=(validate, '%P'))
        self.x_input.place(x=380, y=10, width=80)
        self.y_input.place(x=380, y=35, width=80)

        tk.Label(self, text="X Ratio").place(x=330, y=10, width=40)
        tk.Label(self, text="Y Ratio").place(x=330, y=35, width=40)

        self.img_x = tk.Label(self, text="Loaded X Size: ")
        self.img_x.place(x=10, y=30, width=100)
        self.img_y = tk.Label(self, text="Loaded Y Size: ")
        self.img_y.place(x=10, y=60, width=100)

        self.resize_x = tk.Label(self, text="Resized X Size: ")
        self.resize_x.place(x=150, y=30, width=100)
        self.resize_y = tk.Label(self, text="Resized Y Size: ")
        self.resize_y.place(x=150, y=60, width=100)

        self.place(x=10, y=100)

    def resize(self) -> None:
        """Converts input ratios if possible and resizes loaded image using the ratio. Also updates image dimension
         information. If resize not possible error popup displayed"""
        try:
            self.editor.resize(self.x_input.get(), self.y_input.get())
        except ValueError:
            pop.Popup("Not A Valid Input, Only Numbers Allowed")
        except custom_errors.NoImageError:
            pop.Popup("No Image Loaded")
        else:
            self.resize_x.configure(text=f"Resized X Size: {self.editor.edited_img.size[0]}")
            self.resize_y.configure(text=f"Resized Y Size: {self.editor.edited_img.size[1]}")
            pop.Popup("Success")

    def clear(self) -> None:
        """Clears entries from entry inputs"""
        self.x_input.delete(0, 'end')
        self.y_input.delete(0, 'end')

    @staticmethod
    def is_number(value) -> bool:
        """Return true if value can be cast to float, else return false"""
        try:
            float(value)
            return True
        except ValueError:
            return False
