from tkinter import *

root = Tk()
root.title('Calculate feet to meters')

def calculate(*args):
    try:
        value = float(feets.get())
        m = int(0.3048 * value * 10000 + 0.5)/10000
        meters.set(m)
    except ValueError:
        meters.set('EROR')

frame = Frame(root, padx=12, pady=3)
frame.grid(column=0, row=0)

feets = StringVar()
feets_input = Entry(frame, width=7, textvariable=feets)
feets_input.grid(column=1, row=0)

meters = StringVar()
Label(frame, textvariable=meters).grid(column=1, row=1)

Button(frame, text='Calculate', command=calculate).grid(column=2, row=2)

Label(frame, text='Feets').grid(column=0, row=0)
Label(frame, text='Is equal to').grid(column=0, row=1)
Label(frame, text='meters').grid(column=2, row=1)

#This instruction give the input text the absolutely focus at the beggining
feets_input.focus()

#Bind nos permite escuchar eventos y dependiendo del evento que ocurra, ejecutar una función
root.bind("<Return>", calculate)
root.mainloop()