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
    elif choice == 2:
        status()
    elif choice == 0:
        exit() 

def calculate():
    clear()
    global weight, height
    print("════════════════")
    print("BMI Calculator")
    print("════════════════")
    weight = float(input("Weight: "))
    height = float(input("Height: "))
    print("════════════════")
    time.sleep(2)
    result()

def result():
    global weight, height, bmi
    bmi = weight / height**2
    if bmi <= 18.4:
        Underweight()
    elif 18.5 <= bmi <= 24.9:
        Normal()
    elif 25.0 <= bmi <= 39.9:
        Overweight()
    elif 40.0 > bmi:
        Obese()

def Underweight():
    clear()
    print("════════════════")
    print("   BMI Result")
    print("════════════════")
    print(f"{bmi:.2f} = Underweight")
    print("")
    text = input("Press any key to continue . . . ")
    main()

def Normal():
    clear()
    print("════════════════")
    print("   BMI Result")
    print("════════════════")
    print(f"{bmi:.1f} = Normal")
    print("")
    text = input("Press any key to continue . . . ")
    main()

def Overweight():
    clear()
    print("════════════════")
    print("   BMI Result")
    print("════════════════")
    print(f"{bmi:.1f} = Overweight")
    print("")
    text = input("Press any key to continue . . . ")
    main()

def Obese():
    clear()
    print("════════════════")
    print("   BMI Result")
    print("════════════════")
    print(f"{bmi:.1f} = Obese")
    print("")
    text = input("Press any key to continue . . . ")
    main()

def status():
    clear()
    print(f"""╔══════════════════════════════════╗
║           BMI Status             ║
╠══════════════════════════════════╣
║ 1. < 18.4       -  Underweight   ║
║ 2. 18.5 - 24.9  -  Normal        ║
║ 3. 25.0 - 39.9  -  Overweight    ║     
║ 4. > 40.0       -  Obese         ║
║ 0. Exit                          ║
╚══════════════════════════════════╝""")
    text = input("Press any key to exit . . . ")
    time.sleep(2)
    main()

def exit():
    time.sleep(1)
    clear()
    print("Thank You!")

main()
