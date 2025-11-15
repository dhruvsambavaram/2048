import board_manager as b

def save_game(board: list[list[int]], file_name = "2048.txt"):
    with open(file_name, "w") as f:
        f.write(b.board_to_string(board))

def load_game(file_name = "2048.txt")-> list[list[int]]:
    #1 2 3 4\n5 6 7 8\n9 10 11 12\n13 14 15 16
    with open(file_name, "r") as f:
        board_str = f.read()
        rows = board_str.split("\n")
        board = [list(map(int, row.split(" "))) for row in rows]
        return board    