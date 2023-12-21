# 19.Определить количество мужчин , севших в порту Квинстаун,
# в возрастном интервале медиана +- 15 позиций и сколько из них выжило
import csv

filename = "train.csv"
mans_age_surv = []

with open(filename, 'r', newline='', encoding='utf-8') as file:
    file_reader = csv.DictReader(file)
    for row in file_reader:
        if row['Embarked'] == 'Q' and row['Sex'] == 'male' and row['Age'] != '' and row['Survived'] != '':
            mans_age_surv.append([float(row['Age']), row['Survived'] == '1'])
sort_mans = sorted(mans_age_surv, key=lambda man: man[0])

median_mans = None
if len(sort_mans) <= 31:                # 31 - количество чисел с медианой +- 15
    median_mans = sort_mans
else:
    n = len(sort_mans)
    index = n // 2
    if n % 2 != 0:
        median_mans = sort_mans[index - 15: index + 15]
    else:
        median_mans = sort_mans[index - 15: index + 16]
survived = 0
for man in median_mans:
    if man[1]:
        survived += 1
print(f'Количество  мужчин, севших в порту Квинстаут : {len(median_mans)}')
print(f'Из них выжило : {survived}')
