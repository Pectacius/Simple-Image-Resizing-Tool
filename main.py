from PIL import Image
from tkinter import Button, Entry, filedialog, Label, Tk


class Editor(Tk):
    """Editor for resizing images"""
    valid_file_types = (("Bitmap files", "*.bmp*"),
                        ("JPEG files", "*.jpg*"),
                        ("PNG files", "*.png*"),
                        ("SVG files", "*.svg*"),
                        ("TIFF files", "*.tiff*"))

    def __init__(self) -> None:
        """Initializes all buttons and labels, and places them on screen"""
        super().__init__()
        self.edited_img = None
        self.loaded_img = None

        self.label_file_explorer = Label(self, width=100, fg="blue", borderwidth=2, relief="groove")
        self.label_file_explorer.place(x=20, y=30, width=370)

        button_explore = Button(self, text="Browse Files", command=self.open_file)
        button_explore.place(x=400, y=25, width=80)

        save = Button(self, text="Save", command=self.save_file)
        save.place(x=400, y=100, width=80)

        resize = Button(self, text="Resize", command=self.edit)
        resize.place(x=20, y=100, width=80)

        loaded = Button(self, text="View Loaded", command=self.view_loaded)
        loaded.place(x=20, y=60, width=80)

        edited = Button(self, text="View Edited", command=self.view_edited)
        edited.place(x=400, y=60, width=80)

        self.x_input = Entry(self)
        self.y_input = Entry(self)
        self.x_input.place(x=160, y=100, width=60)
        self.y_input.place(x=280, y=100, width=60)

        x_input_label = Label(self, text="X Ratio")
        y_input_label = Label(self, text="Y Ratio")
        x_input_label.place(x=110, y=100, width=40)
        y_input_label.place(x=230, y=100, width=40)

        self.img_x = Label(self, text="Loaded X Size: ")
        self.img_x.place(x=120, y=52, width=100)
        self.img_y = Label(self, text="Loaded Y Size: ")
        self.img_y.place(x=260, y=52, width=100)

        self.resize_x = Label(self, text="Resized X Size: ")
        self.resize_x.place(x=120, y=74, width=100)
        self.resize_y = Label(self, text="Resized Y Size: ")
        self.resize_y.place(x=260, y=74, width=100)

    def open_file(self) -> None:
        """Opens selected file and sets the img_x and img_y to display the selected image's dimensions"""
        file_name = filedialog.askopenfilename(filetypes=self.valid_file_types)
        self.label_file_explorer.configure(text=file_name)
        self.loaded_img = Image.open(file_name)
        self.img_x.configure(text=f"Loaded X Size: {self.loaded_img.size[0]}")
        self.img_y.configure(text=f"Loaded Y Size: {self.loaded_img.size[1]}")
        self.edited_img = None

    def save_file(self) -> None:
        """Saves edited image if any, creates error popup if none"""
        if self.edited_img:
            file = filedialog.asksaveasfile(mode="w", filetypes=self.valid_file_types, defaultextension=".png")
            if file:
                self.edited_img.save(file.name)
        else:
            Popup("No Resized Image Found")

    def view_loaded(self):
        """Opens loaded image in default image viewer, if not possible, error popup displayed"""
        if self.loaded_img:
            self.loaded_img.show()
        else:
            Popup("No Image Loaded")

    def view_edited(self):
        """Opens edited image in default image viewer, if not possible, error popup displayed"""
        if self.edited_img:
            self.edited_img.show()
        else:
            Popup("No Resized Image Found")

    def edit(self) -> None:
        """Converts input ratios if possible and resizes loaded image using the ratio. Also updates image dimension
         information. If resize not possible error popup displayed"""
        def convert_to_number(value):
            try:
                return int(value)
            except ValueError:
                try:
                    return float(value)
                except ValueError:
                    return None

        x_value = convert_to_number(self.x_input.get())
        y_value = convert_to_number(self.y_input.get())
        if x_value and y_value and self.loaded_img:
            self.edited_img = self.loaded_img.resize((round(self.loaded_img.size[0]*x_value),
                                                     round(self.loaded_img.size[1]*y_value)))
            self.resize_x.configure(text=f"Resized X Size: {self.edited_img.size[0]}")
            self.resize_y.configure(text=f"Resized Y Size: {self.edited_img.size[1]}")
            Popup("Success")

        elif not self.loaded_img:
            Popup("No Image Loaded")
        else:
            Popup("Not A Valid Input, Only Numbers Allowed")


class Popup(Tk):
    """Popup for error and success messages"""
    def __init__(self, message) -> None:
        """creates popup with a message and button to close the window"""
        super().__init__()
        self.wm_title("!")
        label = Label(self, text=message)
        label.pack(side="top", fill="x", pady=10)
        close = Button(self, text="Okay", command=self.destroy)
        close.pack()
        self.minsize(width=100, height=80)
        self.resizable(0, 0)
        self.mainloop()


if __name__ == '__main__':
    window = Editor()
    window.title("Image Resizer")
    window.geometry("500x150")
    window.resizable(0, 0)
    window.mainloop()
