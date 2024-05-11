from tkinter import Frame, Label, Button


class Settings(Frame):
    def __init__(self, parent, controller):
        super().__init__(parent)

        self.controller = controller

        label = Label(self, text="Pomodoro settings", font=("Arial", 20))
        label.pack(pady=20)

        button = Button(
            self,
            text="Ir a home",
            command=lambda: controller.show_view("home"),
        )

        button.pack()
