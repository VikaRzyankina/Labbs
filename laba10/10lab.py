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
root = Tk()
root.title("Крестики-нолики")
root.geometry("320x300")
root.eval('tk::PlaceWindow . center')
player_1 = "X"                                  # игрок 1
player_2 = "O"                                  # Компьютер
buttons = [[], [], []]                          # кнопки
turns = 0
computer = False                                # проверка, сделал ли компьютер ход

for c in range(3): root.columnconfigure(index=c, weight=1)
for r in range(3): root.rowconfigure(index=r, weight=1)

for r in range(3):
    for c in range(3):
        btn = Button(text="", font = "Arial 14", width = 106, command=lambda row=r, column=c: game(row, column))
        buttons[r].append(btn)
        btn.grid(row = r, column = c, sticky = "nsew")

def game(r, c): # начало игры
    global turns
    turns += 1
    buttons[r][c]['text'] = player_1
    if winner_check(player_1):
        text_window('Вы победили', 'Игра окончена')
    else:
        if turns != 9:
            while True:
                one = random.randint(0, 2)
                two = random.randint(0, 2)
                if buttons[one][two]['text'] == '':
                    buttons[one][two]['text'] = player_2
                    if winner_check(player_2):
                        text_window('Победил компьютер','Игра окончена')
                    break
        else:
            text_window('У вас ничья','Игра окончена')


def computer_walk(player_1,player_2):
    global computer, turns
    for i in range(3):
        if buttons[i][0]["text"] == buttons[i][1]["text"] == player_1 and buttons[i][2]["text"] == "":
            turns += 1
            buttons[i][2]["text"] = player_2
            break

def winner_check(player):
    for line in winning_positions:
        win = True
        for coord in line:
            if buttons[coord[0]][coord[1]]['text'] != player:
                win =  False
                break
        if win:
            return True
    return  False



def text_window(message, title = None):  # функция для вывода текста об ошибке
    window = Tk()
    if title != None:
        window.title(title)
    else:
        window.title('Ошибка')
    Label(window, font=14, text=message).pack()
    window.eval('tk::PlaceWindow . center')

root.mainloop()