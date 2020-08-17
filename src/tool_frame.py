import tkinter as tk
from tkinter import filedialog

import popup as pop


class ToolBar(tk.Frame):
    """Holds buttons to view and save images"""
    def __init__(self, gui, **kw):
        super().__init__(highlightbackground="grey", highlightthickness=1, **kw)
        self.gui = gui

        reload = tk.Button(self, text="Reload", width=10, command=self.reload_file)
        reload.grid(row=0, column=3, padx=20, pady=5)

        save = tk.Button(self, text="Save", width=10, command=self.save_file)
        save.grid(row=0, column=4, padx=20, pady=5)

        loaded = tk.Button(self, text="View Loaded", width=10, command=self.view_loaded)
        loaded.grid(row=0, column=1, padx=20, pady=5)

        edited = tk.Button(self, text="View Edited", width=10, command=self.view_edited)
        edited.grid(row=0, column=2, padx=20, pady=5)

        self.place(x=10, y=10, width=480, height=40)

    def reload_file(self) -> None:
        """Reloads uploaded file and removes edited file"""
        file_name = self.gui.label_file_explorer.cget("text")
        if file_name:
            self.gui.load_img(file_name)
            pop.Popup("Success")
        else:
            pop.Popup("Nothing To Reload")

    def save_file(self) -> None:
        """Saves edited image if any, creates error popup if none"""
        if self.gui.editor.edited_img:
            file = filedialog.asksaveasfile(mode="w", filetypes=self.gui.editor.VALID_FILE_TYPES,
                                            defaultextension=".png")
            if file:
                self.gui.editor.edited_img.save(file.name, dpi=(300, 300))
        else:
            pop.Popup("No Edited Image Found")

    def view_loaded(self) -> None:
        """Opens loaded image in default image viewer, if not possible, error popup displayed"""
        if self.gui.editor.loaded_img:
            self.gui.editor.loaded_img.show()
        else:
            pop.Popup("No Image Loaded")

    def view_edited(self) -> None:
        """Opens edited image in default image viewer, if not possible, error popup displayed"""
        if self.gui.editor.edited_img:
            self.gui.editor.edited_img.show()
        else:
            pop.Popup("No Edited Image Found")
