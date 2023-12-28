from tkinter import *
import requests

window= Tk()
window.title("Kanye Quotes")

def kanye_quotes_generator():
    response= requests.get(url="https://api.kanye.rest")
    response.raise_for_status()
    data= response.json()
    quote= data["quote"]
    canvas.itemconfig(background_text, text= quote)

#canvas
canvas= Canvas(height=400, width=400)
pic= PhotoImage(file="./Day_33_API/background.png")
background_image= canvas.create_image(200, 200, image= pic)
background_text= canvas.create_text(200,200, text="Kanye quotes here...",width=250, font=("Ariel", 20, "italic"))
canvas.grid(row= 1, column= 1, columnspan=2)

#button
button_image= PhotoImage(file="./Day_33_API/kanye.png")
button= Button(image=button_image, highlightthickness=0, command= kanye_quotes_generator)
button.grid(row= 2, column= 1)

window.mainloop()
