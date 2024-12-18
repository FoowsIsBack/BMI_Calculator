#dave.py

#Color
#Border = \x1b[1;36m
#Title = \x1b[1;33m
#Text = \x1b[1;32m
#Command = \x1b[1;37m
#Back = \x1b[1;37m

import os
import time
import math

def clear():
    if os.system == 'nt':
        os.system('cls')
    else:
        os.system('clear')

def add():
    global num1, num2, result
    print(f""" 
    \x1b[1;36m╔═════════════════════════╗
    \x1b[1;36m║        \x1b[1;33mADDITION         \x1b[1;36m║
    \x1b[1;36m╚═════════════════════════╝""")
    num1 = int(input("     \x1b[1;32mNum1:\x1b[1;37m "))
    num2 = int(input("     \x1b[1;32mNum2:\x1b[1;37m "))
    result = num1 + num2
    time.sleep(1)
    clear()
    add_result()

def add_result():
    print(f""" 
    \x1b[1;36m╔═════════════════════════╗
    \x1b[1;36m║     \x1b[1;31mADDITION RESULT     \x1b[1;36m║
    \x1b[1;36m╠═════════════════════════╣
    \x1b[1;36m║       \x1b[1;32mNum1 = \x1b[1;37m{num1:<10} \x1b[1;36m║
    \x1b[1;36m║       \x1b[1;32mNum2 = \x1b[1;37m{num2:<10} \x1b[1;36m║
    \x1b[1;36m║       \x1b[1;32mTotal = \x1b[1;37m{result:<10}\x1b[1;36m║
    \x1b[1;36m╚═════════════════════════╝""")
    choice = input("     \x1b[1;31mPress Enter to Go Back:\x1b[1;37m ")
    time.sleep(1)
    main()

def sub():
    global num1, num2, result
    print(f""" 
    \x1b[1;36m╔═════════════════════════╗
    \x1b[1;36m║       \x1b[1;33mSUBTRACTION       \x1b[1;36m║
    \x1b[1;36m╚═════════════════════════╝""")
    num1 = int(input("     \x1b[1;32mNum1:\x1b[1;37m "))
    num2 = int(input("     \x1b[1;32mNum2:\x1b[1;37m "))
    result = num1 - num2
    time.sleep(1)
    clear()
    sub_result()

def sub_result():
    print(f""" 
    \x1b[1;36m╔═════════════════════════╗
    \x1b[1;36m║    \x1b[1;31mSUBTRACTION RESULT   \x1b[1;36m║
    \x1b[1;36m╠═════════════════════════╣
    \x1b[1;36m║       \x1b[1;32mNum1 = \x1b[1;37m{num1:<10} \x1b[1;36m║
    \x1b[1;36m║       \x1b[1;32mNum2 = \x1b[1;37m{num2:<10} \x1b[1;36m║
    \x1b[1;36m║       \x1b[1;32mTotal = \x1b[1;37m{result:<10}\x1b[1;36m║
    \x1b[1;36m╚═════════════════════════╝""")
    choice = input("     \x1b[1;31mPress Enter to Go Back:\x1b[1;37m ")
    time.sleep(1)
    main()

def mult():
    global num1, num2, result
    print(f""" 
    \x1b[1;36m╔═════════════════════════╗
    \x1b[1;36m║      \x1b[1;33mMULTIPLICATION     \x1b[1;36m║
    \x1b[1;36m╚═════════════════════════╝""")
    num1 = int(input("     \x1b[1;32mNum1:\x1b[1;37m "))
    num2 = int(input("     \x1b[1;32mNum2:\x1b[1;37m "))
    result = num1 * num2
    time.sleep(1)
    clear()
    mult_result()

def mult_result():
    print(f""" 
    \x1b[1;36m╔═════════════════════════╗
    \x1b[1;36m║  \x1b[1;31mMULTIPLICATION RESULT  \x1b[1;36m║
    \x1b[1;36m╠═════════════════════════╣
    \x1b[1;36m║       \x1b[1;32mNum1 = \x1b[1;37m{num1:<10} \x1b[1;36m║
    \x1b[1;36m║       \x1b[1;32mNum2 = \x1b[1;37m{num2:<10} \x1b[1;36m║
    \x1b[1;36m║       \x1b[1;32mTotal = \x1b[1;37m{result:<10}\x1b[1;36m║
    \x1b[1;36m╚═════════════════════════╝""")
    choice = input("     \x1b[1;31mPress Enter to Go Back:\x1b[1;37m ")
    time.sleep(1)
    main()       

