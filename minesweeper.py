from data_handler import save_data, del_save
import animation_handler as ani
import minesweeper_tools as mt

# num = (n^2)/Φ+1
#1/2(1+5**0.5)
def minesweeper():
    mt.display(board, dim)
    choice1 = input("Enter dim(x,y) or type 'save' to save the game: ")
    if choice1.lower() != "save":
        ch = [int(i) for i in choice1.split(",")]
        if mt.valid_pos(ch, dim):
            if not mt.check_square(board, ans, ch, bomb_locations, dim):
                if mt.saved:
                    del_save(mt.code, mt.save_location)
                return False
            else: 
                return True
        else:
            print("Invalid Position.")
            return True
    else:
        mt.code = save_data([board, ans, dim], mt.save_location, mt.code)
        print("Your room code is:", mt.code)
        return False


if __name__ == "__main__":
    ignore = []
    loaded_data = mt.start()
    option = ""
    if loaded_data == None:
        option = input(
            """
Choose your difficulty: 
1. Easy
2. Medium
3. Hard
4. ⚠???⚠
"""
        )
        while option not in mt.options.keys():
            print("Invalid Option, Try Again.")
            option = input(
            """
Choose your difficulty: 
1. Easy
2. Medium
3. Hard
4. ⚠???⚠
"""
        )
        dim = mt.difficulty[option].split("x")
        dim = [int(i) for i in dim]
        ani.prints((mt.begin.format(mt.options[option]) if loaded_data == None else "Loading your save..."))
        ignore = input("Enter dim(x,y): ").split(",")
        while not mt.valid_pos(ignore, dim):
            print("Invalid Position, Try Again.")
            ignore = [int(i) for i in input("Enter dim(x,y): ").split(",")] 
        board, ans = mt.create_board(dim, ignore)
        bomb_locations = mt.get_bomb_pos(ans)
        mt.check_square(board, ans, ignore, bomb_locations, dim)
        
    else:
        board, ans, dim = loaded_data
        bomb_locations = mt.get_bomb_pos(ans)

    while True:
        #mt.display(ans, dim)
        if not minesweeper():
            input("Game Over! Press Enter to exit...")
            break
