from tkinter import *
import customtkinter as ctk
from PIL import ImageTk, Image, ImageSequence
import os

### *** /// *** /// *** /// *** /// ###

splash_window = Tk()
splash_window.title("Inicializando")
splash_window.overrideredirect(True)
window_width = 400
window_height = 300

screen_width = splash_window.winfo_screenwidth()
screen_height = splash_window.winfo_screenheight()

x = int((screen_width / 2) - (window_width / 2))
y = int((screen_height / 2) - (window_height / 2))

def play_gif():
    global frame_index
    frame_index = (frame_index + 1) % frame_count
    label.config(image=frames[frame_index])
    splash_window.after(delay_times[frame_index], play_gif)

gif_path = "img/car_gif.gif"

if not os.path.exists(gif_path):
    raise FileNotFoundError(f"GIF file not found: {gif_path}")

gif = Image.open(gif_path)

frames = []
delay_times = []
for frame in ImageSequence.Iterator(gif):
    frames.append(ImageTk.PhotoImage(frame.copy()))
    delay_times.append(frame.info.get('duration', 100))

frame_count = len(frames)
frame_index = 0

splash_window.geometry(f"{window_width}x{window_height}+{x}+{y}")

label = Label(splash_window, image=frames[0])
label.pack()

splash_window.after(delay_times[0], play_gif())

class Main:
    def __init__(self,splash_window):
        self.splash_window = splash_window
        self.current_image_number = 5
        self.resized_tk = None
        image_files = ["img/10000.jpeg", "img/7500.jpeg", "img/5000.jpeg", "img/2500.jpeg", "img/1000.jpeg", "img/aviso.png"]
        self.pil_images = [Image.open(f) for f in image_files]

        # self.main_window()


    # current_image_number = 0
    def change_image(self, n):
        # global current_image_number, resized_tk
        self.current_image_number = n

        w = self.canvas.winfo_width()
        h = self.canvas.winfo_height()

        resized_image = self.pil_images[n].resize((w, h))
        self.resized_tk = ImageTk.PhotoImage(resized_image)

        self.update_canvas()

    def update_canvas(self):
        self.canvas.delete('all')
        self.canvas.create_image(
            self.canvas.winfo_width() // 2,
            self.canvas.winfo_height() // 2,
            anchor = 'center',
            image = self.resized_tk
        )
        self.canvas.image = self.resized_tk


    def fill_image(self, event):
        # global resized_tk, current_image_number

        canvas_width = event.width
        canvas_height = event.height

        img = self.pil_images[self.current_image_number]
        img_ratio = img.width / img.height

        canvas_ratio = canvas_width / canvas_height

        if canvas_ratio > img_ratio:
            width = canvas_width
            height = int(width / img_ratio)
        else:
            height = canvas_height
            width = int(height * img_ratio)

        resized_image = img.resize((width, height))
        self.resized_tk = ImageTk.PhotoImage(resized_image)

        self.update_canvas()

    def main_window(self):
        self.splash_window.destroy()
        self.root = Tk()
        self.root.title("Test")
        self.root.geometry('1500x720')
        self.root.config(bg='grey')
        self.root.columnconfigure((0,1,2,3,4), weight = 1, uniform = 'a')

        self.root.rowconfigure(0, weight = 1,)

        self.screen_width = self.root.winfo_screenwidth()
        self.screen_height = self.root.winfo_screenheight()

        x = int((self.screen_width / 2) - (window_width / 2))
        y = int((self.screen_height / 2) - (window_height / 2))

        pil_image = Image.open("img/aviso.png")

        image_files = ["img/10000.jpeg", "img/7500.jpeg", "img/5000.jpeg", "img/2500.jpeg", "img/1000.jpeg"]
        pil_images = []

        tk_images = []

        image_list = []

        for file in image_files:
            pil_img = Image.open(file)
            pil_images.append(pil_img)
            tk_images.append(ImageTk.PhotoImage(pil_img))

            image_list.append((tk_images))
        image_stretch = image_list[0]

        resized_tk = None

        image_ratio = pil_image.size[0] / pil_image.size[1]


        def stretch_image(event):
            global resized_tk

            width = event.width
            height = event.height

            resized_image = image_stretch.resize((width,height))
            resized_tk = ImageTk.PhotoImage(resized_image)

            self.update_canvas(resized_tk)

        button_frame = Frame(self.root)
        button_frame.columnconfigure(0, weight = 1, uniform = 'a')

        # bg_canvas = Canvas(button_frame)
        # bg_canvas.place(relx=0, rely=0, relwidth=1, relheight=1)

        image = Image.open("img/button_bg.png")
        bg_image = ImageTk.PhotoImage(image)
        bg_label = Label(button_frame, image=bg_image)
        bg_label.place(relx=0, rely=0, relwidth=1, relheight=1, anchor='nw')
        # bg_canvas.create_image(0,0, anchor ='nw', image=bg_image)

        button10000 = Button(button_frame, padx=1, text="10000m", command=lambda: self.change_image(0))
        button7500 = Button(button_frame, padx=1, text="7500m", command=lambda: self.change_image(1))
        button5000 = Button(button_frame, padx=1, text="5000m", command=lambda: self.change_image(2))
        button2500 = Button(button_frame, padx=1, text="2500m", command=lambda: self.change_image(3))
        button1000 = Button(button_frame, padx=1, text="1000m", command=lambda: self.change_image(4))
        buttonEnd = Button(button_frame, padx=1, text="Encerrar", bg='red', command=self.root.quit)

        button10000.grid(row=0, column=0, pady=10, padx=10, sticky='nsew')
        button7500.grid(row=1, column=0, pady=10, padx=10, sticky='nsew')
        button5000.grid(row=2, column=0, pady=10, padx=10, sticky='nsew')
        button2500.grid(row=3, column=0, pady=10, padx=10, sticky='nsew')
        button1000.grid(row=4, column=0, pady=10, padx=10, sticky='nsew')
        buttonEnd.grid(row=5, column=0, pady=10, padx=10, sticky='nsew')

        button_frame.grid(column = 4, row =0, sticky = 'nsew')

        self.canvas = Canvas(self.root, bg='grey', bd= 0, highlightthickness= 0, relief= 'ridge')
        self.canvas.grid(column = 0, columnspan = 4, row= 0, sticky ='nsew')

        # bg_label.bind('<Configure>', fill_image)
        self.canvas.bind('<Configure>', self.fill_image)

main = Main(splash_window)
splash_window.after(3000, main.main_window)

mainloop()

