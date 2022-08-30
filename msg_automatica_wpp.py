import pywhatkit as kit

n = int(0)
minu = int(0)
num = [92999999999]

while n < len(num):
    kit.sendwhatmsg(f"+55{num[n]}", "Bom dia!\n\nOlá Cliente!\n\nVimos que sua lista de canais vence daqui a 3 "
                                    "dias.\n\nIremos renovar?", 10, minu)
    n += 1
    minu += 1
