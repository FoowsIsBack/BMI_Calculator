import os
import time

def clear():
    if os.system == 'nt':
        os.system('cls')
    else:
        os.system('clear')

def main():
    clear()
    print(f"""╔════════════════╗
║ BMI Calculator ║
╠════════════════╣
║ 1. Calculate   ║
║ 2. Status      ║
║ 0. Exit        ║
╚════════════════╝""")    
    choice = int(input("Choice: "))

    if choice == 1:
        calculate()
    elif choice == 0:
        exit() 


def calculate():
    clear()
    global weight, height
    print("════════════════")
    print("BMI Calculator")
    print("════════════════")
    weight = int(input("Weight: "))
    height = int(input("Height: "))
    print("════════════════")
    time.sleep(2)





def result():
    pass




def exit():
    time.sleep(1)
    clear()
    print("Thank You!")



main()