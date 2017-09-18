# -*- coding: utf-8 -*-
'''
Задание 6.2a

Сделать копию скрипта задания 6.2.

Дополнить скрипт:
  Скрипт не должен выводить команды, в которых содержатся слова,
  которые указаны в списке ignore.

Ограничение: Все задания надо выполнять используя только пройденные темы.

'''

ignore = ['duplex', 'alias', 'Current configuration']

from sys import argv
fileName = argv[1]
iItem = True
with open(fileName) as f:
    for line in f:
        for i in ignore:
            if i in line or line.startswith('!'):
                iItem = False
                break
            else:
                iItem = True
                continue
        if iItem == True:
            print(line.strip())
        else:
            continue