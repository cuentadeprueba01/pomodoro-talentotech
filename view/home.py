from tkinter import Frame, Label


class Home(Frame):
    def __init__(self, parent: Frame, controller):
        super().__init__(parent)

        self.controller = controller

        label = Label(self, text="Pomodoro", font=("Arial", 20))
        label.pack(pady=20)

        # image_tomato = ImageTk.PhotoImage(file=Image.open("tomato.png"))

        # label_image = Label(image=image_tomato)
        # label_image.pack()
