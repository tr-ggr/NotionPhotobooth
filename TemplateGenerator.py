from PIL import Image
from tkinter import messagebox
import os
import time

result = None

def GeneratePhotobooth(pictures : list):
    global result
    template = Image.open("assets/photobooth_template.png")
    template_size = template.size

    # final_layer = Image.open("assets/photobooth_template_last_layer.png")

    try:
        for i in range(len(pictures)):
            pictures[i] = pictures[i].resize((1500,1000))
    except:
        messagebox.showerror("Error!", "please fill all the required pictures in the template")


    results = Image.new("RGB",(template_size[0], template_size[1]), (250,250,250))
                        
    results.paste(template, (0,0))
    results.paste(pictures[0], (156,1171))                    
    results.paste(pictures[1], (1705,117))
    results.paste(pictures[2], (1705,1171))
    # results.paste(final_layer, (0,0))

    results.show()

    result = results

def SaveResult():
    if not os.path.exists("outputs"):
        os.makedir("outputs")

    timestr = time.strftime("%Y%m%d-%H%M%S")
    result.save(f"outputs/{timestr}.png")