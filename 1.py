import tkinter as tk
from tkinter import simpledialog

def roundrect(canvas, x1, y1, x2, y2, radius=25, fill='', outline='black', text=''):

    canvas.create_rectangle(x1 + radius, y1, x2 - radius, y2, fill=fill, outline=outline)
    canvas.create_rectangle(x1, y1 + radius, x2, y2 - radius, fill=fill, outline=outline)

    canvas.create_arc(x1, y1, x1 + 2*radius, y1 + 2*radius, start=90, extent=90, style=tk.PIESLICE, fill=fill, outline=outline)
    canvas.create_arc(x2 - 2*radius, y1, x2, y1 + 2*radius, start=0, extent=90, style=tk.PIESLICE, fill=fill, outline=outline)
    canvas.create_arc(x2 - 2*radius, y2 - 2*radius, x2, y2, start=270, extent=90, style=tk.PIESLICE, fill=fill, outline=outline)
    canvas.create_arc(x1, y2 - 2*radius, x1 + 2*radius, y2, start=180, extent=90, style=tk.PIESLICE, fill=fill, outline=outline)

    if text:
        canvas.create_text((x1 + x2) // 2, (y1 + y2) // 2, text=text, fill='black')

root = tk.Tk()
root.withdraw()

x1 = simpledialog.askinteger("Input", "Enter x1 coordinate:", minvalue=0, maxvalue=400)
y1 = simpledialog.askinteger("Input", "Enter y1 coordinate:", minvalue=0, maxvalue=300)
x2 = simpledialog.askinteger("Input", "Enter x2 coordinate:", minvalue=0, maxvalue=400)
y2 = simpledialog.askinteger("Input", "Enter y2 coordinate:", minvalue=0, maxvalue=300)
radius = simpledialog.askinteger("Input", "Enter corner radius:", minvalue=0, maxvalue=100)
text = simpledialog.askstring("Input", "Enter text to display inside the rectangle:")

root.deiconify()

canvas = tk.Canvas(root, width=400, height=300)
canvas.pack()

roundrect(canvas, x1, y1, x2, y2, radius=radius, fill='lightyellow', outline='black', text=text)

root.mainloop()
