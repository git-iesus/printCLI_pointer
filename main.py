import pyautogui as patg
from time import sleep
import os
modulo = 0

b1 = '0'
b2 = '0'
b2 = '0'
b3 = '0'
b4 = '0'
b5 = '0'
i1 = '0'
i2 = '0'
i3 = '0'
i4 = '0'
i5 = '0'

# FUNÇÃO LIMPAR TERMINAL
def limpar_terminal():
    os.system('cls' if os.name == 'nt' else 'clear')

# FUNÇÃO IMPRIMIR
def imprimir():
    sleep(1)
    patg.hotkey('ctrl','p')
    sleep(1)
    patg.press('tab')
    patg.press('tab')
    patg.press('tab')
    patg.press('tab')
    patg.press('tab')
    patg.press('tab')
    patg.press('down')
    patg.press('down')
    patg.press('down')
    sleep(1)



#1. INTRODUÇÃO

os.system('cls')  # Limpa o terminal usando o comando cls
print('Bem vindo ao PrintCLI POINTER *****')
print('-------------------------------------------------------')
print('Escolha o módulo que você deseja imprimir:')
print('1) Boletins')
print('2) Identificações')
modulo = int(input())


#2. COLETA DE INFORMAÇÕES

while modulo != 1 and modulo != 2:
    limpar_terminal()
    print('Opção inválida. Por favor, escolha 1 ou 2.')
    print('-------------------------------------------------------')
    print('Escolha o módulo que você deseja imprimir:')
    print('1) Boletins')
    print('2) Identificações')
    modulo = int(input())


if modulo == 1:
    limpar_terminal()
    print('Digite os BOLETINS que deseja imprimir:')
    print('-------------------------------------------------------')
    b1 = str(input('VIBROKRAFT:'))
    b2 = str(input('ESTRECHADEIRA:'))
    b3 = str(input('ABAST. INTERNO:'))
    b4 = str(input('ABAST. EXTERNO:'))
    b5 = str(input('PÓ DO SECADOR:'))
else:
    limpar_terminal()
    print('Digite as IDENTIFICAÇÕES que deseja imprimir:')
    print('-------------------------------------------------------')
    i1 = str(input('CLASSIFICAÇÃO:'))
    i2 = str(input('MISTURA:'))
    i3 = str(input('MOINHO:'))
    i4 = str(input('PÓ:'))
    i5 = str(input('VARREDURA:'))


#3. EXECUÇÃO


patg.hotkey('winleft','r')
sleep(0.5)
patg.write('C:\\Users\\iesus.candido_petfiv\\Desktop\\GitHub\\printCLI_pointer\\merged_docs.pdf')
sleep(0.5)
patg.press('enter')
sleep(0.5)


#4.1 FUNÇÃO: BOLETINS


if b1 == '0':
    pass
else:
    imprimir()

    patg.write('1-3')    #---MODIFICAR INTERVALO
    sleep(0.5)
    patg.press('tab')
    sleep(0.5)
    patg.write(b1)       #---MODIFICAR VARIÁVEL 
    sleep(0.5)
    patg.press('enter')

if b2 == '0':
    pass
else:
    imprimir()

    patg.write('4-5')    #---MODIFICAR INTERVALO
    sleep(0.5)
    patg.press('tab')
    sleep(0.5)
    patg.write(b2)       #---MODIFICAR VARIÁVEL 
    sleep(0.5)
    patg.press('enter')

if b3 == '0':
    pass
else:
    imprimir()

    patg.write('6-7')    #---MODIFICAR INTERVALO
    sleep(0.5)
    patg.press('tab')
    sleep(0.5)
    patg.write(b3)       #---MODIFICAR VARIÁVEL 
    sleep(0.5)
    patg.press('enter')

if b4 == '0':
    pass
else:
    imprimir()

    patg.write('8')    #---MODIFICAR INTERVALO
    sleep(0.5)
    patg.press('tab')
    sleep(0.5)
    patg.write(b4)       #---MODIFICAR VARIÁVEL 
    sleep(0.5)
    patg.press('enter')

if b5 == '0':
    pass
else:
    imprimir()

    patg.write('9')    #---MODIFICAR INTERVALO
    sleep(0.5)
    patg.press('tab')
    sleep(0.5)
    patg.write(b5)       #---MODIFICAR VARIÁVEL 
    sleep(0.5)
    patg.press('enter')


#4.2 FUNÇÃO: IDENTIFICAÇÕES


if i1 == '0':
    pass
else:
    imprimir()

    patg.write('10')    #---MODIFICAR INTERVALO
    sleep(0.5)
    patg.press('tab')
    sleep(0.5)
    patg.write(i1)       #---MODIFICAR VARIÁVEL 
    sleep(0.5)
    patg.press('enter')

if i2 == '0':
    pass
else:
    imprimir()

    patg.write('11')    #---MODIFICAR INTERVALO
    sleep(0.5)
    patg.press('tab')
    sleep(0.5)
    patg.write(i2)       #---MODIFICAR VARIÁVEL 
    sleep(0.5)
    patg.press('enter')

if i3 == '0':
    pass
else:
    imprimir()

    patg.write('12')    #---MODIFICAR INTERVALO
    sleep(0.5)
    patg.press('tab')
    sleep(0.5)
    patg.write(i3)       #---MODIFICAR VARIÁVEL 
    sleep(0.5)
    patg.press('enter')

if i4 == '0':
    pass
else:
    imprimir()

    patg.write('13')    #---MODIFICAR INTERVALO
    sleep(0.5)
    patg.press('tab')
    sleep(0.5)
    patg.write(i4)       #---MODIFICAR VARIÁVEL 
    sleep(0.5)
    patg.press('enter')

if i5 == '0':
    pass
else:
    imprimir()

    patg.write('14')    #---MODIFICAR INTERVALO
    sleep(0.5)
    patg.press('tab')
    sleep(0.5)
    patg.write(i5)       #---MODIFICAR VARIÁVEL 
    sleep(0.5)
    patg.press('enter')

match modulo:
    case 1:
        patg.alert('printCLI: Boletins impressos com sucesso!')
    case 2:
        patg.alert('printCLI: Identificações impressas com sucesso!')