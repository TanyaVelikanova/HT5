
field = [1, 2, 3, 4, 5, 6, 7, 8, 9]

def show_field():
    global field
    for i in range(0, len(field), 3):
        print(field[i], field[i+1], field[i+2])


def input_otmetka(otmetka):
    valid = False
    while not valid:
        player_choice = int(input(f'Выберите позицию для {otmetka} '))
        if player_choice >= 1 and player_choice <= 9:
            if (str(field[player_choice-1]) not in 'XO'):
                field[player_choice-1] = otmetka
                valid = True
            else:
                print('Позиция занята')
        else:
            print('Ввведите число от 1 до 9')

def proverka(field):
    win_variant = ((0,1,2), (3,4,5), (6,7,8), (0,3,6), (1,4,7), (2,5,8), (0,4,8), (2,4,6))
    for each in win_variant:
       if field[each[0]] == field[each[1]] == field[each[2]]:
          return field[each[0]]
    return False

hod=0
game_over = False
while not game_over:
    show_field()
    if hod % 2 == 0:
        input_otmetka('X')
    else:
        input_otmetka('O')
    hod += 1
    if hod > 4:
        if proverka(field):
            show_field()
            print('Победа')
            game_over = True
            break
    if hod == 9:
        print('Ничья!')
        show_field()
        break
