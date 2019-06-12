#! python3


def player_input(bpieces, wpieces, ospaces, vspaces, cplayer):
    try:
        uinput = input("Which piece would you like to move? (a1 - h8): ")
        if uinput not in vspaces:
            print("Invalid Move!\n")
            player_input(bpieces, wpieces, ospaces, vspaces, cplayer)
        elif (uinput not in wpieces and cplayer == 'White') or (uinput not in bpieces and cplayer == 'Black'):
            print("You don't have a piece there!\n")
            player_input(bpieces, wpieces, ospaces, vspaces, cplayer)
        elif (uinput in wpieces and cplayer == 'White') or (uinput in bpieces and cplayer == 'Black'):
            return uinput
    except:
        print("Invalid character or sequence!\n")
        player_input(bpieces, wpieces, ospaces, vspaces, cplayer)


def move_piece(p_to_m, bspaces, ospaces, vspaces, wpieces, bpieces, cplayer):
    try:
        uinput = input("Where would you like to move? (a1 - h8): ")
        if uinput not in vspaces:
            print("Invalid Move!\n")
            move_piece(p_to_m, bspaces, ospaces, vspaces, wpieces, bpieces, cplayer)
        elif (uinput in wpieces and cplayer == 'White') or (uinput in wpieces and cplayer == 'Black'):
            print("You can't take your own piece!\n")
            move_piece(p_to_m, bspaces, ospaces, vspaces, wpieces, bpieces, cplayer)
        elif uinput in ospaces:
            bspaces[uinput] = p_to_m
            return bspaces
    except:
        print("Invalid character or sequence!\n")
        move_piece(p_to_m, bspaces, ospaces, vspaces, wpieces, bpieces, cplayer)


def get_piece(uinput, bspaces):
    p_to_m = bspaces[uinput]
    bspaces[uinput] = '  '
    return p_to_m


def game_end_check(wpieces, bpieces, gend):
    if 'WK' not in wpieces or 'BK' not in bpieces:
        gend = True
        return gend


def white_turn(cplayer):
    
    cplayer = 'White'
    return cplayer


def black_turn(cplayer):
    cplayer = 'Black'
    return cplayer


def print_game_board(bspaces):
    gboard ="""     
    ---------------------------------------------------------------------
    | |//////|      |//////|      |//////|      |//////|      | |       |
    | |//{}//|  {}  |//{}//|  {}  |//{}//|  {}  |//{}//|  {}  | |   8   |
    | |//////|      |//////|      |//////|      |//////|      | |       |
    | |-------------------------------------------------------| |       |
    | |      |//////|      |//////|      |//////|      |//////| |       |
    | |  {}  |//{}//|  {}  |//{}//|  {}  |//{}//|  {}  |//{}//| |   7   |
    | |      |//////|      |//////|      |//////|      |//////| |       |
    | |-------------------------------------------------------| |       |
    | |//////|      |//////|      |//////|      |//////|      | |       |
    | |//{}//|  {}  |//{}//|  {}  |//{}//|  {}  |//{}//|  {}  | |   6   |
    | |//////|      |//////|      |//////|      |//////|      | |       |
    | |-------------------------------------------------------| |       |
    | |      |//////|      |//////|      |//////|      |//////| |       |
    | |  {}  |//{}//|  {}  |//{}//|  {}  |//{}//|  {}  |//{}//| |   5   |
    | |      |//////|      |//////|      |//////|      |//////| |       |
    | |-------------------------------------------------------| |       |
    | |//////|      |//////|      |//////|      |//////|      | |       |
    | |//{}//|  {}  |//{}//|  {}  |//{}//|  {}  |//{}//|  {}  | |   4   |
    | |//////|      |//////|      |//////|      |//////|      | |       |
    | |-------------------------------------------------------| |       |
    | |      |//////|      |//////|      |//////|      |//////| |       |
    | |  {}  |//{}//|  {}  |//{}//|  {}  |//{}//|  {}  |//{}//| |   3   |
    | |      |//////|      |//////|      |//////|      |//////| |       |
    | |-------------------------------------------------------| |       |
    | |//////|      |//////|      |//////|      |//////|      | |       |
    | |//{}//|  {}  |//{}//|  {}  |//{}//|  {}  |//{}//|  {}  | |   2   |
    | |//////|      |//////|      |//////|      |//////|      | |       |
    | |-------------------------------------------------------| |       |
    | |      |//////|      |//////|      |//////|      |//////| |       |
    | |  {}  |//{}//|  {}  |//{}//|  {}  |//{}//|  {}  |//{}//| |   1   |
    | |      |//////|      |//////|      |//////|      |//////| |       |
    | |-------------------------------------------------------| |-------|
    | |  a      b      c      d      e      f       g      h  | |///////|
    ---------------------------------------------------------------------
    """.format(
            bspaces['a8'], bspaces['b8'], bspaces['c8'], bspaces['d8'], bspaces['e8'], bspaces['f8'], bspaces['g8'], bspaces['h8'],
            bspaces['a7'], bspaces['b7'], bspaces['c7'], bspaces['d7'], bspaces['e7'], bspaces['f7'], bspaces['g7'], bspaces['h7'],
            bspaces['a6'], bspaces['b6'], bspaces['c6'], bspaces['d6'], bspaces['e6'], bspaces['f6'], bspaces['g6'], bspaces['h6'],
            bspaces['a5'], bspaces['b5'], bspaces['c5'], bspaces['d5'], bspaces['e5'], bspaces['f5'], bspaces['g5'], bspaces['h5'],
            bspaces['a4'], bspaces['b4'], bspaces['c4'], bspaces['d4'], bspaces['e4'], bspaces['f4'], bspaces['g4'], bspaces['h4'],
            bspaces['a3'], bspaces['b3'], bspaces['c3'], bspaces['d3'], bspaces['e3'], bspaces['f3'], bspaces['g3'], bspaces['h3'],
            bspaces['a2'], bspaces['b2'], bspaces['c2'], bspaces['d2'], bspaces['e2'], bspaces['f2'], bspaces['g2'], bspaces['h2'],
            bspaces['a1'], bspaces['b1'], bspaces['c1'], bspaces['d1'], bspaces['e1'], bspaces['f1'], bspaces['g1'], bspaces['h1']
        )
    print(gboard)


