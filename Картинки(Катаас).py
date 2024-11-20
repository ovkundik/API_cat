from tkinter import*
import requests
from PIL import Image,ImageTk
from io import BytesIO

from pygame.examples.moveit import load_image


def load_img(url):
    response=requests.get(url)
   # print(response)
   # print(response.headers)
   # print(response.content) #Пришла картинка в закодированном виде
    image_data=BytesIO(response.content)
    print(image_data)
    img=Image.open(image_data)
    print(img)
    return ImageTk.PhotoImage(img)


window=Tk()
window.geometry("500x500")

label=Label()
label.pack()

url="https://cataas.com/cat"
img=load_img(url)

if img:
    label.config(image=img)
    #label.image=img

Knopka=Button(text="Загрузка картинки", command=load_image)

window.mainloop()
