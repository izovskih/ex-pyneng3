# -*- coding: utf-8 -*-
'''
Задание 5.1

1. Запросить у пользователя ввод IP-адреса в формате 10.0.1.1
2. Определить какому классу принадлежит IP-адрес.
3. В зависимости от класса адреса, вывести на стандартный поток вывода:
   'unicast' - если IP-адрес принадлежит классу A, B или C
   'multicast' - если IP-адрес принадлежит классу D
   'local broadcast' - если IP-адрес равен 255.255.255.255
   'unassigned' - если IP-адрес равен 0.0.0.0
   'unused' - во всех остальных случаях

Подсказка по классам (диапазон значений первого байта в десятичном формате):
A: 1-127
B: 128-191
C: 192-223
D: 224-239

Ограничение: Все задания надо выполнять используя только пройденные темы.
'''

LB = 0
UA = 0
ipAddr = input('Enter IPv4 address like this X.X.X.X : ').split('.')
if int(ipAddr[0]) in range(1, 224):
    print('Address is unicast')
elif int(ipAddr[0]) in range(224, 240):
    print('Address is multicast')
else:
    for i in ipAddr:
        if int(i) == 255:
            LB += 1
        elif int(i) == 0:
            UA += 1
        else:
            break
    if LB == 4:
        print('Address is Local Broadcast')
    elif UA == 4:
        print('Address is UnAssigned')
    else:
        print('Address is unused')