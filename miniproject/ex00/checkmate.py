def create_board_from_string(board_str):
    return [line.strip() for line in board_str.strip().splitlines()]


def is_inrange(pos, board_size):
    return (0 <= pos[0] < board_size) and (0 <= pos[1] < board_size)


def is_checkable(board, board_size, piece, from_pos):
    # Pawn : move "up left" and "up right"
    if (piece == 'P'):
        # up left
        tmp_pos = (from_pos[0]-1, from_pos[1]-1)
        if is_inrange(tmp_pos, board_size) and (board[tmp_pos[0]][tmp_pos[1]] == 'K'):
            return True
        # up right
        tmp_pos = (from_pos[0]-1, from_pos[1]+1)
        if is_inrange(tmp_pos, board_size) and (board[tmp_pos[0]][tmp_pos[1]] == 'K'):
            return True
        return False

    # Bishop : move diagonally
    if (piece == 'B'):
        q1 = q2 = q3 = q4 = True
        step = 1
        while (q1 or q2 or q3 or q4):
            # quadrant 1 (top left)
            if (q1):
                tmp_pos = (from_pos[0]-step, from_pos[1]-step)
                if is_inrange(tmp_pos, board_size):
                    if (board[tmp_pos[0]][tmp_pos[1]] == 'K'):
                        return True
                    if (board[tmp_pos[0]][tmp_pos[1]] != '.'):
                        q1 = False
                else:
                    q1 = False
            # quadrant 2 (top right)
            if (q2):
                tmp_pos = (from_pos[0]-step, from_pos[1]+step)
                if is_inrange(tmp_pos, board_size):
                    if (board[tmp_pos[0]][tmp_pos[1]] == 'K'):
                        return True
                    if (board[tmp_pos[0]][tmp_pos[1]] != '.'):
                        q2 = False
                else:
                    q2 = False
            # quadrant 3 (bottom left)
            if (q3):
                tmp_pos = (from_pos[0]+step, from_pos[1]-step)
                if is_inrange(tmp_pos, board_size):
                    if (board[tmp_pos[0]][tmp_pos[1]] == 'K'):
                        return True
                    if (board[tmp_pos[0]][tmp_pos[1]] != '.'):
                        q3 = False
                else:
                    q3 = False
            # quadrant 4 (bottom right)
            if (q4):
                tmp_pos = (from_pos[0]+step, from_pos[1]+step)
                if is_inrange(tmp_pos, board_size):
                    if (board[tmp_pos[0]][tmp_pos[1]] == 'K'):
                        return True
                    if (board[tmp_pos[0]][tmp_pos[1]] != '.'):
                        q4 = False
                else:
                    q4 = False
            step += 1
        return False

    # Rook : move straight (horizontal and vertical)
    if (piece == 'R'):
        q1 = q2 = q3 = q4 = True
        step = 1
        while (q1 or q2 or q3 or q4):
            # move up
            if (q1):
                tmp_pos = (from_pos[0]-step, from_pos[1])
                if is_inrange(tmp_pos, board_size):
                    if (board[tmp_pos[0]][tmp_pos[1]] == 'K'):
                        return True
                    if (board[tmp_pos[0]][tmp_pos[1]] != '.'):
                        q1 = False
                else:
                    q1 = False
            # move right
            if (q2):
                tmp_pos = (from_pos[0], from_pos[1]+step)
                if is_inrange(tmp_pos, board_size):
                    if (board[tmp_pos[0]][tmp_pos[1]] == 'K'):
                        return True
                    if (board[tmp_pos[0]][tmp_pos[1]] != '.'):
                        q2 = False
                else:
                    q2 = False
            # move down
            if (q3):
                tmp_pos = (from_pos[0]+step, from_pos[1])
                if is_inrange(tmp_pos, board_size):
                    if (board[tmp_pos[0]][tmp_pos[1]] == 'K'):
                        return True
                    if (board[tmp_pos[0]][tmp_pos[1]] != '.'):
                        q3 = False
                else:
                    q3 = False
            # move left
            if (q4):
                tmp_pos = (from_pos[0], from_pos[1]-step)
                if is_inrange(tmp_pos, board_size):
                    if (board[tmp_pos[0]][tmp_pos[1]] == 'K'):
                        return True
                    if (board[tmp_pos[0]][tmp_pos[1]] != '.'):
                        q4 = False
                else:
                    q4 = False
            step += 1
        return False

    # Queen  : move in straight lines (horizontal and vertical) and diagonally
    if (piece == 'Q'):
        # So, moves like a combination of a bishop and a rook
        return is_checkable(board, board_size, 'B', from_pos) or is_checkable(board, board_size, 'R', from_pos)


def checkmate(board_str):
    board = create_board_from_string(board_str)
    board_size = len(board)

    for i in range(board_size):
        for j in range(board_size):
            this_piece = board[i][j]
            if (this_piece != '.' and this_piece != 'K'):
                if (is_checkable(board, board_size, this_piece, (i, j))):
                    # return True
                    print("Success")
                    return
    # return False
    print("Fail")
