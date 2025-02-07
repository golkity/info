import tkinter as tk
import random


def check_answer():
    user_choice = choice_var.get()

    is_even = (secret_number % 2 == 0)

    if (user_choice == 'even' and is_even) or (user_choice == 'odd' and not is_even):
        result_label.config(text="Правильно!")
    else:
        result_label.config(text=f"Неправильно! (Загаданное число: {secret_number})")


root = tk.Tk()
root.title("Игра «Чёт или нечёт»")

secret_number = random.randint(1, 100)

info_label = tk.Label(root, text="Компьютер загадал число от 1 до 100.\nВыберите, чётное оно или нечётное:")
info_label.pack(pady=10)

choice_var = tk.StringVar(value='even')

rb_even = tk.Radiobutton(root, text="Чёт", variable=choice_var, value='even')
rb_odd = tk.Radiobutton(root, text="Нечёт", variable=choice_var, value='odd')

rb_even.pack()
rb_odd.pack()

check_button = tk.Button(root, text="Проверить", command=check_answer)
check_button.pack(pady=10)

result_label = tk.Label(root, text="")
result_label.pack(pady=5)

root.mainloop()
