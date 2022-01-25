from tkinter import *

users=["admin", "host"]
passwords=["admin", "host"]

def menuska(x,y,text,bcolor,fcolor,):
    menuska=Toplevel()
    menuska.grab_set()
    menuska.geometry("300x600")
    menuska.configure(bg="#141414")

    def on_enter(e):
        btn1["background"]=bcolor
        btn1["background"]=fcolor

    def on_leave(e):
        btn1["background"]=bcolor
        btn1["background"]=fcolor

    btn1=Button(menuska, width=42, height=2, text=text,
                fg=bcolor,
                bg=fcolor,
                border=0,
                activeforeground=fcolor,
                activebackground=bcolor)

    btn1.bind("<Enter>", on_enter)
    btn1.bind("<Leave>", on_leave)

    
    btn1.place(x=x,y=y)
    menuska.mainloop()

def btn_clicked():
    print("Button Clicked")


window = Tk()
 
window.geometry("1440x1024")
window.configure(bg = "#ffffff")
window.title("Zachetnaya Tihhonova")
canvas = Canvas(
    window,
    bg = "#ffffff",
    height = 1024,
    width = 1440,
    bd = 0,
    highlightthickness = 0,
    relief = "ridge")
canvas.place(x = 0, y = 0)

background_img = PhotoImage(file = f"background.png")
background = canvas.create_image(
    826.0, 441.5,
    image=background_img)

entry0_img = PhotoImage(file = f"img_textBox0.png")
entry0_bg = canvas.create_image(
    275.5, 135.0,
    image = entry0_img)

entry0 = Entry(
    bd = 0,
    bg = "#fffafa",
    highlightthickness = 0)

entry0.place(
    x = 99.0, y = 89,
    width = 353.0,
    height = 90)

entry1_img = PhotoImage(file = f"img_textBox1.png")
entry1_bg = canvas.create_image(
    275.5, 298.0,
    image = entry1_img)

entry1 = Entry(
    bd = 0,
    bg = "#fffafa",
    highlightthickness = 0)

entry1.place(
    x = 99.0, y = 252,
    width = 353.0,
    height = 90)

img0 = PhotoImage(file = f"img0.png")
b0 = Button(
    image = img0,
    borderwidth = 0,
    highlightthickness = 0,
    command = btn_clicked,
    relief = "flat")

b0.place(
    x = 189, y = 385,
    width = 174,
    height = 96)

b0.bind("<Button-1>",
           lambda e="Description": menuska(e))

menuska(0,0,"K ä ä r i d, K i v i, P a p e r", "#ffcc66", "#141414")
window.resizable(False, False)
window.mainloop()

