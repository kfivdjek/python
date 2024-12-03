'''Шестнадцатеричные четные числа, у которых 5я справа цифра равна В. Составить и вывести 
словами частотный словарь цифр.'''
f = open('3.txt', 'r')
d={
    '0': 0,
    '1': 0,
    '2': 0,
    '3': 0,
    '4': 0,
    '5': 0,
    '6': 0,
    '7': 0,
    '8': 0,
    '9': 0,
    'A': 0,
    'B': 0,
    'C': 0,
    'D': 0,
    'E': 0,
    'F': 0
}
s = f.readline().split()
while s!=[]:
    for i in s:
        i = i.upper()
        try: int(i,16)
        except: continue
        else:
            if len(i)>4:
                if i[-5]=='B' and int(i,16)%2==0: 
                    print(i)
                    for sym in i:
                        if sym!='-' and sym!='+': d[sym]+=1
                    dole = sum(d.values())/100
    s = f.readline().split()
for key in d: print(f'Частота появления {key} в искомых числах равна {dole*d[key]}')
