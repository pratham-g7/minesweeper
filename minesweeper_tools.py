from random import choice
import animation_handler as ani
from data_handler import load_data
from pathlib import Path


finished = []
options = {"1": "Easy", "2": "Medium", "3": "Hard", "4": "⚠???⚠"}
difficulty = {"1": "3x3", "2": "5x5", "3": "7x7", "4": "9x9"}
intro = "Welcome to MineSweeper!"
begin = "You have picked {} mode. Good Luck."

code = None
saved = False
save_location = Path.home() / "Documents" / "minesweeper_saves" / "minesweeper.dat"
save_location.parent.mkdir(parents=True, exist_ok=True)
save_location.touch(exist_ok=True)

def valid_pos(pos, dim):
    if int(pos[0]) <= int(dim[0]) and int(pos[1]) <= int(dim[1]) and int(pos[0]) > 0 and int(pos[1]) > 0:
        return True
    return False

def apply_point_check(board: list, dim: list):
    new_board = [["" for j in range(dim[0])] for i in range(dim[1])]
    for i in range(dim[1]):
        for j in range(dim[0]):
            if board[i][j] != "💣":
                count = 0
                for x in range(-1, 2):
                    for y in range(-1, 2):
                        if 0 <= i + x < dim[0] and 0 <= j + y < dim[1]:
                            if board[i + x][j + y] == "💣":
                                count += 1
                new_board[i][j] = f"{count} "
            else:
                new_board[i][j] = "💣"
    return new_board
    

def create_board(dimensions: list = [3, 3], ignore: list = [], std=False):
    x, y = int(dimensions[0]), int(dimensions[1])
    GRID = [["📦" for j in range(y)] for i in range(x)]
    if std:
        return GRID, []
    ANS_GRID = [[choice(["💣", "$ ", "$ ", "$ ", "$ "]) for j in range(y)] for i in range(x)]
    if ignore:
        ANS_GRID[int(ignore[0])-1][int(ignore[1])-1] = "$ "
    
    return GRID, apply_point_check(ANS_GRID, dimensions)


def display(g: list, dim: list):
    _rows = ""
    for i in range(len(g)):
        _row = str(i + 1) + "| " + " ".join(g[i]) + " |"
        _rows += _row + "\n"
    numbering = "    " + "  ".join([str(i + 1) for i in range(dim[0])]) + "   \n"
    head = "=| " + ("=" * (((dim[0] * 3) - 1))) + " |=\n"
    tail = "=| " + ("=" * (((dim[0] * 3) - 1))) + " |="
    _board = numbering + head + _rows + tail
    print(_board)


def get_bomb_pos(answer_key: list):
    bomb_pos = []
    for i in range(len(answer_key)):
        for j in range(len(answer_key[i])):
            if answer_key[i][j] == "💣":
                bomb_pos.append([i, j])
    return bomb_pos


def get_pts(board: list):
    nums = []
    for i in board:
        for j in i:
            if j not in ["💣", "📦"]:
                nums.append(j)
    return sum([int(i.strip()) for i in nums])


def flood_fill(board, ans, loc: list, dim: list):
    if loc not in finished:
        finished.append(loc)
        value = ans[loc[0]][loc[1]]
        board[loc[0]][loc[1]] = value
        if value == "0 ":
            for dx in range(-1, 2):
                for dy in range(-1, 2):
                    if dx == 0 and dy == 0:
                        continue
                    new_loc = [loc[0] + dx, loc[1] + dy]

                    if 0 <= new_loc[0] < dim[0] and 0 <= new_loc[1] < dim[1]:
                        flood_fill(board, ans, new_loc, dim)


def reveal_square(index, board, ans, rev=None):
    reveal = ans[index[0]][index[1]] if rev == None else rev
    board[index[0]][index[1]] = reveal
    if reveal == "0 ":
        flood_fill(board, ans, index, [len(board), len(board[0])])
    else:
        finished.append(index)
    return reveal

def check_win(finished, bomb_locations, dim):
    return len(finished) == ((dim[0] * dim[1]) - len(bomb_locations))

def check_square(board, ans, index: list, bomb_locations, dim):
    pts = get_pts(board)
    loc = [int(index[0]) - 1, int(index[1]) - 1]
    if loc not in finished:
        check = reveal_square(loc, board, ans)
        if check == "💣":
            for i in bomb_locations:
                reveal_square(i, board, ans)
            reveal_square(loc, board, ans, "💥")
            display(board, dim)
            print("You lost...")
            print(f"Your score was {pts}!")
            return False
        else:
            if check_win(finished, bomb_locations, dim):
                for i in bomb_locations:
                    reveal_square(i, board, ans)
                display(board, dim)
                print("You won!")
                print(f"Your score was {pts}!")
                return False
            else:
                return True
    else:
        print("This square has already been revealed!")
        return True

def start():
    global code
    ani.prints(intro)
    load_old_game = input("Would you like to load a previous game? (y/n)\n")
    if load_old_game.lower() == "y":
        exists, dat = load_data(code := input("Enter the room code: "), save_location)
        while not exists:
            retry = input("This code is invalid, would you like to start a new game or re-enter? (y/n/r)\n")
            if retry.lower() == "n":
                exit()
            elif retry.lower() == "y":
                return None
            else:
                exists, dat = load_data(code := input("Enter the room code: "), save_location)
        return dat
    elif load_old_game.lower() == "n":
        return None
    else:
        print("Invalid Option, Starting New Game...")
        return None
 