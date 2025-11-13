# main.py
import tkinter as tk
import board_manager as b
import game_logic as g


LABELS = []
GAME_STATE = "CONTINUE"
commands = {
            'Up'   : g.move, 
            'Down' : g.move,
            'Left' : g.move,
            'Right': g.move
        }
CELL_COLORS = {
    0: "#cdc1b4",
    2: "#eee4da",
    4: "#ede0c8",
    8: "#f2b179",
    16: "#f59563",
    32: "#f67c5f",
    64: "#f65e3b",
    128: "#edcf72",
    256: "#edcc61",
    512: "#edc850",
    1024: "#edc53f",
    2048: "#edc22e"
}
CELL_NUMBER_COLORS = {2: "#776e65", 4: "#776e65"}
CELL_NUMBER_FONT = ("Verdana", 24, "bold")

def game_over_screen():
        print(GAME_STATE)
        over = tk.Toplevel(root)
        over.title("Game Over 😭")
        tk.Label(over, text="Game Over!", font=("Verdana", 20, "bold")).pack(pady=20)

def game_won_screen():
        over = tk.Toplevel(root)
        over.title("Game won !!!")
        tk.Label(over, text="Game won!", font=("Verdana", 20, "bold")).pack(pady=20)

def display_board(board):
    num_rows = len(board)
    num_cols = len(board[0])
    for i in range(num_rows):
        for j in range(num_cols):
            LABELS[4*i + j].config(text = str(board[i][j]))
             

def key_pressed(event):
    # detect direction
    # call game_logic move function
    # update board view
    global GAME_STATE
    if GAME_STATE == "CONTINUE":
        try:     
            key = event.keysym
            if key in commands.keys():
                
                # operation
                commands[key](board, key)
                
                # feasability
                GAME_STATE = g.check_game_state(board)
                
                if GAME_STATE == "CONTINUE":
                    b.spawn_random_tile(board)
                    print(g.check_game_state(board))
                
                elif GAME_STATE == "WON":
                    game_won_screen()
                
                display_board(board)

        
        except ValueError:
            if GAME_STATE == "LOST":
                game_over_screen()
         

if __name__ == "__main__":
    #main()
    root = tk.Tk()
    root.bind("<Key>", key_pressed)
    root.title("2048")

    board = b.init_board()

    frame = tk.Frame(root, bg = "#bbada0")
    frame.pack(padx = 20, pady = 20)
    for i in range(4):
        for j in range(4):
            labelA = tk.Label(frame, text = str(board[i][j]), borderwidth = 1, width = 10, height = 3, justify= tk.CENTER, bg = CELL_COLORS[0], font= CELL_NUMBER_FONT )
            labelA.grid(row = i, column = j, padx = 5, pady = 5)
            LABELS.append(labelA)
    for i in range(4):
        frame.grid_rowconfigure(i, weight = 1)
        frame.grid_columnconfigure(i, weight = 1)


    root.mainloop()
