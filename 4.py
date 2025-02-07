import tkinter as tk

def show_capital(event):
    selected_indices = listbox.curselection()
    if selected_indices:
        index = selected_indices[0]

        selected_country = listbox.get(index)

        capital = capital_map.get(selected_country, "Неизвестна")

        label_result.config(text=f"Столица: {capital}")

capital_map = {
    "Россия": "Москва",
    "США": "Вашингтон",
    "Великобритания": "Лондон",
    "Германия": "Берлин",
    "Франция": "Париж",
    "Испания": "Мадрид"
}

root = tk.Tk()
root.title("Столицы стран")

label_info = tk.Label(root, text="Выберите государство из списка:")
label_info.pack(pady=5)

listbox = tk.Listbox(root, height=6)
listbox.pack(pady=5)

for country in capital_map.keys():
    listbox.insert(tk.END, country)

listbox.bind("<<ListboxSelect>>", show_capital)

label_result = tk.Label(root, text="Столица: -")
label_result.pack(pady=5)
root.mainloop()
