import tkinter as tk

import color_frame as cf


class ReplaceColor(tk.Frame):
    """Frame to hold utilities to replace a color in an image"""

    def __init__(self, gui, **kw) -> None:
        super().__init__(highlightbackground="grey", highlightthickness=1, width=480, height=200, **kw)
        self.gui = gui

        tk.Label(self, text="Replace Colors Tool", borderwidth=2, relief="ridge").place(x=0, y=0, width=110)

        self.old_color = cf.ColorFrame("Color To Replace", master=self)
        self.old_color.place(x=120, y=10)

        self.new_color = cf.ColorFrame("Color To Replace With", master=self)
        self.new_color.place(x=300, y=10)

        mode_panel = tk.Frame(self, highlightbackground="grey", highlightthickness=1)
        mode_panel.place(x=5, y=30, width=100, height=120)

        match_description = tk.Label(mode_panel, text="Replace Modes")
        match_description.pack()

        for text, mode in self.gui.editor.REPLACE_MODES:
            b = tk.Radiobutton(mode_panel, text=text, variable=self.gui.editor.mode, value=mode, justify=tk.LEFT)
            b.pack(anchor=tk.W)

        replace = tk.Button(self, text="Replace", command=self.replace)
        replace.place(x=10, y=160, width=80)

        self.place(x=10, y=210)

    def replace(self) -> None:
        pass
