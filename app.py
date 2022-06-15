from tkinter import *
from PIL import ImageTk, Image
from word import get_words


class App(Tk):
    screen_width = 1000
    screen_height = 800
    canvas_color = '#acd8c0'
    white = '#fff'
    back_text_background = '#8fc2ae'
    language_font = ('Arial', 32, 'italic')
    word_font = ('Arial', 48, 'bold')
    words = get_words()

    def __init__(self):
        super().__init__()
        self.language = StringVar()
        self.word = StringVar()
        self.progress = 0

        self.title('Flashy')
        self.geometry(f'{self.screen_width}x{self.screen_height}')
        self.card_front = ImageTk.PhotoImage(Image.open('images/card_front.png'))
        self.card_back = ImageTk.PhotoImage(Image.open('images/card_back.png'))
        self.right_button = ImageTk.PhotoImage(Image.open('images/right.png'))
        self.wrong_button = ImageTk.PhotoImage(Image.open('images/wrong.png'))

        # CANVAS
        main_canvas = Canvas(master=self)
        main_canvas.configure(
            background=self.canvas_color,
            width=self.screen_width,
            height=self.screen_height
        )
        main_canvas.pack()

        # WRONG BUTTON
        wrong_button = Button(master=main_canvas)
        wrong_button.img = self.wrong_button
        wrong_button.configure(
            image=self.wrong_button,
            background=self.canvas_color,
        )
        wrong_button.place(x=250, y=600)

        # RIGHT BUTTON
        right_button = Button(master=main_canvas)
        right_button.img = self.right_button
        right_button.configure(
            image=self.right_button,
            background=self.canvas_color,
            command=self.flip_back
        )
        right_button.place(x=650, y=600)

        # FLASH CARD
        self.flash_card = Label(master=main_canvas)
        self.flash_card.place(relx=0.5, rely=0.45, anchor=CENTER)

        # LANGUAGE LABEL
        self.language_label = Label(master=main_canvas)
        self.language_label.configure(textvariable=self.language)
        self.language_label.place(relx=0.5, rely=0.3, anchor=CENTER)

        # WORD LABEL
        self.word_label = Label(master=main_canvas)
        self.word_label.configure(textvariable=self.word)
        self.word_label.place(relx=0.5, rely=0.42, anchor=CENTER)

        self.study()

    def flip_front(self):
        self.flash_card.img = self.card_front
        self.flash_card.configure(
            image=self.card_front,
            background=self.canvas_color
        )

        self.language.set('Italian')
        self.language_label.configure(
            background=self.white,
            font=self.language_font
        )

        self.word.set(self.words[self.progress].italian)
        self.word_label.configure(
            background=self.white,
            font=self.word_font
        )

    def flip_back(self):
        self.flash_card.img = self.card_back
        self.flash_card.configure(
            image=self.card_back,
            background=self.canvas_color
        )

        self.language.set('English')
        self.language_label.configure(
            background=self.back_text_background,
            foreground=self.white
        )

        self.word.set(self.words[self.progress].english)
        self.word_label.configure(
            background=self.back_text_background,
            foreground=self.white,
        )

    def study(self):
        self.flip_front()
        self.after(3000, self.flip_back)
