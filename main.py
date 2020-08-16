from PIL import Image
from tkinter import Button, Entry, filedialog, Frame, Label, Scale, Tk


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

        tool_frame = Frame(self, highlightbackground="grey", highlightthickness=1)
        tool_frame.place(x=10, y=10, width=480, height=40)

        resize_frame = Frame(self, highlightbackground="grey", highlightthickness=1)
        resize_frame.place(x=10, y=100, width=480, height=100)

        color_replace_frame = Frame(self, highlightbackground="grey", highlightthickness=1)
        color_replace_frame.place(x=10, y=210, width=480, height=200)

        self.label_file_explorer = Label(self, width=100, fg="blue", borderwidth=2, relief="groove")
        self.label_file_explorer.place(x=20, y=65, width=370)

        button_explore = Button(self, text="Browse Files", command=self.open_file)
        button_explore.place(x=400, y=60, width=80)

        reload = Button(tool_frame, text="Reload", width=10, command=self.reload_file)
        reload.grid(row=0, column=3, padx=20, pady=5)

        save = Button(tool_frame, text="Save", width=10, command=self.save_file)
        save.grid(row=0, column=4, padx=20, pady=5)

        resize = Button(resize_frame, text="Resize", command=self.resize)
        resize.place(x=380, y=60, width=80)

        loaded = Button(tool_frame, text="View Loaded", width=10, command=self.view_loaded)
        loaded.grid(row=0, column=1, padx=20, pady=5)

        edited = Button(tool_frame, text="View Edited", width=10, command=self.view_edited)
        edited.grid(row=0, column=2, padx=20, pady=5)

        resize_label = Label(resize_frame, text="Resize Tool", borderwidth=2, relief="ridge")
        resize_label.place(x=0, y=0)

        self.x_input = Entry(resize_frame)
        self.y_input = Entry(resize_frame)
        self.x_input.place(x=380, y=10, width=80)
        self.y_input.place(x=380, y=35, width=80)

        x_input_label = Label(resize_frame, text="X Ratio")
        y_input_label = Label(resize_frame, text="Y Ratio")
        x_input_label.place(x=330, y=10, width=40)
        y_input_label.place(x=330, y=35, width=40)

        self.img_x = Label(resize_frame, text="Loaded X Size: ")
        self.img_x.place(x=10, y=30, width=100)
        self.img_y = Label(resize_frame, text="Loaded Y Size: ")
        self.img_y.place(x=10, y=60, width=100)

        self.resize_x = Label(resize_frame, text="Resized X Size: ")
        self.resize_x.place(x=150, y=30, width=100)
        self.resize_y = Label(resize_frame, text="Resized Y Size: ")
        self.resize_y.place(x=150, y=60, width=100)

        vcmd = (self.register(lambda p: str.isdigit(p) or p == ""))

        self.old_red = Entry(self, validate="all", validatecommand=(vcmd, '%P'))
        self.old_red.place(x=20, y=300, width=150)
        self.old_green = Entry(self, validate="all", validatecommand=(vcmd, '%P'))
        self.old_green.place(x=130, y=300)
        self.old_blue = Entry(self, validate="all", validatecommand=(vcmd, '%P'))
        self.old_blue.place(x=240, y=300)
        self.old_alpha = Entry(self, validate="all", validatecommand=(vcmd, '%P'))
        self.old_alpha.place(x=350, y=300)

        self.new_red = Scale
        self.new_green = Scale
        self.new_blue = Scale
        self.new_alpha = Scale

    def open_file(self) -> None:
        """Opens selected file and sets the img_x and img_y to display the selected image's dimensions"""
        file_name = filedialog.askopenfilename(filetypes=self.valid_file_types)
        self.label_file_explorer.configure(text=file_name)
        self.load_img(file_name)

    def reload_file(self) -> None:
        """Reloads uploaded file and removes edited file"""
        file_name = self.label_file_explorer.cget("text")
        self.load_img(file_name)

    def load_img(self, file_name) -> None:
        """Loads file and updates file information"""
        self.loaded_img = Image.open(file_name)
        self.img_x.configure(text=f"Loaded X Size: {self.loaded_img.size[0]}")
        self.img_y.configure(text=f"Loaded Y Size: {self.loaded_img.size[1]}")
        self.resize_x.configure(text="Resized X Size: ")
        self.resize_y.configure(text="Resized Y Size: ")
        self.edited_img = None

    def save_file(self) -> None:
        """Saves edited image if any, creates error popup if none"""
        if self.edited_img:
            file = filedialog.asksaveasfile(mode="w", filetypes=self.valid_file_types, defaultextension=".png")
            if file:
                self.edited_img.save(file.name, dpi=(300, 300))
        else:
            Popup("No Edited Image Found")

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
            Popup("No Edited Image Found")

    def resize(self) -> None:
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
        if x_value and y_value and self.loaded_img and not self.edited_img:
            self.edited_img = self.loaded_img.resize((round(self.loaded_img.size[0] * x_value),
                                                      round(self.loaded_img.size[1] * y_value)))
            self.update_resize_text()
            Popup("Success")
        elif x_value and y_value and self.loaded_img and self.edited_img:
            self.edited_img = self.edited_img.resize((round(self.edited_img.size[0] * x_value),
                                                      round(self.edited_img.size[1] * y_value)))
            self.update_resize_text()
            Popup("Success")

        elif not self.loaded_img:
            Popup("No Image Loaded")
        else:
            Popup("Not A Valid Input, Only Numbers Allowed")

    def update_resize_text(self) -> None:
        """Updates text in resized image boxes to new image dimensions"""
        self.resize_x.configure(text=f"Resized X Size: {self.edited_img.size[0]}")
        self.resize_y.configure(text=f"Resized Y Size: {self.edited_img.size[1]}")

    def validate_digit(self, p):
        return str.isdigit(p) or p == ""


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
    window.geometry("500x500")
    window.resizable(0, 0)
    window.mainloop()
