import numpy as np
import tkinter as tk
import tkinter.messagebox

def hebbian_train(inputs, targets):
    weights = np.zeros((len(inputs[0]), len(targets[0])))
    for x, y in zip(inputs, targets):
        x = np.array(x).reshape(-1, 1)
        y = np.array(y).reshape(1, -1)
        weights += x @ y
    return weights

def predict(input_vector, weights):
    result = np.dot(input_vector, weights)
    return np.argmax(result)

train_states = [
    ([1, -1, 1, 0, -1, 0, 0, 0, 0], [1, 0]),  
    ([1, -1, 0, 1, -1, 0, 0, 0, 0], [1, 0]),
    ([1, -1, 1, -1, 1, -1, 0, 0, 0], [0, 1]),  
    ([1, -1, 0, 1, 0, 0, -1, 0, 0], [0, 1]),
]

train_moves = [
    ([1, -1, 1, 0, -1, 0, 0, 0, 0], [0, 0, 0, 1, 0, 1, 1, 1, 1]),
    ([1, 1, 0, -1, -1, 0, 0, 0, 0], [0, 0, 1, 0, 0, 1, 1, 1, 1]),
]

weights_turn = hebbian_train([s for s, _ in train_states], [t for _, t in train_states])
weights_move = hebbian_train([s for s, _ in train_moves], [t for _, t in train_moves])

board = [0]*9
current_symbol = 'X'

def check_winner(board):
    winning_combinations = [
        [0, 1, 2], [3, 4, 5], [6, 7, 8], 
        [0, 3, 6], [1, 4, 7], [2, 5, 8], 
        [0, 4, 8], [2, 4, 6]
    ]
    
    for combination in winning_combinations:
        if board[combination[0]] != 0 and board[combination[0]] == board[combination[1]] == board[combination[2]]:
            return board[combination[0]]  # 1 for X, -1 for O
    return 0  # No winner yet

def update_gui():
    for i in range(9):
        val = board[i]
        symbol = "X" if val == 1 else ("O" if val == -1 else "")
        buttons[i].config(text=symbol)
    
    turn_out = predict(board, weights_turn)
    move_out = predict(board, weights_move)
    
    turn_label.config(text=f"Predicted Turn: {'X' if turn_out == 0 else 'O'}")
    
    best_move = np.argmax(move_out)
    for i, btn in enumerate(buttons):
        if i == best_move and board[i] == 0:
            btn.config(bg="lightgreen")
        else:
            btn.config(bg="white")
    
    winner = check_winner(board)
    if winner != 0:  # A winner has been found
        winner_symbol = "X" if winner == 1 else "O"
        result = tk.messagebox.showinfo("Game Over", f"Player {winner_symbol} wins!")
        if result == 'ok':  # Reset the board after the user clicks "OK"
            reset_board()

def click_cell(i):
    global current_symbol
    if board[i] != 0:
        return
    board[i] = 1 if current_symbol == 'X' else -1
    current_symbol = 'O' if current_symbol == 'X' else 'X'
    update_gui()

def reset_board():
    global board, current_symbol
    board = [0]*9
    current_symbol = 'X'
    update_gui()

root = tk.Tk()
root.title("Hebbian TIC-TAC-TOE predictor")

buttons = []
for i in range(9):
    btn = tk.Button(root, text="", width=6, height=3, font=("Arial", 20), command=lambda i=i: click_cell(i))
    btn.grid(row=i//3, column=i%3)
    buttons.append(btn)

turn_label = tk.Label(root, text="Predicted Turn: ?", font=("Arial", 14))
turn_label.grid(row=3, column=0, columnspan=3)

reset_btn = tk.Button(root, text="Reset", command=reset_board)
reset_btn.grid(row=4, column=0, columnspan=3)

update_gui()
root.mainloop()
