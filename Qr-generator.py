from email.mime import image
from tkinter import *
from tkinter import messagebox
import qrcode
from PIL import Image, ImageTk

root = Tk()
root.title("Qr-Generator")
root.geometry("600x600")
user = StringVar()
Label(text="Enter text or URL", font="Tahoma 16", pady=10).pack()
entry = Entry(root, textvariable=user, font="Tahoma 14", width=30)
entry.pack(pady=10)


def gen():
    if len(user.get()) != 0:
        global img
        img = qrcode.make(user.get())
        img.save("qr.png")
        img = ImageTk.PhotoImage(Image.open("qr.png"))
        lbl.config(image=img)
    else:
        messagebox.showwarning("Warning", "fill the feild first!")


btn = Button(root, text="Generate", command=gen, padx=5, pady=5, font="Tahoma 14")
btn.pack()
lbl = Label(root, image=None)
lbl.pack(pady=20)
root.mainloop()