def div():
    global num1, num2, result
    print(f""" 
    \x1b[1;36m╔═════════════════════════╗
    \x1b[1;36m║        \x1b[1;33mDIVISION         \x1b[1;36m║
    \x1b[1;36m╚═════════════════════════╝""")
    num1 = int(input("     \x1b[1;32mNum1:\x1b[1;37m "))
    num2 = int(input("     \x1b[1;32mNum2:\x1b[1;37m "))
    result = num1 / num2
    time.sleep(1)
    clear()
    div_result()

def div_result():
    print(f""" 
    \x1b[1;36m╔═════════════════════════╗
    \x1b[1;36m║     \x1b[1;31mDIVISION RESULT     \x1b[1;36m║
    \x1b[1;36m╠═════════════════════════╣
    \x1b[1;36m║       \x1b[1;32mNum1 = \x1b[1;37m{num1:<10} \x1b[1;36m║
    \x1b[1;36m║       \x1b[1;32mNum2 = \x1b[1;37m{num2:<10} \x1b[1;36m║
    \x1b[1;36m║       \x1b[1;32mTotal = \x1b[1;37m{result:<10.5f}\x1b[1;36m║
    \x1b[1;36m╚═════════════════════════╝""")
    choice = input("     \x1b[1;31mPress Enter to Go Back:\x1b[1;37m ")
    time.sleep(1)
    main()  

def qroot():
    global num1, result
    print(f""" 
    \x1b[1;36m╔═════════════════════════╗
    \x1b[1;36m║       \x1b[1;33mSQUARE ROOT       \x1b[1;36m║
    \x1b[1;36m╚═════════════════════════╝""")
    num1 = int(input("     \x1b[1;32mNum1:\x1b[1;37m "))
    result = math.sqrt(num1)
    time.sleep(1)
    clear()
    qroot_result()

def qroot_result():
    print(f""" 
    \x1b[1;36m╔═════════════════════════╗
    \x1b[1;36m║    \x1b[1;31mSQUARE ROOT RESULT   \x1b[1;36m║
    \x1b[1;36m╠═════════════════════════╣
    \x1b[1;36m║       \x1b[1;32mNum1 = \x1b[1;37m{num1:<10} \x1b[1;36m║
    \x1b[1;36m║       \x1b[1;32mQroot = \x1b[1;37m{result:<10.4f}\x1b[1;36m║
    \x1b[1;36m╚═════════════════════════╝""")
    choice = input("     \x1b[1;31mPress Enter to Go Back:\x1b[1;37m ")
    time.sleep(1)
    clear()
    shift_mode()  

def asmd():
    global num1, num2, result, result1, result2, result3
    print(f""" 
    \x1b[1;36m╔═════════════════════════╗
    \x1b[1;36m║  \x1b[1;33mALL IN ONE CALCULATOR  \x1b[1;36m║
    \x1b[1;36m╚═════════════════════════╝""")
    num1 = int(input("     \x1b[1;32mNum1:\x1b[1;37m "))
    num2 = int(input("     \x1b[1;32mNum2:\x1b[1;37m "))
    result = num1 + num2
    result1 = num1 - num2
    result2 = num1 * num2
    result3 = num1 / num2
    time.sleep(1)
    clear()
    asmd_result()

def asmd_result():
    print(f""" 
    \x1b[1;36m╔═════════════════════════╗
    \x1b[1;36m║    \x1b[1;31mALL IN ONE RESULT    \x1b[1;36m║
    \x1b[1;36m╠═════════════════════════╣
    \x1b[1;36m║       \x1b[1;32mNum1 = \x1b[1;37m{num1:<10} \x1b[1;36m║
    \x1b[1;36m║       \x1b[1;32mNum2 = \x1b[1;37m{num2:<10} \x1b[1;36m║
    \x1b[1;36m╠═════════════════════════╣
    \x1b[1;36m║       \x1b[1;32mAdd = \x1b[1;37m{result:<10}  \x1b[1;36m║
    \x1b[1;36m║       \x1b[1;32mSub = \x1b[1;37m{result1:<10}  \x1b[1;36m║
    \x1b[1;36m║       \x1b[1;32mMult = \x1b[1;37m{result2:<10} \x1b[1;36m║
    \x1b[1;36m║       \x1b[1;32mDiv = \x1b[1;37m{result3:<10}  \x1b[1;36m║
    \x1b[1;36m╚═════════════════════════╝""")
    choice = input("     \x1b[1;31mPress Enter to Go Back:\x1b[1;37m ")
    time.sleep(1)
    main()

