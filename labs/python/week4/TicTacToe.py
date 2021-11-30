def display_instruct():
    print('''
        WELCOME TO TIC TAC TOE

    YOU WILL BE PLAYING AGAINST THE 
    COMPUTER BY INPUTTING A NUMBER
            BETWEEN 0-8

             0 | 1 | 2 
            -----------
             3 | 4 | 5
            -----------
             6 | 7 | 8

    ''')

def ask_yes_no(question):
    response = None
    while response not in ('yes', 'no'):
        response = input(question)
    return response

def ask_number(question, low, high):
    response = None
    while response not in range(low, high):
        response = int(input(question))
    return response

def pieces():
    go_first = ask_yes_no('Would you like to go first: ')
    if go_first == 'yes': 
        print('You\'re taking the first move.')
        human = 'X'
        cpu = 'O'
    else:
        print('Ooooo you\'re brave, i\'ll take the first move then.')
        human = 'O'
        cpu = 'X'

def new_board():
    board = []
    for i in range(9):
        board.append(' ')
    return board

def display_board(board):
    """Display game board on screen.""" 
    print("\n\t", board[0], "|", board[1], "|", board[2]) 
    print("\t", "---------") 
    print("\t", board[3], "|", board[4], "|", board[5]) 
    print("\t", "---------") 
    print("\t", board[6], "|", board[7], "|", board[8], "\n")

def legal_moves(board): 
    """Create list of legal moves.""" 
    moves = [] 
    for square in range(9): 
        if board[square] == ' ': 
            moves.append(square) 
    return moves

def winner(board):
    WAYS_TO_WIN = (
        (0,1,2),
        (3,4,5),
        (6,7,8),
        (0,3,6),
        (1,4,7),
        (2,5,8),
        (0,4,8),
        (2,4,6)
    )
    for row in WAYS_TO_WIN:
        if board[row[0]] == board[row[1]] == board[row[2]] != ' ':
            winner = board[row[0]]
            return winner
        if ' ' not in board:
            return 'TIE'
        return None

def human_move(board, human):
    