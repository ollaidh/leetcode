import copy
from dataclasses import dataclass

import my_utils.testing as tst


class InvalidDimensionsError(Exception):
    def __str__(self):
        return 'Invalid dimensions!'


class NoMovesError(Exception):
    def __str__(self):
        return 'No more possible moves!'


class YouWon(Exception):
    def __str__(self):
        return 'What a great tour! Congratulations!'


@dataclass
class Cell:
    knight_is = False
    knight_was = False
    possible_moves = -1
    step_visited = 0

    def is_empty(self):
        return not self.knight_is and not self.knight_was


def test_cell_is_empty():
    cell = Cell()

    tst.verify_if_equal(cell.is_empty(), True, '')

    cell.knight_is, cell.knight_was = True, False
    tst.verify_if_equal(cell.is_empty(), False, '')

    cell.knight_is, cell.knight_was = False, True
    tst.verify_if_equal(cell.is_empty(), False, '')

    cell.knight_is, cell.knight_was = True, True
    tst.verify_if_equal(cell.is_empty(), False, '')


class Chessboard:
    def __init__(self, sizex, sizey):
        self.knight_pos_x = -1
        self.knight_pos_y = -1
        self.knight_pos_x_init = -1
        self.knight_pos_y_init = -1
        self.visited = 0  # how many cells was visited by the knight during game
        self.user_play = True

        self.board = []

        try:
            self.sizex = int(sizex)
            self.sizey = int(sizey)
            if self.sizex <= 0 or self.sizey <= 0:
                raise InvalidDimensionsError

            for i in range(self.sizey):
                line = []
                for j in range(self.sizex):
                    cell = Cell()
                    line.append(cell)
                self.board.append(line)
        except ValueError:
            raise InvalidDimensionsError

    # converts board coordinates into matrix coordinates
    # board: zero point in left lower angle, index starts from 1, X axis from left to right, Y axis from bottom to top
    # matrix: zero point in left upper angle, index starts from 0, X axis from top to bottom, Y axis left to right
    def coord_conv_to_internal(self, board_x, board_y):
        matrix_x = self.sizey - board_y
        matrix_y = board_x - 1
        return matrix_x, matrix_y

    def coord_conv_to_board(self, intern_x, intern_y):
        board_y = self.sizey - intern_x
        board_x = intern_y + 1
        return board_x, board_y

    def add_knight(self, xpos, ypos):
        if not self.is_inside_board(int(xpos), int(ypos)):
            raise InvalidDimensionsError
        self.knight_pos_x, self.knight_pos_y = self.coord_conv_to_internal(int(xpos), int(ypos))
        self.knight_pos_x_init, self.knight_pos_y_init = self.knight_pos_x, self.knight_pos_y
        self.board[self.knight_pos_x][self.knight_pos_y].knight_is = True
        self.visited += 1
        self.board[self.knight_pos_x][self.knight_pos_y].step_visited = self.visited

    def is_inside_board(self, x, y):
        if 0 < x <= self.sizex and 0 < y <= self.sizey:
            return True
        return False

    def is_inside_matrix(self, x, y):
        if 0 <= x < self.sizey and 0 <= y < self.sizex:
            return True
        return False

    def is_empty_cell(self, x, y):
        if self.board[x][y].knight_is or self.board[x][y].knight_was:
            return False
        return True

    def is_any_moves(self):
        for row in range(self.sizey):
            for line in range(self.sizex):
                if self.board[row][line].possible_moves != -1:
                    return True
        return False

    # find positions, where the knight can be moved and counts how many moves can be made from each position
    def check_movedir(self, x_new, y_new):
        xknight, yknight = self.coord_conv_to_internal(int(x_new), int(y_new))

        possible_moves = [[-2, -1], [-2, 1], [-1, 2], [1, 2], [2, 1], [2, -1], [1, -2], [-1, -2]]
        for move in possible_moves:
            if self.is_inside_matrix(xknight + move[0], yknight + move[1]) and self.is_empty_cell(xknight + move[0], yknight + move[1]):
                test_x = xknight + move[0]
                test_y = yknight + move[1]
                counter = 0
                for m in possible_moves:
                    if self.is_inside_matrix(test_x + m[0], test_y + m[1]) and self.is_empty_cell(test_x + m[0], test_y + m[1]):
                        counter += 1
                self.board[test_x][test_y].possible_moves = counter
        if not self.is_any_moves():
            raise NoMovesError

    def clear_possible_moves(self):
        for row in range(self.sizey):
            for line in range(self.sizex):
                self.board[row][line].possible_moves = -1

    def move_knight(self, x, y):
        xpos, ypos = self.coord_conv_to_internal(int(x), int(y))
        if xpos < 0 or xpos >= self.sizey or ypos < 0 or ypos >= self.sizex:
            raise InvalidDimensionsError
        else:
            if self.board[xpos][ypos].possible_moves != -1:

                self.board[self.knight_pos_x][self.knight_pos_y].knight_is = False
                self.board[self.knight_pos_x][self.knight_pos_y].knight_was = True
                self.board[xpos][ypos].knight_is = True
                self.knight_pos_x = xpos
                self.knight_pos_y = ypos
                self.visited += 1
                self.board[self.knight_pos_x][self.knight_pos_y].step_visited = self.visited
                if self.visited == self.sizex * self.sizey:
                    raise YouWon
            else:
                raise InvalidDimensionsError

        self.clear_possible_moves()

    def min_moves_cell(self):
        min_moves = 8
        i_move = 0
        j_move = 0

        for i in range(self.sizey):
            for j in range(self.sizex):
                if min_moves > self.board[i][j].possible_moves >= 0:
                    min_moves = self.board[i][j].possible_moves
                    i_move = i
                    j_move = j
        return i_move, j_move, min_moves

    def __str__(self):
        lines = []

        border = ' ' * len(str(self.sizey)) + '-' * (self.sizex * ((len(str(self.sizex * self.sizey))) + 1) + 3)
        lines.append(border)

        current_row_index = len(self.board)
        for row in range(self.sizey):
            cells = []
            for column in range(self.sizex):
                if self.user_play:
                    if self.board[row][column].is_empty() and self.board[row][column].possible_moves == -1:
                        cells.append('_' * len(str(self.sizex * self.sizey)))
                    elif self.board[row][column].knight_is:
                        cells.append(' ' * (len(str(self.sizex * self.sizey)) - 1) + 'X')
                    elif self.board[row][column].knight_was:
                        cells.append(' ' * (len(str(self.sizex * self.sizey)) - 1) + '*')
                    elif self.board[row][column].possible_moves != -1:
                        cells.append(' ' * (len(str(self.sizex * self.sizey)) -
                                            len(str(self.board[row][column].possible_moves))) +
                                     str(self.board[row][column].possible_moves))
                elif not self.user_play:
                    cells.append(' ' * (len(str(self.sizex * self.sizey)) - len(str(self.board[row][column].step_visited))) + str(self.board[row][column].step_visited))
            row_repr = ' ' * (len(str(self.sizey)) - len(str(current_row_index))) + str(current_row_index) + '| ' + ' '.join(cells) + ' |'
            lines.append(row_repr)
            current_row_index -= 1

        lines.append(border)

        cells = []
        for column in range(self.sizex):
            cells.append(' ' * (len(str(self.sizex * self.sizey)) - len(str(column + 1)) + 1) + str(column + 1))

        line_repr = ' ' * (len(str(self.sizey)) + 1) + ''.join(cells)
        lines.append(line_repr)

        return '\n'.join(lines)