def exponent():
    global num1, num2, result
    print(f""" 
    \x1b[1;36m╔═════════════════════════╗
    \x1b[1;36m║     \x1b[1;33mRAISED TO POWER     \x1b[1;36m║
    \x1b[1;36m╚═════════════════════════╝""")
    num1 = int(input("     \x1b[1;32mBase:\x1b[1;37m "))
    num2 = int(input("     \x1b[1;32mExponent:\x1b[1;37m "))
    result = math.pow(num1, num2)
    time.sleep(1)
    clear()
    exponent_result()

def exponent_result():
    print(f""" 
    \x1b[1;36m╔═════════════════════════╗
    \x1b[1;36m║ \x1b[1;32m{num1} \x1b[1;33mRAISED TO POWER OF \x1b[1;32m{num2} \x1b[1;36m║
    \x1b[1;36m╠═════════════════════════╣
    \x1b[1;36m║      \x1b[1;32mNum1 = \x1b[1;37m{num1:<10}  \x1b[1;36m║
    \x1b[1;36m║      \x1b[1;32mNum2 = \x1b[1;37m{num2:<10}  \x1b[1;36m║
    \x1b[1;36m║      \x1b[1;32mResult = \x1b[1;37m{result:<10.0f}\x1b[1;36m║
    \x1b[1;36m╚═════════════════════════╝""")
    choice = input("     \x1b[1;31mPress Enter to Go Back:\x1b[1;37m ")
    time.sleep(1)
    clear()
    shift_mode()  

def factorial():
    global num1, result
    print(f""" 
    \x1b[1;36m╔═════════════════════════╗
    \x1b[1;36m║        \x1b[1;33mFACTORIAL        \x1b[1;36m║
    \x1b[1;36m╚═════════════════════════╝""")
    num1 = int(input("     \x1b[1;32mNum1:\x1b[1;37m "))
    result = math.factorial(num1)
    time.sleep(1)
    clear()
    factorial_result()

def factorial_result():
    print(f""" 
    \x1b[1;36m╔═════════════════════════╗
    \x1b[1;36m║     \x1b[1;31mFACTORIAL RESULT    \x1b[1;36m║
    \x1b[1;36m╠═════════════════════════╣
    \x1b[1;36m║      \x1b[1;32mNum1 = \x1b[1;37m{num1:<10}  \x1b[1;36m║
    \x1b[1;36m║      \x1b[1;32mResult = \x1b[1;37m{result:<10}\x1b[1;36m║    
    \x1b[1;36m╚═════════════════════════╝""")
    choice = input("     \x1b[1;31mPress Enter to Go Back:\x1b[1;37m ")
    time.sleep(1)
    clear()
    shift_mode()

def ncr():
    global num1, num2, result
    print(f""" 
    \x1b[1;36m╔═════════════════════════╗
    \x1b[1;36m║        \x1b[1;33mnCr METHODS      \x1b[1;36m║
    \x1b[1;36m╚═════════════════════════╝""")
    num1 = int(input("     \x1b[1;32mNum1:\x1b[1;37m "))
    num2 = int(input("     \x1b[1;32mNum2:\x1b[1;37m "))
    result = math.comb(num1, num2)
    time.sleep(1)
    clear()
    ncr_result()    

def ncr_result():
    print(f""" 
    \x1b[1;36m╔═════════════════════════╗
    \x1b[1;36m║        \x1b[1;31mnCr RESULT       \x1b[1;36m║
    \x1b[1;36m╠═════════════════════════╣
    \x1b[1;36m║      \x1b[1;32mNum1 = \x1b[1;37m{num1:<10}  \x1b[1;36m║
    \x1b[1;36m║      \x1b[1;32mNum2 = \x1b[1;37m{num2:<10}  \x1b[1;36m║
    \x1b[1;36m║      \x1b[1;32mResult = \x1b[1;37m{result:<10}\x1b[1;36m║    
    \x1b[1;36m╚═════════════════════════╝""")
    choice = input("     \x1b[1;31mPress Enter to Go Back:\x1b[1;37m ")
    time.sleep(1)
    clear()
    shift_mode()

def modulus():
    global num1, num2, result
    print(f""" 
    \x1b[1;36m╔═════════════════════════╗
    \x1b[1;36m║         \x1b[1;33mMODULUS         \x1b[1;36m║
    \x1b[1;36m╚═════════════════════════╝""")
    num1 = int(input("     \x1b[1;32mNum1:\x1b[1;37m\x1b[1;37m "))
    num2 = int(input("     \x1b[1;32mNum2:\x1b[1;37m\x1b[1;37m "))
    result = num1 % num2
    time.sleep(1)
    clear()
    modulus_result()
 
