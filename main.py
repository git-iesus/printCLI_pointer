import pyautogui as patg
from time import sleep
import os
modulo = 0

#1. INTRODUÇÃO

os.system('cls')  # Limpa o terminal usando o comando cls
print('Bem vindo ao PrintCLI POINTER *****')
print('-------------------------------------------------------')
print('Escolha o módulo que você deseja imprimir:')
print('1) Boletins')
print('2) Identificações')
modulo = str(input())

while modulo != 1 and modulo !=2:
    print('!!! OPÇÃO INCORRETA')
    print('Escolha o módulo que você deseja imprimir:')
    print('1) Boletins')
    print('2) Identificações')
    modulo = str(input())


#2. COLETA DE INFORMAÇÕES


if modulo == 1:
    print('Digite as quantidades que deseja imprimir:')
    print('-------------------------------------------------------')
    b1 = str(input('VIBROKRAFT:'))
    b2 = str(input('ESTRECHADEIRA:'))
    b3 = str(input('ABAST. INTERNO:'))
    b4 = str(input('ABAST. EXTERNO:'))
    b5 = str(input('PÓ DO SECADOR:'))
else:
    print('Digite as quantidades que deseja imprimir:')
    print('-------------------------------------------------------')
    i1 = str(input('CLASSIFICAÇÃO:'))
    i2 = str(input('MISTURA:'))
    i3 = str(input('MOINHO:'))
    i4 = str(input('PÓ:'))
    i5 = str(input('VARREDURA:'))





# patg.hotkey('winleft','r')
# sleep(0.5)
# patg.write("C:\\Users\\iesus.candido_petfiv\\Desktop\\GitHub\\printgui_apontamento\\indexsheet.pdf")
# sleep(0.1)
# patg.press('enter')
# sleep(1)

# if i1 == '0': #CLASSIFICAÇÃO
#     pass
# else:
#     patg.hotkey('ctrl','p')
#     sleep(2)
#     patg.press('tab')
#     patg.press('tab')
#     patg.press('tab')
#     patg.press('tab')
#     patg.press('tab')
#     patg.press('tab')
#     sleep(0.3)
#     patg.press('down')
#     patg.press('down')
#     patg.press('down')
#     sleep(0.5)
#     patg.write('1')
#     patg.press('tab')
#     sleep(0.3)
#     patg.write(i1)
#     sleep(0.2)
#     patg.press('enter')

# if i2 == '0': #MISTURA
#     pass
# else:
#     patg.hotkey('ctrl','p')
#     sleep(2)
#     patg.press('tab')
#     patg.press('tab')
#     patg.press('tab')
#     patg.press('tab')
#     patg.press('tab')
#     patg.press('tab')
#     sleep(0.3)
#     patg.press('down')
#     patg.press('down')
#     patg.press('down')
#     sleep(0.5)
#     patg.write('2')
#     patg.press('tab')
#     sleep(0.3)
#     patg.write(i2)
#     sleep(0.2)
#     patg.press('enter')

# if i3 == '0': #MOINHO
#     pass
# else:
#     patg.hotkey('ctrl','p')
#     sleep(2)
#     patg.press('tab')
#     patg.press('tab')
#     patg.press('tab')
#     patg.press('tab')
#     patg.press('tab')
#     patg.press('tab')
#     sleep(0.3)
#     patg.press('down')
#     patg.press('down')
#     patg.press('down')
#     sleep(0.5)
#     patg.write('3')
#     patg.press('tab')
#     sleep(0.3)
#     patg.write(i3)
#     sleep(0.2)
#     patg.press('enter')

# if i4 == '0': #PÓ
#     pass
# else:
#     patg.hotkey('ctrl','p')
#     sleep(2)
#     patg.press('tab')
#     patg.press('tab')
#     patg.press('tab')
#     patg.press('tab')
#     patg.press('tab')
#     patg.press('tab')
#     sleep(0.3)
#     patg.press('down')
#     patg.press('down')
#     patg.press('down')
#     sleep(0.5)
#     patg.write('4')
#     patg.press('tab')
#     sleep(0.3)
#     patg.write(i4)
#     sleep(0.2)
#     patg.press('enter')

# if i5 == '0': #VARREDURA
#     pass
# else:
#     patg.hotkey('ctrl','p')
#     sleep(2)
#     patg.press('tab')
#     patg.press('tab')
#     patg.press('tab')
#     patg.press('tab')
#     patg.press('tab')
#     patg.press('tab')
#     sleep(0.3)
#     patg.press('down')
#     patg.press('down')
#     patg.press('down')
#     sleep(0.5)
#     patg.write('5')
#     patg.press('tab')
#     sleep(0.3)
#     patg.write(i5)
#     sleep(0.2)
#     patg.press('enter')
    
# patg.alert('PrintCLI IDENTIFICAÇÕES!')