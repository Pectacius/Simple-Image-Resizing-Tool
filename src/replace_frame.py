import tkinter as tk

import color_frame as cf
import custom_errors
import popup as pop


class ReplaceColor(tk.Frame):
    """Frame to hold utilities to replace a color in an image"""

    def __init__(self, gui, **kw) -> None:
        super().__init__(highlightbackground="grey", highlightthickness=1, width=480, height=230, **kw)
        self.gui = gui

        tk.Label(self, text="Replace Colors Tool", borderwidth=2, relief="ridge").place(x=0, y=0, width=110)

        self.old_color = cf.ColorFrame("Color To Replace", master=self)
        self.old_color.place(x=120, y=10)

        self.new_color = cf.ColorFrame("Color To Replace With", master=self)
        self.new_color.place(x=300, y=10)

        mode_panel = tk.Frame(self, highlightbackground="grey", highlightthickness=1)
        mode_panel.place(x=5, y=30, width=100, height=160)

        match_description = tk.Label(mode_panel, text="Replace Modes")
        match_description.pack()

        for text, mode in self.gui.editor.REPLACE_MODES:
            b = tk.Radiobutton(mode_panel, text=text, variable=self.gui.editor.mode, value=mode, justify=tk.LEFT)
            b.pack(anchor=tk.W)

        replace = tk.Button(self, text="Replace", command=self.replace)
        replace.place(x=15, y=195, width=80)

        view_loaded_colors = tk.Button(self, text="View Loaded Image Colors", command=self.view_loaded_colors)
        view_loaded_colors.place(x=130, y=195, width=150)
        view_edited_colors = tk.Button(self, text="View Edited Image Colors", command=self.view_edited_colors)
        view_edited_colors.place(x=310, y=195, width=150)
        self.place(x=10, y=210)

    def replace(self) -> None:
        """Replaces the color (ro, go, bo, ao) with the color (rn, gn, bn, an)"""
        # colors to be replaced
        ro = self.old_color.red.get()
        go = self.old_color.green.get()
        bo = self.old_color.blue.get()
        ao = self.old_color.alpha.get()

        # colors to replace with
        rn = self.new_color.red.get()
        gn = self.new_color.green.get()
        bn = self.new_color.blue.get()
        an = self.new_color.alpha.get()

        try:
            self.gui.editor.replace_color(ro=ro, go=go, bo=bo, ao=ao, rn=rn, gn=gn, bn=bn, an=an)
        except custom_errors.InvalidRGBAError:
            pop.Popup("Invalid Input")
        except custom_errors.NoImageError:
            pop.Popup("No Image Found")
        else:
            pop.Popup("Success")

    def view_loaded_colors(self) -> None:
        """shows a display of all unique colors in the loaded image"""
        try:
            colors = self.gui.editor.unique_colors_loaded()
        except custom_errors.NoImageError:
            pop.Popup("No Image Found")
        else:
            Table(colors, "Unique Colors In Loaded Image")

    def view_edited_colors(self) -> None:
        """shows a display of all unique colors in the edited image"""
        try:
            colors = self.gui.editor.unique_colors_edited()
        except custom_errors.NoImageError:
            pop.Popup("No Image Found")
        else:
            Table(colors, "Unique Colors In Loaded Image")


class Table(tk.Tk):
    """Popup to show all the unique colors in an image in table format"""

    def __init__(self, values, title) -> None:
        super().__init__()
        self.wm_title(title)
        tk.Label(self, text="RGBA Value", width=25, borderwidth=1, relief="solid",
                 font='TkDefaultFont 8 bold').grid(row=0, column=0)
        tk.Label(self, text="Color", width=25, borderwidth=1, relief="solid",
                 font='TkDefaultFont 8 bold').grid(row=0, column=1)

        for index, value in enumerate(values):
            tk.Label(self, text=str(value), justify=tk.LEFT, width=25,
                     borderwidth=1, relief="solid").grid(row=index + 1, column=0)
            tk.Label(self, bg="#%02x%02x%02x" % value[:3], width=25,
                     borderwidth=1, relief="solid").grid(row=index + 1, column=1)

        self.resizable(0, 0)
        self.mainloop()
