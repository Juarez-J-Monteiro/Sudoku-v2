import tkinter as tk

class interfaceJogo:
    def __init__(self, master):
        self.master = master
        self.celulas = []  # matriz 9x9 de widgets Entry

        frame = tk.Frame(master)
        frame.pack(padx=10, pady=10)

        for i in range(9):
            linha = []
            for j in range(9):
                e = tk.Entry(frame, width=2, justify="center",
                             font=("Arial", 18))
                # espaço extra entre os blocos 3x3
                padx = (0, 6) if j % 3 == 2 and j != 8 else (0, 0)
                pady = (0, 6) if i % 3 == 2 and i != 8 else (0, 0)
                e.grid(row=i, column=j, padx=padx, pady=pady)
                linha.append(e)
            self.celulas.append(linha)