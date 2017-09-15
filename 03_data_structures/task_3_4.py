# -*- coding: utf-8 -*-
'''
Задание 3.4

Из строк command1 и command2 получить список VLANов,
которые есть и в команде command1 и в команде command2.

Для данного примера, результатом должен быть список: [1, 3, 100]
Этот список содержит подсказку по типу итоговых данных.

Ограничение: Все задания надо выполнять используя только пройденные темы.

'''

command1 = 'switchport trunk allowed vlan 1,3,10,20,30,100'
command2 = 'switchport trunk allowed vlan 1,3,100,200,300'

# commands = [command1.split(),command2.split()]
# command1 = set(commands[0][-1].split(','))
# command2 = set(commands[1][-1].split(','))
# print(list(command1.intersection(command2)))

print(list(set(command1.split()[-1].split(',')).intersection(set(command2.split()[-1].split(',')))))