class Game:
    def auto_game(self, board):
        board.user_play = False
        kx, ky = board.coord_conv_to_board(board.knight_pos_x, board.knight_pos_y)
        board.check_movedir(kx, ky)

        while True:
            try:
                pos_x, pos_y, moves = board.min_moves_cell()
                x, y = board.coord_conv_to_board(pos_x, pos_y)
                board.move_knight(x, y)
                board.check_movedir(x, y)
            except NoMovesError:
                return False
            except YouWon as err:
                for i in range(board.sizey):
                    for j in range(board.sizex):
                        board.board[i][j].knight_was = False
                        board.board[i][j].knight_is = False
                return True

    def check_is_solution(self, board):
        virtual_board = copy.deepcopy(board)
        return self.auto_game(virtual_board)


def test_create_board():
    for len_x in range(3, 6):
        for len_y in range(2, 5):
            board = Chessboard(len_x, len_y)
            tst.verify_if_equal(board.sizex, len_x, "X board coord")
            tst.verify_if_equal(board.sizey, len_y, "Y board coord")
            tst.verify_if_equal(len(board.board[0]), len_x, "Length along X")
            tst.verify_if_equal(len(board.board), len_y, "Length along Y")


def test_copy_board():
    board1 = Chessboard(6, 5)

    knight_x, knight_y = 2, 2
    knight_x, knight_y = board1.coord_conv_to_internal(knight_x, knight_y)
    board1.add_knight(2, 2)
    board1.board[0][1].possible_moves = 42
    board2 = copy.deepcopy(board1)
    tst.verify_if_equal(board1.board[knight_x][knight_y].knight_is, True, "Board 1")
    tst.verify_if_equal(board2.board[knight_x][knight_y].knight_is, True, "Copied board")
    tst.verify_if_equal(board2.board[0][1].possible_moves, 42, "Additional data")
    board1.board[knight_x][knight_y].knight_is = False
    tst.verify_if_equal(board1.board[knight_x][knight_y].knight_is, False, "Board 1 after move")
    tst.verify_if_equal(board2.board[knight_x][knight_y].knight_is, True, "Copied board after move")
    tst.verify_if_equal(board2.board[0][1].possible_moves, 42, "Additional data")


