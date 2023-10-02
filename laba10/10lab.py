from tkinter import *
import random
winning_positions = [
        [[0, 0], [0, 1], [0, 2]],
        [[1, 0], [1, 1], [1, 2]],
        [[2, 0], [2, 1], [2, 2]],
        [[0, 0], [1, 0], [2, 0]],
        [[0, 1], [1, 1], [2, 1]],
        [[0, 2], [1, 2], [2, 2]],
        [[0, 0], [1, 1], [2, 2]],
        [[2, 0], [1, 1], [0, 2]]]
root = None

player_1 = "X"                                  # игрок 1
player_2 = "O"                                  # Компьютер

def game(r, c): # начало игры
    global turns, computer
    if buttons[r][c]['text'] == '':
        buttons[r][c]['text'] = player_1
    else:
        return
    turns += 1
    if winner_check(player_1):
        text_window('Вы победили', 'Игра окончена')
    else:
        if turns != 9:
            turns += 1
            computer_walk()
            if computer == False:
                while True:
                    one = random.randint(0, 2)
                    two = random.randint(0, 2)
                    if buttons[one][two]['text'] == '':
                        buttons[one][two]['text'] = player_2
                        if winner_check(player_2):
                            text_window('Победил компьютер','Игра окончена')
                        break
            computer = False
            if winner_check(player_2):
                text_window('Победил компьютер', 'Игра окончена')
        else:
            text_window('У вас ничья','Игра окончена')

def computer_TF(r, c):  # компьютер уже сделал свой ход
    global computer
    if buttons[r][c]['text'] == '':
        buttons[r][c]['text'] = player_2
    computer = True

def computer_walk():
    global computer
    for r in range(3): # горизонталь
        if buttons[r][0]['text'] == buttons[r][1]['text'] == player_1 and buttons[r][2]["text"] == '':
            computer_TF(r, 2)
            return
        elif buttons[r][1]['text'] == buttons[r][2]['text'] == player_1 and buttons[r][0]["text"] == '':
            computer_TF(r, 0)
            return
        elif buttons[r][0]['text'] == buttons[r][2]['text'] == player_1 and buttons[r][1]['text'] == '':
            computer_TF(r, 1)
            return

    for r in range(3):   # вертикаль
        if buttons[0][r]['text'] == buttons[1][r]['text'] == player_1 and buttons[2][r]["text"] == '':
            computer_TF(2, r)
            return
        elif buttons[1][r]['text'] == buttons[2][r]['text'] == player_1 and buttons[0][r]['text'] == '':
            computer_TF(0, r)
            return
        elif buttons[0][r]['text'] == buttons[2][r]['text'] == player_1 and buttons[1][r]['text'] == '':
            computer_TF(1, r)
            return

    if buttons[0][0]['text'] == buttons[1][1]['text'] == player_1 and buttons[2][2]['text'] == '': # диагональ
        computer_TF(2, 2)
        return
    elif buttons[1][1]['text'] == buttons[2][2]['text'] == player_1 and buttons[0][0]['text'] == '':
        computer_TF(0, 0)
        return
    elif buttons[0][0]['text'] == buttons[2][2]['text'] == player_1 and buttons[1][1]['text'] == '':
        computer_TF(1, 1)
        return
    elif buttons[0][2]['text'] == buttons[1][1]['text'] == player_1 and buttons[2][0]['text'] == '':
        computer_TF(2, 0)
        return
    elif buttons[2][0]['text'] == buttons[1][1]['text'] == player_1 and buttons[0][2]['text'] == '':
        computer_TF(0, 2)
        return
    elif buttons[2][0]['text'] == buttons[0][2]['text'] == player_1 and buttons[1][1]['text'] == '':
        computer_TF(1, 1)
        return
    while True:
        r = random.choice([[0, 0], [2, 2], [2, 0], [0, 2]])
        if buttons[r[0]][r[1]]['text'] == '':
            computer_TF(r[0],r[1])
            return

def winner_check(player):
    for line in winning_positions:
        win = True
        for coord in line:
            if buttons[coord[0]][coord[1]]['text'] != player:
                win = False
                break
        if win:
            return True
    return False

def new_game(window):
    global root, buttons, turns, computer
    if root != None:
        root.destroy()
    if window != None:
        window.destroy()
    root = Tk()
    root.title("Крестики-нолики")
    root.geometry("320x300")
    root.eval('tk::PlaceWindow . center')
    buttons = [[], [], []]  # кнопки
    turns = 0
    computer =  False

    for c in range(3): root.columnconfigure(index=c, weight=1)
    for r in range(3): root.rowconfigure(index=r, weight=1)
    for r in range(3):
        for c in range(3):
            btn = Button(text='', font="Arial 14", width=106, command=lambda row=r, column=c: game(row, column))
            buttons[r].append(btn)
            btn.grid(row=r, column=c, sticky="nsew")

def text_window(message, title):  # функция для вывода текста об ошибке
    window = Tk()
    window.title(title)
    Label(window, font="Arial 14", width=30, height=3, text=message).pack()
    window.eval('tk::PlaceWindow . center')
    Button(window, text='Новая игра', font="Arial 14", width=20, command = lambda: new_game(window)).pack()

new_game(None)
root.mainloop()