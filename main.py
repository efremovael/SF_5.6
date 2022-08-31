#создание доски
def create_game_board(game_board_list):
    print('*'*13)
    for i in range(3):
        print('|', game_board_list[0 + i * 3], '|', game_board_list[1 + i * 3], '|', game_board_list[2 + i * 3], '|')
        print('*'*13)

#перерисовка доски
def take_move(move, counter):
    if move  in game_board_list:
        move_cell = game_board_list.index(move)
        if counter % 2 == 0:
            game_board_list[move_cell] = 'O'
        else:
            game_board_list[move_cell] = 'X'
        return game_board_list
    else:
        return "Укажите клетку из доступных на поле"


#проверка на победу
def winner_checking(game_board_list):
    winner_combination = ((0,1,2), (3,4,5),(6,7,8),(0,3,6),(1,4,7),(2,5,8),(0,4,8),(2,4,6))
    for i in winner_combination:
        if game_board_list[i[0]] == game_board_list[i[1]] == game_board_list[i[2]]:
            return True
        else:
            return False

def game():
    game_board_list = list(range(1, 10))
    create_game_board(game_board_list)
    win = False
    counter = 0
    while not win:
        if counter % 2 == 0:
            playerID = "X"
        else:
            playerID = 'O'
        if counter  == 9:
            print('Ничья!')
            break
        if winner_checking(game_board_list):
            print('Ты выиграл,'+ playerID)
            break
        move = int(input('Ты ходишь, ' + playerID))
        take_move(move, counter)
        create_game_board(game_board_list)
        counter += 1

game()