def modulus_result():
    print(f""" 
    \x1b[1;36m╔═════════════════════════╗
    \x1b[1;36m║      \x1b[1;31mMODULUS RESULT     \x1b[1;36m║
    \x1b[1;36m╠═════════════════════════╣
    \x1b[1;36m║      \x1b[1;32mNum1 = \x1b[1;37m{num1:<10}  \x1b[1;36m║
    \x1b[1;36m║      \x1b[1;32mNum2 = \x1b[1;37m{num2:<10}  \x1b[1;36m║
    \x1b[1;36m║      \x1b[1;32mResult = \x1b[1;37m{result:<10}\x1b[1;36m║    
    \x1b[1;36m╚═════════════════════════╝""")
    choice = input("     \x1b[1;31mPress Enter to Go Back:\x1b[1;37m ")
    time.sleep(1)
    clear()
    shift_mode()

def shift_mode():
    print(f""" 
    \x1b[1;36m╔═════════════════════════╗
    \x1b[1;36m║       \x1b[1;33mSHIFT MODE        \x1b[1;36m║
    \x1b[1;36m╠═════════════════════════╣
    \x1b[1;36m║  \x1b[1;32m1.   Square root       \x1b[1;36m║
    \x1b[1;36m║  \x1b[1;32m2.   Exponent          \x1b[1;36m║  
    \x1b[1;36m║  \x1b[1;32m3.   Factorial         \x1b[1;36m║   
    \x1b[1;36m║  \x1b[1;32m4.   nCr               \x1b[1;36m║
    \x1b[1;36m║  \x1b[1;32m5.   Modulus           \x1b[1;36m║
    \x1b[1;36m║  \x1b[1;31m0.   Back              \x1b[1;36m║
    \x1b[1;36m╚═════════════════════════╝""")
    choice = int(input("     \x1b[1;33mChoice:\x1b[1;37m "))
    time.sleep(1)
    clear()

    if choice == 1:
        qroot()
    elif choice == 2:
        exponent()
    elif choice == 3:
        factorial()
    elif choice == 4:
        ncr()
    elif choice == 5:
        modulus()
    elif choice == 0:
        main()
    else:
        print(f""" 
        \x1b[1;36m╔═════════════════════════╗
        \x1b[1;36m║      \x1b[1;32mInvalid Input!     \x1b[1;36m║
        \x1b[1;36m╚═════════════════════════╝""")
        time.sleep(1.5)
        clear()
        shift_mode()

def main():
    clear()
    print(f""" 
    \x1b[1;36m╔═════════════════════════╗
    \x1b[1;36m║  \x1b[1;33mSCIENTIFIC CALCULATOR  \x1b[1;36m║
    \x1b[1;36m╠═════════════════════════╣
    \x1b[1;36m║  \x1b[1;32m1.   Addition          \x1b[1;36m║
    \x1b[1;36m║  \x1b[1;32m2.   Subtraction       \x1b[1;36m║
    \x1b[1;36m║  \x1b[1;32m3.   Multiplication    \x1b[1;36m║
    \x1b[1;36m║  \x1b[1;32m4.   Division          \x1b[1;36m║
    \x1b[1;36m║  \x1b[1;32m5.   All in One        \x1b[1;36m║
    \x1b[1;36m║  \x1b[1;32m6.   Shift-Mode        \x1b[1;36m║    
    \x1b[1;36m║  \x1b[1;31m0.   Exit              \x1b[1;36m║
    \x1b[1;36m╚═════════════════════════╝""")
    choice = int(input("     \x1b[1;33mChoice:\x1b[1;37m "))
    time.sleep(1)
    clear()

    if choice == 1:
        add()
    elif choice == 2:
        sub()
    elif choice == 3:
        mult()
    elif choice == 4:
        div()
    elif choice == 5:
        asmd()
    elif choice == 6:
        shift_mode()
    elif choice == 0:
        clear()
        print(f""" 
        \x1b[1;36m╔═════════════════════════╗
        \x1b[1;36m║      \x1b[1;32mBye bye bye...     \x1b[1;36m║
        \x1b[1;36m╚═════════════════════════╝""")
        time.sleep(1.5)
    else:
        print(f""" 
        \x1b[1;36m╔═════════════════════════╗
        \x1b[1;36m║      \x1b[1;32mInvalid Input!     \x1b[1;36m║
        \x1b[1;36m╚═════════════════════════╝""")
        time.sleep(1.5)
        main()

main()