def main():
    board_spaces = {
        'a8': 'BR', 'b8': 'BN', 'c8': 'BB', 'd8': 'BQ', 'e8': 'BK', 'f8': 'BB', 'g8': 'BN', 'h8': 'BR',
        'a7': 'BP', 'b7': 'BP', 'c7': 'BP', 'd7': 'BP', 'e7': 'BP', 'f7': 'BP', 'g7': 'BP', 'h7': 'BP',
        'a6': '  ', 'b6': '  ', 'c6': '  ', 'd6': '  ', 'e6': '  ', 'f6': '  ', 'g6': '  ', 'h6': '  ',
        'a5': '  ', 'b5': '  ', 'c5': '  ', 'd5': '  ', 'e5': '  ', 'f5': '  ', 'g5': '  ', 'h5': '  ',
        'a4': '  ', 'b4': '  ', 'c4': '  ', 'd4': '  ', 'e4': '  ', 'f4': '  ', 'g4': '  ', 'h4': '  ',
        'a3': '  ', 'b3': '  ', 'c3': '  ', 'd3': '  ', 'e3': '  ', 'f3': '  ', 'g3': '  ', 'h3': '  ',
        'a2': 'WP', 'b2': 'WP', 'c2': 'WP', 'd2': 'WP', 'e2': 'WP', 'f2': 'WP', 'g2': 'WP', 'h2': 'WP',
        'a1': 'WR', 'b1': 'WN', 'c1': 'WB', 'd1': 'WQ', 'e1': 'WK', 'f1': 'WB', 'g1': 'WN', 'h1': 'WR'
    }

    current_player = 'White'
    valid_spaces = board_spaces.keys()
    black_pieces = [i for i in valid_spaces if board_spaces[i] != '  ' and board_spaces[i][0] == 'B']
    white_pieces = [i for i in valid_spaces if board_spaces[i] != '  ' and board_spaces[i][0] == 'W']
    open_spaces = [i for i in valid_spaces if board_spaces[i] == '  ']
    game_end = False
    #white_pieces_taken = []
    #black_pieces_taken = []


    while game_end == False:

        print_game_board(board_spaces)

        if current_player == 'White':
            print("White's Turn!\n")
            user_input = player_input(black_pieces, white_pieces, open_spaces, valid_spaces, current_player)
            piece_to_move = get_piece(user_input, board_spaces)
            board_spaces = move_piece(piece_to_move, board_spaces, open_spaces, valid_spaces, white_pieces, black_pieces, current_player)
        
        print_game_board(board_spaces)
        game_end = game_end_check(white_pieces, black_pieces, game_end)    
        current_player = black_turn(current_player)
        
        if current_player == 'Black':
            print("Black's Turn!\n")
            user_input = player_input(black_pieces, white_pieces, open_spaces, valid_spaces, current_player)
            piece_to_move = get_piece(user_input, board_spaces)
            board_spaces = move_piece(piece_to_move, board_spaces, open_spaces, valid_spaces, white_pieces, black_pieces, current_player)
            
        print_game_board(board_spaces)
        game_end = game_end_check(white_pieces, black_pieces, game_end)    
        current_player = white_turn(current_player)


if __name__ == "__main__":
    main()