# -*- coding: utf-8 -*-
'''
Задание 6.2b

Дополнить скрипт из задания 6.2a:
* вместо вывода на стандартный поток вывода,
  скрипт должен записать полученные строки в файл config_sw1_cleared.txt

При этом, должны быть отфильтрованы строки, которые содержатся в списке ignore.
Строки, которые начинаются на '!' отфильтровывать не нужно.

Ограничение: Все задания надо выполнять используя только пройденные темы.

'''

ignore = ['duplex', 'alias', 'Current configuration']

from sys import argv

fileName = argv[1]
iItem = True
lsStrs = []
with open(fileName) as f:
    for line in f:
        for i in ignore:
            if i in line:
                iItem = False
                break
            else:
                iItem = True
                continue
        if iItem == True:
            lsStrs.append(line)
        else:
            continue
with open('config_sw1_cleared.txt', 'w') as fw:
    fw.writelines(lsStrs)
