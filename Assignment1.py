import tkinter as tk
from tkinter import messagebox
from forex_python.converter import CurrencyRates

c = CurrencyRates()

def convert_currency():
    amount = float(entry_amount.get())
    from_currency = entry_from_currency.get().upper()
    to_currency = entry_to_currency.get().upper()

    try:
        converted_amount = c.convert(from_currency, to_currency, amount)
        label_result.config(text=f"Converted Amount in {to_currency}: " + str(converted_amount))
    except Exception as e:
        messagebox.showerror("Error", str(e))

window = tk.Tk()
window.title("Currency Converter")
window.geometry("500x300")

label_amount = tk.Label(window, text="Amount:")
label_amount.pack()

entry_amount = tk.Entry(window)
entry_amount.pack()

label_from_currency = tk.Label(window, text="From Currency (e.g., USD):")
label_from_currency.pack()

entry_from_currency = tk.Entry(window)
entry_from_currency.pack()

label_to_currency = tk.Label(window, text="To Currency (e.g., INR):")
label_to_currency.pack()

entry_to_currency = tk.Entry(window)
entry_to_currency.pack()

convert_button = tk.Button(window, text="Convert", command=convert_currency)
convert_button.pack(pady=40)

label_result = tk.Label(window, text="Converted Amount:")
label_result.pack()

window.mainloop()