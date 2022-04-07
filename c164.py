from tkinter import *
from tkinter import filedialog
from PIL import ImageTk,Image

root=Tk()
root.title("image viewer")
root.geometry("400x400")
root.configure(background="black")

imagepath=""
def openimage():
    global imagepath
    imagepath=filedialog.askopenfilename(title="opentextfile",filetypes=[("Image Files","*.jpg *.gif *.png *.jpeg")])
    im=ImageTk.PhotoImage(Image.open(imagepath))
    label_image["image"]=im
    im.close()


btn_open=Button(root,text="open image",command=openimage)
btn_open.place(relx=0.5,rely=0.25,anchor=CENTER)

label_image=Label(root)
label_image.place(relx=0.5,rely=0.5,anchor=CENTER)

root.mainloop()

