# -*- coding: utf-8 -*-
'''
Задание 4.1b

Преобразовать скрипт из задания 4.1a таким образом,
чтобы сеть/маска не запрашивались у пользователя,
а передавались как аргумент скрипту.

Ограничение: Все задания надо выполнять используя только пройденные темы.

'''

from sys import argv
argParam = argv[1:]
addrStr,cidrStr = ''.join(argParam).split('/')
addr = addrStr.split('.')
mask = [0, 0, 0, 0]
for i in range(int(cidrStr)):
    mask[i//8] = mask[i//8] + (1 << (7 - i % 8))
net = []
for i in range(4):
    net.append(int(addr[i]) & mask[i])
print('Network:')
print(''.join('{:<10}'.format(i) for i in net))
print(''.join('{:10}'.format(bin(int(i))[2:].zfill(8)) for i in net))
print('\nMask:')
print('/' + cidrStr)
print(''.join('{:<10}'.format(int(i)) for i in mask))
print(''.join('{:10}'.format(bin(int(i))[2:].zfill(8)) for i in mask))
