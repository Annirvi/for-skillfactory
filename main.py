#генерация пустого игрового поля
game_field = [[1, 2, 0], [3, 4, 6], [5, 7, 8]]
for i in range(0, len(game_field)):
    for j in range(0, len(game_field[i])):
        print(game_field[i][j], end=' ')
    print()

win_condition = True
if game_field[0][0] == game_field[0][1] == game_field[0][2]:
    print("win")
elif game_field[0][0] == game_field[1][1] == game_field[2][2]:
    print("win")
elif game_field[0][2] == game_field[1][1] == game_field[2][0]:
    print("win")
elif game_field[0][0] == game_field[1][0] == game_field[2][0]:
    print("win")
elif game_field[0][1] == game_field[1][1] == game_field[2][1]:
    print("win")
elif game_field[0][2] == game_field[1][2] == game_field[2][2]:
    print("win")
elif game_field[0][1] == game_field[1][1] == game_field[2][1]:
    print("win")
elif game_field[2][0] == game_field[2][1] == game_field[2][2]:
    print("win")
else:
    print("you lose")
    exit
