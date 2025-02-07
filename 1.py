import tkinter as tk
import math


def calculate_area():
    try:
        r = float(entry_radius.get())

        area = math.pi * (r ** 2)

        label_result.config(text=f"Площадь: {area:.3f}")
    except ValueError:
        label_result.config(text="Ошибка: введите число!")


root = tk.Tk()
root.title("Площадь круга")

label_prompt = tk.Label(root, text="Введите радиус:")
label_prompt.pack(pady=5)

entry_radius = tk.Entry(root)
entry_radius.pack(pady=5)

btn_calculate = tk.Button(root, text="Вычислить", command=calculate_area)
btn_calculate.pack(pady=5)

label_result = tk.Label(root, text="Площадь: -")
label_result.pack(pady=10)

root.mainloop()
