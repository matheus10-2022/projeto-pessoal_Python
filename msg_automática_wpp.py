import pywhatkit as kit
import pyautogui as auto
import os
from time import sleep

n = int(0)
hora, minu = int(14), int(22)
num = [92984914894,
       92996177035

       ]  # Usar dia 27/12

while n < len(num):
    kit.sendwhatmsg(f"+55{num[n]}", "Boa tarde!\n\nOlá Cliente!\n\nVimos que sua lista de canais vence daqui a 3 "
                                    "dias.\n\nIremos renovar?", hora, minu)
    n += 1
    minu += 1
    sleep(12)
    auto.click(1234, 18)
    auto.hotkey("alt", "f4")  # Fecha a aba

print('Desligando pc...')
sleep(6)
# os.system("shutdown /s /t 1")  # Desliga o computador