def test_coordconv_to_internal():
    """tests for the function that converts board coordinates into matrix coordinates"""
    board = Chessboard(6, 5)
    tst.run_test(board.coord_conv_to_internal, (1, 2), (3, 0), 'Convert BORD to INTERNAL coords')
    tst.run_test(board.coord_conv_to_internal, (6, 5), (0, 5), 'Convert BORD to INTERNAL coords')
    tst.run_test(board.coord_conv_to_internal, (6, 3), (2, 5), 'Convert BORD to INTERNAL coords')
    tst.run_test(board.coord_conv_to_internal, (3, 4), (1, 2), 'Convert BORD to INTERNAL coords')
    tst.run_test(board.coord_conv_to_internal, (1, 5), (0, 0), 'Convert BORD to INTERNAL coords')
    tst.run_test(board.coord_conv_to_internal, (6, 1), (4, 5), 'Convert BORD to INTERNAL coords')
    tst.run_test(board.coord_conv_to_internal, (1, 1), (4, 0), 'Convert BORD to INTERNAL coords')
    tst.run_test(board.coord_conv_to_internal, (6, 5), (0, 5), 'Convert BORD to INTERNAL coords')

    board2 = Chessboard(6, 6)
    tst.run_test(board2.coord_conv_to_internal, (2, 2), (4, 1), 'Convert BORD to INTERNAL coords')
    tst.run_test(board2.coord_conv_to_internal, (4, 1), (5, 3), 'Convert BORD to INTERNAL coords')
    tst.run_test(board2.coord_conv_to_internal, (3, 3), (3, 2), 'Convert BORD to INTERNAL coords')
    tst.run_test(board2.coord_conv_to_internal, (1, 4), (2, 0), 'Convert BORD to INTERNAL coords')

    board2 = Chessboard(4, 3)
    tst.run_test(board2.coord_conv_to_internal, (4, 3), (0, 3), 'Convert BORD to INTERNAL coords')


def test_coordconv_to_board():
    """tests for the function that converts matrix coordinates into board coordinates"""
    board = Chessboard(6, 5)
    tst.run_test(board.coord_conv_to_board, (0, 0), (1, 5), 'Convert INTERNAL to BORD coords')
    tst.run_test(board.coord_conv_to_board, (3, 0), (1, 2), 'Convert INTERNAL to BORD coords')
    tst.run_test(board.coord_conv_to_board, (0, 5), (6, 5), 'Convert INTERNAL to BORD coords')
    tst.run_test(board.coord_conv_to_board, (1, 2), (3, 4), 'Convert INTERNAL to BORD coords')
    tst.run_test(board.coord_conv_to_board, (0, 5), (6, 5), 'Convert INTERNAL to BORD coords')

    board2 = Chessboard(6, 6)
    tst.run_test(board2.coord_conv_to_board, (4, 1), (2, 2), 'Convert INTERNAL to BORD coords')
    tst.run_test(board2.coord_conv_to_board, (5, 3), (4, 1), 'Convert INTERNAL to BORD coords')
    tst.run_test(board2.coord_conv_to_board, (3, 2), (3, 3), 'Convert INTERNAL to BORD coords')
    tst.run_test(board2.coord_conv_to_board, (2, 0), (1, 4), 'Convert INTERNAL to BORD coords')

    board2 = Chessboard(4, 3)
    tst.run_test(board2.coord_conv_to_board, (0, 3), (4, 3), 'Convert INTERNAL to BORD coords')


