import tkinter as tk
from tkinter import ttk
from tkinter import messagebox

class InvalidProductException(Exception):
    pass

# Função para calcular o total da fatura com desconto
def calculateInvoice(products, discount):
    total = 0
    for product in products:
        if product["price"] < 0 or product["quantity"] < 0:
            raise InvalidProductException("Preço ou quantidade inválidos.")
        total += product["price"] * product["quantity"]

    total -= total * (discount / 100)

    # Desconto adicional se o total for maior que R$ 1000
    if total > 1000:
        total -= 100  # Desconto adicional

    return total

# Função para adicionar um produto à lista
def add_product():
    try:
        name = entry_name.get()
        price = float(entry_price.get())
        quantity = int(entry_quantity.get())

        if price < 0 or quantity < 0:
            raise ValueError("Preço e quantidade devem ser positivos.")

        products.append({"name": name, "price": price, "quantity": quantity})

        # Atualiza a lista na interface
        listbox_products.insert(tk.END, f"{name} - R${price:.2f} x {quantity}")

        # Limpa os campos de entrada
        entry_name.delete(0, tk.END)
        entry_price.delete(0, tk.END)
        entry_quantity.delete(0, tk.END)

    except ValueError as ve:
        messagebox.showerror("Erro", str(ve))

# Função para limpar a lista de produtos
def clear_list():
    products.clear()
    listbox_products.delete(0, tk.END)
    label_result.config(text="Total da fatura: R$ 0,00")

# Função para calcular a fatura e exibir o total
def calculate():
    try:
        # Obtém o valor de desconto
        discount = float(entry_discount.get())

        # Verifica se há produtos na lista
        if not products:
            messagebox.showwarning("Aviso", "Adicione produtos antes de calcular a fatura.")
            return

        # Calcula o total
        total = calculateInvoice(products, discount)

        # Atualiza a label com o total calculado
        label_result.config(text=f"Total da fatura: R$ {total:.2f}")

    except InvalidProductException as ip:
        messagebox.showerror("Erro", str(ip))
    except ValueError:
        messagebox.showerror("Erro", "Desconto inválido.")

# Configuração da interface gráfica
root = tk.Tk()
root.title("Calculadora de Fatura")
root.geometry("500x600")  # Tamanho da janela
root.resizable(False, False)  # Impede o redimensionamento

# Lista para armazenar os produtos
products = []

# Estilo de widgets com ttk
style = ttk.Style()
style.configure("TLabel", font=("Arial", 12), background="#f7f7f7")
style.configure("TButton", font=("Arial", 10), padding=10, background="#4CAF50", foreground="white", width=20)
style.map("TButton", background=[("active", "#45a049")])
style.configure("TEntry", font=("Arial", 12), padding=10, relief="flat", background="#f0f0f0")

# Layout com grid
frame = ttk.Frame(root, padding="20")
frame.grid(row=0, column=0, padx=20, pady=20)

# Widgets para entrada de produto
label_name = ttk.Label(frame, text="Nome do Produto:")
label_name.grid(row=0, column=0, sticky="w", pady=5)

entry_name = ttk.Entry(frame, width=30)
entry_name.grid(row=0, column=1, pady=5)

label_price = ttk.Label(frame, text="Preço do Produto (R$):")
label_price.grid(row=1, column=0, sticky="w", pady=5)

entry_price = ttk.Entry(frame, width=30)
entry_price.grid(row=1, column=1, pady=5)

label_quantity = ttk.Label(frame, text="Quantidade:")
label_quantity.grid(row=2, column=0, sticky="w", pady=5)

entry_quantity = ttk.Entry(frame, width=30)
entry_quantity.grid(row=2, column=1, pady=5)

# Botão para adicionar produto
button_add_product = ttk.Button(frame, text="Adicionar Produto", command=add_product)
button_add_product.grid(row=3, column=0, columnspan=2, pady=10)

# Lista de produtos
listbox_products = tk.Listbox(frame, height=6, width=40, font=("Arial", 10))
listbox_products.grid(row=4, column=0, columnspan=2, pady=10)

# Botão para limpar a lista de produtos
button_clear_list = ttk.Button(frame, text="Limpar Lista", command=clear_list)
button_clear_list.grid(row=5, column=0, columnspan=2, pady=5)

# Entrada do desconto
label_discount = ttk.Label(frame, text="Desconto (%):")
label_discount.grid(row=6, column=0, sticky="w", pady=5)

entry_discount = ttk.Entry(frame, width=30)
entry_discount.grid(row=6, column=1, pady=5)

# Botão para calcular fatura
button_calculate = ttk.Button(frame, text="Calcular Fatura", command=calculate)
button_calculate.grid(row=7, column=0, columnspan=2, pady=10)

# Label para exibir o resultado
label_result = ttk.Label(frame, text="Total da fatura: R$ 0,00", font=("Arial", 14), foreground="black")
label_result.grid(row=8, column=0, columnspan=2, pady=20)

# Iniciar o loop da interface gráfica
root.mainloop()