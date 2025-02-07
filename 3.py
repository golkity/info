import tkinter as tk
import random


def roll_player1():
    global roll1
    roll1 = random.randint(1, 6)
    label_roll1.config(text=f"Выпало: {roll1}")


def roll_player2():
    global roll2
    roll2 = random.randint(1, 6)
    label_roll2.config(text=f"Выпало: {roll2}")


def determine_winner():
    if roll1 == 0 or roll2 == 0:
        result_label.config(text="Сначала оба игрока должны бросить кубик!")
        return

    if roll1 > roll2:
        result_label.config(text="Победил первый игрок!")
    elif roll2 > roll1:
        result_label.config(text="Победил второй игрок!")
    else:
        result_label.config(text="Ничья!")


roll1 = 0
roll2 = 0

root = tk.Tk()
root.title("Игра «Кубик» для двух игроков")

button_p1 = tk.Button(root, text="Бросает 1-й игрок", command=roll_player1)
button_p1.grid(row=0, column=0, padx=10, pady=10)

label_roll1 = tk.Label(root, text="Выпало: -")
label_roll1.grid(row=0, column=1, padx=10, pady=10)

button_p2 = tk.Button(root, text="Бросает 2-й игрок", command=roll_player2)
button_p2.grid(row=1, column=0, padx=10, pady=10)

label_roll2 = tk.Label(root, text="Выпало: -")
label_roll2.grid(row=1, column=1, padx=10, pady=10)

result_button = tk.Button(root, text="Определить результат игры", command=determine_winner)
result_button.grid(row=2, column=0, columnspan=2, pady=10)

result_label = tk.Label(root, text="")
result_label.grid(row=3, column=0, columnspan=2, pady=10)

root.mainloop()
