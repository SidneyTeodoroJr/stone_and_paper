import random
import tkinter as tk

# Definir as escolhas possíveis do jogo
CHOICES = ['pedra', 'papel', 'tesoura']

# Função para o botão de jogar
def play():
    # Escolher a jogada do computador
    computer_choice = random.choice(CHOICES)
    
    # Obter a escolha do jogador
    player_choice = player_var.get()
    
    # Determinar o resultado
    if player_choice == computer_choice:
        result_label.config(text="Empatou!")
    elif player_choice == 'pedra' and computer_choice == 'tesoura' or \
         player_choice == 'papel' and computer_choice == 'pedra' or \
         player_choice == 'tesoura' and computer_choice == 'papel':
        result_label.config(text="Parabéns, você venceu!")
    else:
        result_label.config(text="Que pena, você perdeu!")

# Criar a janela principal
root = tk.Tk()
root.title("Pedra, Papel, Tesoura")
root.geometry("500x600")
root.configure(bg="#e6e6e6")
root.resizable(width=False, height=False)

# Definir o ícone da janela
icon = tk.PhotoImage(file='icon.png')
root.iconphoto(True, icon)

# Criar as variáveis para a escolha do jogador
player_var = tk.StringVar()

# Criar os widgets
title_label = tk.Label(root, text="Escolha cuidadosamente uma jogada:", padx=45, pady=45, bg="#e6e6e6", font="Verdana 16")
rock_button = tk.Radiobutton(root, text="Pedra", variable=player_var, value="pedra", padx=45, pady=45, font="Arial 12", bg="#e6e6e6")
paper_button = tk.Radiobutton(root, text="Papel", variable=player_var, value="papel", padx=45, pady=45, font="Arial 12", bg="#e6e6e6")
scissors_button = tk.Radiobutton(root, text="Tesoura", variable=player_var, value="tesoura", padx=45, pady=45, font="Arial 12", bg="#e6e6e6")
play_button = tk.Button(root, text="Jogar", command=play)
result_label = tk.Label(root, padx=45, pady=45, text="", font="Verdana 12", bg="#e6e6e6")

# Colocar os widgets na janela
title_label.pack()
rock_button.pack()
paper_button.pack()
scissors_button.pack()
play_button.pack()
result_label.pack()

# Iniciar o loop de eventos
root.mainloop()
