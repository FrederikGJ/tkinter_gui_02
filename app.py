from tkinter import *
from tkinter import filedialog

def save_file():
    file = filedialog.asksaveasfile(mode='w', defaultextension=".txt")
    if file is None:  
        return
    file_text = str(text.get(1.0, END))
    file.write(file_text)
    file.close()

def update_font_size():
    font_style = ("Terminal", font_size.get())
    text.configure(font=font_style)

def bigger_font_size():
    font_size.set(font_size.get() + 2)
    update_font_size()

def smaller_font_size():
    font_size.set(font_size.get() - 2)
    update_font_size()

window = Tk()
window.geometry("800x600")

font_size = IntVar()
font_size.set(16)

button_font_style = ("Terminal", 16)

save_button = Button(window, text="Gem", command=save_file, font=button_font_style)
save_button.pack()

make_font_smaller_button = Button(window, text="Gør tekst mindre", command=smaller_font_size, font=button_font_style)
make_font_smaller_button.pack()

make_font_bigger_button = Button(window, text="Gør tekst større", command=bigger_font_size, font=button_font_style)
make_font_bigger_button.pack()

text = Text(window, font=("Terminal", font_size.get()))
text.pack(fill=BOTH, expand=YES)

window.mainloop()
