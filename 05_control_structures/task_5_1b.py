# -*- coding: utf-8 -*-
'''
Задание 5.1b

Сделать копию скрипта задания 5.1a.

Дополнить скрипт:
Если адрес был введен неправильно, запросить адрес снова.

Ограничение: Все задания надо выполнять используя только пройденные темы.
'''

ipC = False
ipStr = input('Enter IPv4 address like this X.X.X.X : ')
ipLs = ipStr.split('.')
while not ipC:
    try:
        if len(ipLs) != 4 or (not ((0 <= int(ipLs[0]) <= 255) and (0 <= int(ipLs[1]) <= 255) and
(0 <= int(ipLs[2]) <= 255) and (0 <= int(ipLs[3]) <= 255))):
            ipStr = input('Incorrect IPv4 address. Enter IPv4 address again : ')
            ipLs = ipStr.split('.')
        elif 1 <= int(ipLs[0]) <= 223:
            print('Address is unicast')
            ipC = True
        elif 224 <= int(ipLs[0]) <=239:
            print('Address is multicast')
            ipC = True
        elif ipStr == '255.255.255.255':
            print('Address is Local Broadcast')
            ipC = True
        elif ipStr == '0.0.0.0':
            print('Address is UnAssigned')
            ipC = True
        else:
            print('Address is unused')
            ipC = True
    except ValueError:
        ipStr = input('Incorrect IPv4 address. Enter IPv4 address again : ')
        ipLs = ipStr.split('.')