# 1. Написать программу, удаляющую из 
# текста все слова содержащие "абв".

#my_text = 'Напишите абв абв програабвмму, удаляющую из \
    #этого абв текста все абвс слова, содерабващие содержащие "а б в"'

#def del_some_words(my_text):
   # my_text = list(filter(lambda x: 'абв' not in x, my_text.split()))
   # return " ".join(my_text)

#my_text = del_some_words(my_text)
#print(my_text)
# Задача №2: Создайте программу для игры с конфетами человек против человека. 

#from random import randint

#def input_dat(name):
    #x = int(input(f"{name}, введите количество конфет, которое возьмете от 1 до 28: "))
    #while x < 1 or x > 28:
     #   x = int(input(f"{name}, введите корректное количество конфет: "))
    #return x

#
#def p_print(name, k, counter, value):
    #print(f"Ходил {name}, он взял {k}, теперь у него {counter}. Осталось на столе {value} конфет.")

#player1 = input("Введите имя первого игрока: ")
#player2 = input("Введите имя второго игрока: ")
#value = int(input("Введите количество конфет на столе: "))
#flag = randint(0,2)
#if flag:
   # print(f"Первый ходит {player1}")
#else:
 #   print(f"Первый ходит {player2}")

#counter1 = 0 
#counter2 = 0

#while value > 28:
    #if flag:
       # k = input_dat(player1)
       # counter1 += k
       # value -= k
       # flag = False
       # p_print(player1, k, counter1, value)
   # else:
      #  k = input_dat(player2)
      #  counter2 += k
      #  value -= k
      #  flag = True
      #  p_print(player2, k, counter2, value)

#if flag:
  #  print(f"Выиграл {player1}")
#else:
  #  print(f"Выиграл {player2}")

 
 #Задача №3  Создать программу для игры в ""Крестики-нолики""
# maps = [1,2,3,
#         4,5,6,
#         7,8,9]
 

# victories = [[0,1,2],
#              [3,4,5],
#              [6,7,8],
#              [0,3,6],
#              [1,4,7],
#              [2,5,8],
#              [0,4,8],
#              [2,4,6]]
 

# def print_maps():
#     print(maps[0], end = " ")
#     print(maps[1], end = " ")
#     print(maps[2])
 
#     print(maps[3], end = " ")
#     print(maps[4], end = " ")
#     print(maps[5])
 
#     print(maps[6], end = " ")
#     print(maps[7], end = " ")
#     print(maps[8])    
 

# def step_maps(step,symbol):
#     ind = maps.index(step)
#     maps[ind] = symbol
 
# def get_result():
#     win = ""
 
#     for i in victories:
#         if maps[i[0]] == "X" and maps[i[1]] == "X" and maps[i[2]] == "X":
#             win = "X"
#         if maps[i[0]] == "O" and maps[i[1]] == "O" and maps[i[2]] == "O":
#             win = "O"   
             
#     return win
 

# game_over = False
# player1 = True
 
# while game_over == False:
 
   
#     print_maps()
 
#     if player1 == True:
#         symbol = "X"
#         step = int(input("Gamer1, ваш ход: "))
#     else:
#         symbol = "O"
#         step = int(input("Gamer2, ваш ход: "))
 
#     step_maps(step,symbol) 
#     win = get_result() 
#     if win != "":
#         game_over = True
#     else:
#         game_over = False
 
#     player1 = not(player1)        
        
# print_maps()
# print("Победил", win)
# Задача №4: Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления данных. Входные и выходные данные хранятся в отдельных текстовых файлах. Пример:




# def coding(txt):
#     count = 1
#     res = ''
#     for i in range(len(txt)-1):
#         if txt[i] == txt[i+1]:
#             count += 1
#         else:
#             res = res + str(count) + txt[i]
#             count = 1
#     if count > 1 or (txt[len(txt)-2] != txt[-1]):
#         res = res + str(count) + txt[-1]
#     return res

# def decoding(txt):
#     number = ''
#     res = ''
#     for i in range(len(txt)):
#         if not txt[i].isalpha():
#             number += txt[i]
#         else:
#             res = res + txt[i] * int(number)
#             number = ''
#     return res


# s = input("Введите текст для кодировки: ")
# print(f"Текст после кодировки: {coding(s)}")
# print(f"Текст после дешифровки: {decoding(coding(s))}")
