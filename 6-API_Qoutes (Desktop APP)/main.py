import requests
from random import randint
from tkinter import *
import os 

API_END_POINT = "https://zenquotes.io/api/quotes" 
respnse = requests.get(url=API_END_POINT)
respnse.raise_for_status()
data=respnse.json()
base_dir = os.path.dirname(__file__) 


def get_quote():
    index = randint(0, len(data) - 1)
    quote = data[index]['q']    
    author = data[index]['a']
    quote_text_2=f"{quote}\n-{author}"
    
    canvas.itemconfig(quote_text,text=quote_text_2)
    
#-----------------------------------------------GUI_SetUP-----------------------------------------------#
window=Tk()
window.title("Yousef's Qoutes")
window.config(padx=50, pady=50)

canvas = Canvas(width=300, height=414)
background_img = PhotoImage(file=os.path.join(base_dir,'assets','background3.png'))
canvas.create_image(150, 207, image=background_img)
quote_text = canvas.create_text(150, 207, text="Click To Start Qoutes", width=250, font=("Georgia", 12, "bold"), fill="white")
canvas.grid(row=0, column=0,columnspan=2)

kanye_img = PhotoImage(file=os.path.join(base_dir,'assets','Yousef3.png'))
kanye_button = Button(image=kanye_img, highlightthickness=0, command=get_quote)
kanye_button.grid(row=1, column=0)

window.mainloop()





























