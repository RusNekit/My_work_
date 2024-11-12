import tkinter as tk

window = tk.Tk()
window.title('Калькулятор')
window.geometry("350x350")
window.resizable(False, False)
button_add = tk.Button(window)
button_add.place(x=100, y=100)
window.mainloop()