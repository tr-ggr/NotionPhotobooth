import tkinter as tk
from tkinter import filedialog
from PIL import Image, ImageTk
from TemplateGenerator import *

pictures = [None,None,None]

def open_image(number):
    file_path = filedialog.askopenfilename(title="Open Image File", filetypes=[("Image files", "*.png *.jpg *.jpeg *.gif *.bmp *.ico *.JPG")])
    if file_path:
        display_image(file_path, number)

def display_image(file_path, number):
    image = Image.open(file_path)
    image = image.resize((307,205))
    photo = ImageTk.PhotoImage(image)
    images[number].config(image=photo)
    images[number].photo = photo
    pictures[number] = image

def save_image():
    SaveResult()
    messagebox.showinfo("Saved!", "image saved!")

root = tk.Tk()
root.geometry('906x617')
root.resizable(False, False)

root.title("Photobooth GUI")

frame1 = tk.Frame(root)
frame2 = tk.Frame(root)

image1_label = tk.Label(frame1)
image2_label = tk.Label(frame1)
image3_label = tk.Label(frame1)

images = [image1_label, image2_label, image3_label]


image1_label.grid(row=1, column=0)
image2_label.grid(row=0, column=1)
image3_label.grid(row=1, column=1)

# text_widget = tk.Text(root, wrap=tk.WORD, height=15, width=35)

open_button1 = tk.Button(frame2, text="Open Image 1", command=lambda: open_image(0))
open_button1.pack(expand=True, fill=tk.X, side=tk.LEFT)

open_button2 = tk.Button(frame2, text="Open Image 2", command=lambda: open_image(1))
open_button2.pack(expand=True, fill=tk.X, side=tk.LEFT)

open_button3 = tk.Button(frame2, text="Open Image 3", command=lambda: open_image(2))
open_button3.pack(expand=True, fill=tk.X, side=tk.LEFT)


generate_button = tk.Button(frame2, text="Preview Template", command=lambda: GeneratePhotobooth(pictures=pictures))
generate_button.pack(expand=True, fill=tk.X, side=tk.LEFT)


save_button = tk.Button(frame2, text="Save Template", command=save_image)
save_button.pack(expand=True, fill=tk.X, side=tk.LEFT)


frame1.pack(expand=True, fill=tk.BOTH, side=tk.TOP, padx=20, pady=20)
frame2.pack(expand=True, fill=tk.BOTH, side=tk.BOTTOM)

root.mainloop()


