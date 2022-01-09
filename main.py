from tkinter import *

app = Tk()
app.title('Length Converter')
app.geometry('350x150 ')

scales = ['Meters', 'Inches', 'Foot']
_from = StringVar()
from_menu = OptionMenu(app, _from, *scales)
from_menu.grid(row=0, column=0, pady=5)

lbl = Label(app, text='convert to')
lbl.grid(row=0, column=1, pady=5)

to_ = StringVar()
to_menu = OptionMenu(app, to_, *scales)
to_menu.grid(row=0, column=2, pady=5)

enterL = Label(app, text='Enter your length ')
enterL.grid(row=1, column=0, columnspan=2, pady=5)

numE = Entry(app)
numE.grid(row=1, column=2, columnspan=2, pady=5)


def converter():
    From = _from.get()
    To = to_.get()
    Num = numE.get()

    if From == 'Meters' and To == 'Inches':
        conv_num = float(Num) * 39.37
    elif From == 'Meters' and To == 'Foot':
        conv_num = float(Num) * 3.28
    elif From == 'Inches' and To == 'Meters':
        conv_num = float(Num) / 39.37
    elif From == 'Foot' and To == 'Meters':
        conv_num = float(Num) / 3.28
    elif From == 'Inches' and To == 'Foot':
        conv_num = float(Num) / 12
    elif From == 'Foot' and To == 'Inches':
        conv_num = float(Num) * 12
    else:
        conv_num = Num
    numL = Label(app, text=round(conv_num, 2), width=10)
    numL.grid(row=1, column=4, pady=5)


conB = Button(app, text='Convert', command=converter)
conB.grid(row=2, column=0, pady=5)

app.mainloop()
