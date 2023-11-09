board = [' ' for _ in range(9)]


def print_board():
    print(board[0], '|', board[1], '|', board[2])
    print('---------')
    print(board[3], '|', board[4], '|', board[5])
    print('---------')
    print(board[6], '|', board[7], '|', board[8])

#проверка победы
def win_condition(player):
    if board[2] == board[5] == board[8] == player:
        return True

    if board[1] == board[4] == board[7] == player:
        return True

    if board[0] == board[3] == board[6] == player:
        return True

    if board[6] == board[7] == board[8] == player:
        return True

    if board[3] == board[4] == board[5] == player:
        return True

    if board[0] == board[1] == board[2] == player:
        return True

    if board[0] == board[4] == board[8] == player:
        return True

    if board[2] == board[4] == board[6] == player:
        return True
    return False

def play_game():
    player = 'X'
    while True:
        print_board()
        move = int(input("Игрок " + player + ", ваш ход? (1-9): "))
        if move < 1 or move > 9:
            print("Неверный ход, попробуй еще раз")

        elif board[move - 1] == ' ':
            board[move - 1] = player
            if win_condition(player):
                print_board()
                print("Игрок", player, "победил!")
                break
            elif ' ' not in board:
                print_board()
                print("Ничья!")
                break
            player = 'O' if player == 'X' else 'X'
        else:
            print("Неверный ход, попробуй еще раз")


play_game()