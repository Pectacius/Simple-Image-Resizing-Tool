import tkinter as tk
from tkinter import filedialog

import color_frame as cf
import image_editor as edit
import popup as pop
import resize_frame as rf


class EditorGUI(tk.Tk):
    """Editor for resizing images"""
    VALID_FILE_TYPES = (("Bitmap files", "*.bmp*"),
                        ("JPEG files", "*.jpg*"),
                        ("PNG files", "*.png*"),
                        ("SVG files", "*.svg*"),
                        ("TIFF files", "*.tiff*"))

    REPLACE_MODES = (("Match Exact", 1), ("Match Not", 2))

    def __init__(self) -> None:
        """Initializes all buttons and labels, and places them on screen"""
        super().__init__()
        self.editor = edit.ImageEditor()

        tool_frame = tk.Frame(self, highlightbackground="grey", highlightthickness=1)
        tool_frame.place(x=10, y=10, width=480, height=40)

        self.resize_frame = rf.Resize(self.editor)

        color_replace_frame = tk.Frame(self, highlightbackground="grey", highlightthickness=1)
        color_replace_frame.place(x=10, y=210, width=480, height=200)

        self.label_file_explorer = tk.Label(self, width=100, fg="blue", borderwidth=2, relief="groove")
        self.label_file_explorer.place(x=20, y=65, width=370)

        button_explore = tk.Button(self, text="Browse Files", command=self.open_file)
        button_explore.place(x=400, y=60, width=80)

        reload = tk.Button(tool_frame, text="Reload", width=10, command=self.reload_file)
        reload.grid(row=0, column=3, padx=20, pady=5)

        save = tk.Button(tool_frame, text="Save", width=10, command=self.save_file)
        save.grid(row=0, column=4, padx=20, pady=5)

        loaded = tk.Button(tool_frame, text="View Loaded", width=10, command=self.view_loaded)
        loaded.grid(row=0, column=1, padx=20, pady=5)

        edited = tk.Button(tool_frame, text="View Edited", width=10, command=self.view_edited)
        edited.grid(row=0, column=2, padx=20, pady=5)

        color_label = tk.Label(color_replace_frame, text="Replace Colors Tool", borderwidth=2, relief="ridge")
        color_label.place(x=0, y=0, width=110)

        self.mode = tk.IntVar()
        self.mode.set(1)

        mode_panel = tk.Frame(color_replace_frame, highlightbackground="grey", highlightthickness=1)
        mode_panel.place(x=5, y=30, width=100, height=120)

        match_description = tk.Label(mode_panel, text="Replace Modes")
        match_description.pack()

        for text, mode in self.REPLACE_MODES:
            b = tk.Radiobutton(mode_panel, text=text, variable=self.editor.mode, value=mode, justify=tk.LEFT)
            b.pack(anchor=tk.W)

        replace = tk.Button(color_replace_frame, text="Replace")
        replace.place(x=10, y=160, width=80)

        self.old_color = cf.ColorFrame("Color To Replace", master=color_replace_frame)
        self.old_color.place(x=120, y=10)

        self.new_color = cf.ColorFrame("Color To Replace With", master=color_replace_frame)
        self.new_color.place(x=300, y=10)

    def open_file(self) -> None:
        """Opens selected file and sets the img_x and img_y to display the selected image's dimensions"""
        file_name = filedialog.askopenfilename(filetypes=self.editor.VALID_FILE_TYPES)
        self.label_file_explorer.configure(text=file_name)
        self.load_img(file_name)

    def reload_file(self) -> None:
        """Reloads uploaded file and removes edited file"""
        file_name = self.label_file_explorer.cget("text")
        if file_name:
            self.load_img(file_name)
            pop.Popup("Success")
        else:
            pop.Popup("Nothing To Reload")

    def load_img(self, file_name) -> None:
        """Loads file and updates file information"""
        self.editor.open_file(file_name)
        self.resize_frame.img_x.configure(text=f"Loaded X Size: {self.editor.loaded_img.size[0]}")
        self.resize_frame.img_y.configure(text=f"Loaded Y Size: {self.editor.loaded_img.size[1]}")
        self.resize_frame.resize_x.configure(text="Resized X Size: ")
        self.resize_frame.resize_y.configure(text="Resized Y Size: ")

    def save_file(self) -> None:
        """Saves edited image if any, creates error popup if none"""
        if self.editor.edited_img:
            file = filedialog.asksaveasfile(mode="w", filetypes=self.editor.VALID_FILE_TYPES, defaultextension=".png")
            if file:
                self.editor.edited_img.save(file.name, dpi=(300, 300))
        else:
            pop.Popup("No Edited Image Found")

    def view_loaded(self):
        """Opens loaded image in default image viewer, if not possible, error popup displayed"""
        if self.editor.loaded_img:
            self.editor.loaded_img.show()
        else:
            pop.Popup("No Image Loaded")

    def view_edited(self):
        """Opens edited image in default image viewer, if not possible, error popup displayed"""
        if self.editor.edited_img:
            self.editor.edited_img.show()
        else:
            pop.Popup("No Edited Image Found")


if __name__ == '__main__':
    window = EditorGUI()
    window.title("Image Resizer")
    window.geometry("500x450")
    window.resizable(0, 0)
    window.mainloop()
