import tkinter as tk


class ColorFrame(tk.Frame):
    """Represents a frame that contains entry widgets to modify the color of the image"""

    def __init__(self, title: str, **kw) -> None:
        """Sets up entry widgets to adjust the color"""
        super().__init__(highlightbackground="grey", highlightthickness=1, width=170, height=180, **kw)

        validate = (self.register(lambda p: str.isdigit(p) or p == ""))

        tk.Label(self, text=title + " (RGBA)", borderwidth=2, relief="ridge").place(x=0, y=0)

        self.red = tk.Entry(self, validate="all", validatecommand=(validate, '%P'))
        self.red.place(x=60, y=40, width=80)
        tk.Label(self, text="RED").place(x=10, y=40)

        self.green = tk.Entry(self, validate="all", validatecommand=(validate, '%P'))
        self.green.place(x=60, y=70, width=80)
        tk.Label(self, text="GREEN").place(x=10, y=70)

        self.blue = tk.Entry(self, validate="all", validatecommand=(validate, '%P'))
        self.blue.place(x=60, y=100, width=80)
        tk.Label(self, text="BLUE").place(x=10, y=100)

        self.alpha = tk.Entry(self, validate="all", validatecommand=(validate, '%P'))
        self.alpha.place(x=60, y=130, width=80)
        tk.Label(self, text="ALPHA").place(x=10, y=130)
