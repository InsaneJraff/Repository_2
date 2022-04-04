import time


def aa():
    a = input("Wpisz swoje imie: \n")
    print(f'Siema {a}')

def godzina():
    t = time.localtime()
    current_time = time.strftime('%H:%M:%S', t)
    print('jest godzina ', current_time)

aa()
godzina()