def test_is_inside_matrix():
    """tests for the function that checks if coords are inside matrix.
    Note: creating board in board coords, coords - in matrix coord"""
    board = Chessboard(5, 4)
    tst.run_test(board.is_inside_matrix, (3, 3), True, 'Is inside matrix')
    tst.run_test(board.is_inside_matrix, (0, 0), True, 'Is inside matrix')
    tst.run_test(board.is_inside_matrix, (1, 1), True, 'Is inside matrix')
    tst.run_test(board.is_inside_matrix, (3, 2), True, 'Is inside matrix')
    tst.run_test(board.is_inside_matrix, (4, 6), False, 'Is inside matrix')
    tst.run_test(board.is_inside_matrix, (6, 4), False, 'Is inside matrix')
    tst.run_test(board.is_inside_matrix, (5, 4), False, 'Is inside matrix')


def test_is_inside_board():
    """tests for the function that checks if coords are inside matrix.
    Note: creating board in board coords, coords - in board coord"""
    board = Chessboard(5, 4)
    tst.run_test(board.is_inside_board, (3, 3), True, 'Is inside board')
    tst.run_test(board.is_inside_board, (0, 0), False, 'Is inside board')
    tst.run_test(board.is_inside_board, (1, 1), True, 'Is inside board')
    tst.run_test(board.is_inside_board, (3, 2), True, 'Is inside board')
    tst.run_test(board.is_inside_board, (4, 6), False, 'Is inside board')
    tst.run_test(board.is_inside_board, (6, 4), False, 'Is inside board')
    tst.run_test(board.is_inside_board, (5, 4), True, 'Is inside board')


def run_all_tests():
    test_create_board()
    test_copy_board()
    test_coordconv_to_internal()
    test_coordconv_to_board()
    test_cell_is_empty()
    test_is_inside_matrix()
    test_is_inside_board()


def main():
    while True:
        try:
            sizex, sizey = (input('Enter your board dimensions:')).split()
            board = Chessboard(sizex, sizey)
            game = Game()
            break
        except ValueError:
            print('Invalid dimensions!')
        except InvalidDimensionsError as err:
            print(err)

    while True:
        try:
            kx, ky = (input('Enter the knight\'s starting position:')).split()
            board.add_knight(kx, ky)
            break
        except ValueError:
            print('Invalid dimensions!')
        except InvalidDimensionsError as err:
            print(err)

    while True:
        try_puzzle = str(input('Do you want to try the puzzle? (y/n):'))
        # computer plays:
        if try_puzzle == 'n':
            if game.auto_game(board):
                print('Here\'s the solution!')
                print(board)
                return
            else:
                print('No solution exists!')
                break
        elif try_puzzle == 'y':
            # check if there is a solution:
            is_solution = game.check_is_solution(board)
            if is_solution is False:
                print('No solution exists!')
                return
            # user plays:
            board.check_movedir(kx, ky)
            print(board)
            while True:
                print('Enter your next move:', end='')
                while True:
                    try:
                        xmove, ymove = (input()).split()
                        board.move_knight(xmove, ymove)
                        board.check_movedir(xmove, ymove)
                        print(board)
                        break
                    except ValueError:
                        print('Invalid move! Enter your next move:', end='')
                    except InvalidDimensionsError:
                        print('Invalid move! Enter your next move:', end='')
                    except NoMovesError as err:
                        print(err)
                        print('Your knight visited', board.visited, 'squares!')
                        return
                    except YouWon as err:
                        print(board)
                        print(err)
                        return
        else:
            print('Invalid input!')


if __name__ == '__main__':
    # run_all_tests()
    main()

