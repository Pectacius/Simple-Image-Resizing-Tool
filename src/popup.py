import tkinter as tk


class Popup(tk.Tk):
    """Popup for error and success messages"""

    def __init__(self, message) -> None:
        """creates popup with a message and button to close the window"""
        super().__init__()
        self.wm_title("!")
        label = tk.Label(self, text=message)
        label.pack(side="top", fill="x", pady=10)
        close = tk.Button(self, text="Okay", command=self.destroy)
        close.pack()
        self.minsize(width=100, height=80)
        self.resizable(0, 0)
        self.mainloop()