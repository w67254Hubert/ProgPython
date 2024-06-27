import tkinter as tk
from tkinter import messagebox

class MyApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Główne Okno")

        # Tworzenie przycisku w głównym oknie
        self.button = tk.Button(self.root, text="Otwórz nowe okno", command=self.open_new_window)
        self.button.pack(pady=20)

        # Etykieta do wyświetlania wyniku
        self.result_label = tk.Label(self.root, text="Wynik: ")
        self.result_label.pack(pady=20)

    def open_new_window(self):
        # Tworzenie nowego okna
        self.new_window = tk.Toplevel(self.root)
        self.new_window.title("Nowe Okno")

        # Przycisk "True"
        self.true_button = tk.Button(self.new_window, text="Tak", command=lambda: self.return_result(True))
        self.true_button.pack(side=tk.LEFT, padx=20, pady=20)

        # Przycisk "False"
        self.false_button = tk.Button(self.new_window, text="Nie", command=lambda: self.return_result(False))
        self.false_button.pack(side=tk.RIGHT, padx=20, pady=20)

    def return_result(self, result):
        # Wyświetlanie wyniku w etykiecie w głównym oknie
        self.result_label.config(text=f"Wynik: {result}")
        # Zamknięcie nowego okna
        self.new_window.destroy()

# Tworzenie głównego okna aplikacji
root = tk.Tk()
app = MyApp(root)
root.mainloop()
