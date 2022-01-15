print("*" * 10, " Игра Крестики-нолики для двух игроков ", "*" * 10)

board = list(range(1,10))                                                                 # С помощью команды range мы задаем максимальное количество ячеек

def draw_board(board):                                                                    # def это функци или же пользовательская команда, которая в дальнейшем легче выводится и редактируется
   print("-" * 13)
   for i in range(3):
      print("|", board[0+i*3], "|", board[1+i*3], "|", board[2+i*3], "|")                 # Рисует внешний вид доски
      print("-" * 13)

def take_input(player_token):
   valid = False                                                                          # False значит что игра еще не окончена, True будет означать что игра подошла к концу
   while not valid:
      player_answer = input("Куда поставим " + player_token+"? ") 
      try:
         player_answer = int(player_answer)
      except:
         print("Некорректный ввод. Вы уверены, что ввели число?")
         continue
      if player_answer >= 1 and player_answer <= 9: 
         if(str(board[player_answer-1]) not in "XO"):                                     # Проверяет наличия X или 0 на индексах
            board[player_answer-1] = player_token
            valid = True
         else:
            print("Эта клетка уже занята!")
      else:
        print("Некорректный ввод. Введите число от 1 до 9.")

def check_win(board):
   win_coord = ((0,1,2), (3,4,5), (6,7,8), (0,3,6), (1,4,7), (2,5,8), (0,4,8), (2,4,6))   # Координаты ячеек индексами
   for each in win_coord:
       if board[each[0]] == board[each[1]] == board[each[2]]:                             # board[each[0]] == board[each[1]] == board[each[2]]: - проверяет находится ли Х или 0 на координатах(ячейках) по индэксам масива 
          return board[each[0]]
   return False

def main(board):
    counter = 0                                                                           # Количество ходов
    win = False                                                                           # False значит что игра еще не окончена, True будет означать что игра подошла к концу
    while not win: 
        draw_board(board)                                                                 # Вызывает функцию которая рисует доску
        if counter % 2 == 0:                                                              # % - Деление по модулю, проверяет остаток от деления если остаток имеется, то число не четное 
           take_input("X")                                                                # take_input - в зависимости от хода ставит нужное значение в ячейку X или
        else:
           take_input("O")
        counter += 1                                                                      # Когда значение введено в ячейку counter увеличивается и передает ход другу.       
        if counter > 4:                                                                   # Когда уже прошло БОЛЕЕ чем 4 хода то идет проверка победы функцией 
           tmp = check_win(board)                                                         # В переменную tmp берется результат с фунуции check_win                                                                                                           
           if tmp:
              print(tmp, "выиграл!")                                                      # Конкатенирует tmp с текстом
              win = True                                                                  # Меняет буловое значение на True что означает конец игры
              break
        if counter == 9:                                                                  # Проверяет количество пройденых ходов 
            print("Ничья!")                                                               # Если пройдено 9 ходов, а победимель не найден то выводит на экран Ничию
            break
    draw_board(board)
main(board)

input("Нажмите Enter для выхода!")                                                        # При нажадие Enter программа будет завершена.