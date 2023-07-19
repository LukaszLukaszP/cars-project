from tkinter import *
from tkinter import ttk


def calculate_excise():
    price = float(price_entry.get())
    engine_capacity = int(engine_capacity_entry.get())
    fuel_type = fuel_type_combobox.get()

    if fuel_type == "elektryczny":
        excise = 0
    elif fuel_type == "spalinowy":
        if engine_capacity <= 2000:
            excise = 0.031 * price
        else:
            excise = 0.186 * price
    elif fuel_type == "hybrydowy":
        if engine_capacity <= 2000:
            excise = 0.5 * 0.031 * price
        else:
            excise = 0.5 * 0.186 * price
    elif fuel_type == "hybrydowy plug-in":
        if engine_capacity <= 2000:
            excise = 0
        else:
            excise = 0.5 * 0.186 * price

    result_label.config(
        text=f"Kwota zakupu: {price}\nPojemność silnika: {engine_capacity}\nRodzaj paliwa: {fuel_type}\nAkcyza: {excise}")


root = Tk()
root.title("Kalkulator akcyzy")

Label(root, text="Kwota zakupu:").grid(row=0, column=0, sticky=W)
price_entry = Entry(root)
price_entry.grid(row=0, column=1, sticky=E)

Label(root, text="Pojemność silnika (cm^3):").grid(row=1, column=0, sticky=W)
engine_capacity_entry = Entry(root)
engine_capacity_entry.grid(row=1, column=1, sticky=E)

Label(root, text="Rodzaj paliwa:").grid(row=2, column=0, sticky=W)
fuel_type_combobox = ttk.Combobox(root, values=["spalinowy", "hybrydowy", "hybrydowy plug-in", "elektryczny"])
fuel_type_combobox.grid(row=2, column=1, sticky=E)

Button(root, text="Oblicz", command=calculate_excise).grid(row=3, column=0, columnspan=2)

result_label = Label(root, text="")
result_label.grid(row=4, column=0, columnspan=2)

root.mainloop()
