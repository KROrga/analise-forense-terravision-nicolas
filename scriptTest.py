from tkinter import *
import customtkinter as ctk
from PIL import ImageTk, Image

current_image_number = 0

def change_image(n):
    global current_image_number, resized_tk
    current_image_number = n

    w = canvas.winfo_width()
    h = canvas.winfo_height()

    resized_image = pil_images[n].resize((w, h))
    resized_tk = ImageTk.PhotoImage(resized_image)

    update_canvas()

def fill_image(event):
    global resized_tk, current_image_number

    canvas_width = event.width
    canvas_height = event.height

    img = pil_images[current_image_number]
    img_ratio = img.width / img.height

    canvas_ratio = canvas_width / canvas_height

    if canvas_ratio > img_ratio:
        width = canvas_width
        height = int(width / img_ratio)
    else:
        height = canvas_height
        width = int(height * img_ratio)

    resized_image = img.resize((width, height))
    resized_tk = ImageTk.PhotoImage(resized_image)

    update_canvas()

root = Tk()
root.title("Test")
root.geometry('1400x700')
root.config(bg='grey')
root.columnconfigure((0,1,2,3,4), weight = 1, uniform = 'a')
root.rowconfigure(0, weight = 1,)

pil_image = Image.open("img/image.png")

image_files = ["img/image.png", "img/image2.png", "img/image3.png"]

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

def update_canvas():
    canvas.delete('all')
    canvas.create_image(
       canvas.winfo_width() // 2,
        canvas.winfo_height() // 2,
        anchor = 'center',
        image = resized_tk
    )

    canvas.image = resized_tk


def stretch_image(event):
    global resized_tk

    width = event.width
    height = event.height

    resized_image = image_stretch.resize((width,height))
    resized_tk = ImageTk.PhotoImage(resized_image)

    update_canvas(resized_tk)

button_frame = Frame(root)
button_frame.columnconfigure(0, weight = 1, uniform = 'a')

# bg_canvas = Canvas(button_frame)
# bg_canvas.place(relx=0, rely=0, relwidth=1, relheight=1)

image = Image.open("img/button_bg.png")
bg_image = ImageTk.PhotoImage(image)
bg_label = Label(button_frame, image=bg_image)
bg_label.place(relx=0, rely=0, relwidth=1, relheight=1, anchor='nw')
# bg_canvas.create_image(0,0, anchor ='nw', image=bg_image)

button10000 = Button(button_frame, padx=1, text="10000m", command=lambda: change_image(0))
button7500 = Button(button_frame, padx=1, text="7500m")
button5000 = Button(button_frame, padx=1, text="5000m", command=lambda: change_image(1))
button2500 = Button(button_frame, padx=1, text="2500m")
button1000 = Button(button_frame, padx=1, text="1000m", command=lambda: change_image(2))


button10000.grid(row=0, column=0, pady=10, padx=10, sticky='nsew')
button7500.grid(row=1, column=0, pady=10, padx=10, sticky='nsew')
button5000.grid(row=2, column=0, pady=10, padx=10, sticky='nsew')
button2500.grid(row=3, column=0, pady=10, padx=10, sticky='nsew')
button1000.grid(row=4, column=0, pady=10, padx=10, sticky='nsew')

button_frame.grid(column = 4, row =0, sticky = 'nsew')

canvas = Canvas(root, bg='grey', bd= 0, highlightthickness= 0, relief= 'ridge')
canvas.grid(column = 0, columnspan = 4, row= 0, sticky ='nsew')

# bg_label.bind('<Configure>', fill_image)
canvas.bind('<Configure>', fill_image)


root.mainloop()

