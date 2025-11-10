# main.py
import tkinter as tk
import board as b
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

def key_pressed(event):
    # detect direction
    # call game_logic move function
    # update board view
    pass

if __name__ == "__main__":
    #main()
    root = tk.Tk()
    root.title("2048")

    board = b.init_board()

    frame = tk.Frame(root, bg = "#bbada0")
    frame.pack(padx = 20, pady = 20)
    for i in range(4):
        for j in range(4):
            labelA = tk.Label(frame, text = str(board[i][j]), borderwidth = 1, width = 10, height = 3, justify= tk.CENTER, bg = CELL_COLORS[0], font= CELL_NUMBER_FONT )
            labelA.grid(row = i, column = j, padx = 5, pady = 5)
    for i in range(4):
        frame.grid_rowconfigure(i, weight = 1)
        frame.grid_columnconfigure(i, weight = 1)


    root.mainloop()
