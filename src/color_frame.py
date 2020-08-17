import tkinter as tk


class ColorFrame(tk.Frame):
    """Represents a frame that contains entry widgets to modify the color of the image"""

    def __init__(self, title: str, **kw) -> None:
        """Sets up entry widgets to adjust the color"""
        super().__init__(highlightbackground="grey", highlightthickness=1, width=170, height=180, **kw)

        validate = (self.register(lambda p: str.isdigit(p) or p == ""))

        tk.Label(self, text=title + " (RGBA)", borderwidth=2, relief="ridge").place(x=0, y=0)

        self.red = tk.Entry(self, validate="all", validatecommand=(validate, '%P'))
        self.red.place(x=60, y=30, width=80)
        tk.Label(self, text="RED").place(x=10, y=30)

        self.green = tk.Entry(self, validate="all", validatecommand=(validate, '%P'))
        self.green.place(x=60, y=60, width=80)
        tk.Label(self, text="GREEN").place(x=10, y=60)

        self.blue = tk.Entry(self, validate="all", validatecommand=(validate, '%P'))
        self.blue.place(x=60, y=90, width=80)
        tk.Label(self, text="BLUE").place(x=10, y=90)

        self.alpha = tk.Entry(self, validate="all", validatecommand=(validate, '%P'))
        self.alpha.place(x=60, y=120, width=80)
        tk.Label(self, text="ALPHA").place(x=10, y=120)

        clear = tk.Button(self, text="Clear", command=self.clear)
        clear.place(x=60, y=145, width=80)

    def clear(self) -> None:
        """Clears all entries"""
        self.red.delete(0, 'end')
        self.green.delete(0, 'end')
        self.blue.delete(0, 'end')
        self.alpha.delete(0, 'end')