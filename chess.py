"""Chess Game"""

class InvalidPositionError(Exception):
    pass


class ChessBoard:
    def __init__(self):
        self.size = 8

    def is_valid_position(self, position):
        if len(position) != 2:
            return False
        column, row = position
        return column in 'abcdefgh' and row in '12345678'

    def position_to_indices(self, position):
        if not self.is_valid_position(position):
            raise InvalidPositionError(f"Invalid position: {position}")
        column, row = position
        return ord(column) - ord('a'), int(row) - 1

    def can_queen_move(self, start, end):
        try:
            start_x, start_y = self.position_to_indices(start)
            end_x, end_y = self.position_to_indices(end)
        except InvalidPositionError as e:
            return str(e)

        if start == end:
            return "Start and end positions are the same."

        dx = abs(end_x - start_x)
        dy = abs(end_y - start_y)

        if dx == dy or dx == 0 or dy == 0:
            return True
        else:
            return False

    def can_knight_move(self, start, end):
        try:
            start_x, start_y = self.position_to_indices(start)
            end_x, end_y = self.position_to_indices(end)
        except InvalidPositionError as e:
            return str(e)

        if start == end:
            return "Start and end positions are the same."

        dx = abs(end_x - start_x)
        dy = abs(end_y - start_y)

        if (dx == 2 and dy == 1) or (dx == 1 and dy == 2):
            return True
        else:
            return False


def main():
    board = ChessBoard()
    
    # Test Queen Moves
    print("Queen Move Test:")
    start_pos = input("Enter start position for Queen (e.g., 'd4'): ")
    end_pos = input("Enter end position for Queen (e.g., 'e5'): ")
    result = board.can_queen_move(start_pos, end_pos)
    if result == True:
        print(f"Queen can move from {start_pos} to {end_pos} in one move.")
    elif result == False:
        print(f"Queen cannot move from {start_pos} to {end_pos} in one move.")
    else:
        print(result)
    
    # Test Knight Moves
    print("\nKnight Move Test:")
    start_pos = input("Enter start position for Knight (e.g., 'g1'): ")
    end_pos = input("Enter end position for Knight (e.g., 'f3'): ")
    result = board.can_knight_move(start_pos, end_pos)
    if result == True:
        print(f"Knight can move from {start_pos} to {end_pos} in one move.")
    elif result == False:
        print(f"Knight cannot move from {start_pos} to {end_pos} in one move.")
    else:
        print(result)


if __name__ == "__main__":
    main()
