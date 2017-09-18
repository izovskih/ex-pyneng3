# -*- coding: utf-8 -*-
'''
Задание 5.1a

Сделать копию скрипта задания 5.1.

Дополнить скрипт:
- Добавить проверку введенного IP-адреса.
- Адрес считается корректно заданным, если он:
   - состоит из 4 чисел разделенных точкой,
   - каждое число в диапазоне от 0 до 255.

Если адрес задан неправильно, выводить сообщение:
'Incorrect IPv4 address'

Ограничение: Все задания надо выполнять используя только пройденные темы.

'''

LB = 0
UA = 0
IP = True
ipAddr = input('Enter IPv4 address like this X.X.X.X : ').split('.')
if len(ipAddr) == 4:
    try:
        for i in ipAddr:
            if 0 <= int(i) <= 255:
                if int(i) == 255:
                    LB += 1
                elif int(i) == 0:
                    UA += 1
                else:
                    continue
            else:
                IP = False
                break
        if IP == True:
            if int(ipAddr[0]) in range(1, 224):
                print('Address is unicast')
            elif int(ipAddr[0]) in range(224, 240):
                print('Address is multicast')
            elif LB == 4:
                print('Address is Local Broadcast')
            elif UA == 4:
                print('Address is UnAssigned')
            else:
                print('Address is unused')
        else:
            print('Incorrect IPv4 address  Limit')
    except ValueError:
        print('Incorrect IPv4 address ValueError')
else:
    print('Incorrect IPv4 address')
