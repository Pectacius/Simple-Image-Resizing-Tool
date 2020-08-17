import tkinter as tk
from tkinter import filedialog

import image_editor as edit
import replace_frame as rpf
import resize_frame as rf
import tool_frame as tf


class EditorGUI(tk.Tk):
    """Editor for resizing images"""

    def __init__(self) -> None:
        """Initializes all buttons and labels, and places them on screen"""
        super().__init__()
        self.label_file_explorer = tk.Label(self, width=100, fg="blue", borderwidth=2, relief="groove")
        self.label_file_explorer.place(x=20, y=65, width=370)
        button_explore = tk.Button(self, text="Browse Files", command=self.open_file)
        button_explore.place(x=400, y=60, width=80)

        self.editor = edit.ImageEditor()
        self.tool_frame = tf.ToolBar(gui=self, master=self)
        self.resize_frame = rf.Resize(self.editor, master=self)
        self.color_replace_frame = rpf.ReplaceColor(gui=self, master=self)

    def open_file(self) -> None:
        """Opens selected file and sets the img_x and img_y to display the selected image's dimensions"""
        file_name = filedialog.askopenfilename(filetypes=self.editor.VALID_FILE_TYPES)
        self.label_file_explorer.configure(text=file_name)
        self.load_img(file_name)

    def load_img(self, file_name) -> None:
        """Loads file and updates file information"""
        self.editor.open_file(file_name)
        self.resize_frame.img_x.configure(text=f"Loaded X Size: {self.editor.loaded_img.size[0]}")
        self.resize_frame.img_y.configure(text=f"Loaded Y Size: {self.editor.loaded_img.size[1]}")
        self.resize_frame.resize_x.configure(text="Resized X Size: ")
        self.resize_frame.resize_y.configure(text="Resized Y Size: ")


if __name__ == '__main__':
    window = EditorGUI()
    window.title("Image Editor")
    window.geometry("500x450")
    window.resizable(0, 0)
    window.mainloop()
