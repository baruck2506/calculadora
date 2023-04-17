import tkinter as tk

def atualizar_visor(valor):
    visor.insert(tk.END, valor)

def calcular():
    try:

        expressao = visor.get(1.0, tk.END).strip()
        resultado = eval(expressao)

        visor.delete(1.0, tk.END)
        visor.insert(tk.END, resultado)

    except Exception as e:
        visor.delete(1.0, tk.END)
        visor.insert(tk.END, "Erro")

def limpar():
    visor.delete(1.0, tk.END)


janela = tk.Tk()

janela.title("Calculadora")

visor = tk.Text(janela, height=2, font=("Heveltica", 16))
visor.grid(row=0, column=0, columnspan=4)

botoes = [
    ("7", 1, 0), ("8", 1, 1), ("9", 1, 2), ("/", 1, 3),
    ("4", 2, 0), ("5", 2, 1), ("6", 2, 2), ("*", 2, 3),
    ("1", 3, 0), ("2", 3, 1), ("3", 3, 2), ("-", 3, 3),
    ("0", 4, 0), (".", 4, 1), ("+", 4,3)
]

for btn in botoes:
    text, row, col = btn
    tk.Button(
        janela,
        text=text,
        font=("Heveltica", 16),
        command=lambda
        t = text: atualizar_visor(t)

    ).grid(row=row, column=col)


tk.Button(
        janela,
        text="C",
        font=("Heveltica", 16),
        fg="red",
        command=limpar
    ).grid(
        row = 5,
        column= 0,
        columnspan=4
    )
tk.Button(
        janela,
        text="=",
        font=("Heveltica", 16),
        fg="red",
        command=calcular
    ).grid(
        row = 5,
        column= 2
    )

janela.mainloop()