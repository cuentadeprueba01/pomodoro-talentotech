from tkinter import Tk, Frame
from consts import YELLOW
from view import Analytics, Home


class Window(Tk):
    def __init__(self):
        super().__init__()

        self.title("Pomodoro App")
        self.geometry("450x420")
        self.config(bg=YELLOW)

        self.container = Frame(self)
        self.container.pack(fill="both", expand=True)

        # views
        self.frames = {}

        self.add_view(Home, "home")
        self.add_view(Analytics, "analytics")

        self.show_view("home")

    def show_view(self, name):
        # ocultar la vista actual
        for frame in self.frames.values():
            frame.pack_forget()

        # show new frame
        view = self.frames.get(name)

        if view:
            view.pack()

    def add_view(self, view, name):
        frame: Frame = view(self.container, self)

        self.frames[name] = frame
        frame.pack(fill="both", expand=True)
        frame.config(bg=YELLOW)
