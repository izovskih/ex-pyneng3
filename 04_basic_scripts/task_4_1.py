# -*- coding: utf-8 -*-
'''
Задание 4.1

Запросить у пользователя ввод IP-сети в формате: 10.1.1.0/24

Затем вывести информацию о сети и маске в таком формате:

Network:
10        1         1         0
00001010  00000001  00000001  00000000

Mask:
/24
255       255       255       0
11111111  11111111  11111111  00000000

Проверить работу скрипта на разных комбинациях сеть/маска.

Ограничение: Все задания надо выполнять используя только пройденные темы.
'''

Net,Mask = input('Enter network address and mask in format X.X.X.X/XX: ').split('/')
Net = Net.split('.')

print('Network:')
print(''.join('{:10}'.format(i) for i in Net))
print(''.join('{:10}'.format(bin(int(j))[2:].zfill(8)) for j in Net))
print('\nMask:')
print('/' + Mask)

ind = '1'*(32-(32-int(Mask)))
ind = ''.join('{0:<032}'.format(ind))
Mask = [ind[i:i+8] for i in range(0, len(ind), 8)]

print(''.join('{:<10}'.format(int(j, 2)) for j in Mask))
print(''.join('{:10}'.format(i) for i in Mask))
