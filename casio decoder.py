try:
    # Python2
    import Tkinter as tk
except ImportError:
    # Python3
    import tkinter as tk

from decimal import Decimal

r = tk.Tk()
r.withdraw()
    
input = r.clipboard_get()

if "http://wes.casio.com/math/index.php" in input and "+R-" in input:

    index = input.find("+R-")
    best_bit = input[index+4:]
    best_bit = best_bit[:19]
    
    number = best_bit[:15]
    number = Decimal(number[0] + "." + number[1:])
    multsign = int(best_bit[16]) in [1,6]
    sign = int(best_bit[16]) not in [5,6]
    mult = int(best_bit[17:])
    if not multsign:
        mult = 100 - mult
    #    multsign = -1
    #number_out = number * (10**(multsign * mult))
    for i in range(mult):
        if multsign:
            number = number * 10
        else:
            number = number / 10
    if not sign:
        number = 0 - number
    if number == int(number) and 'e' not in str(number):
        number = int(number)
    try:
        print(number.normalize())
    except:
        print(number)
    
    try:
        if number == int(number):
            number = int(number)
    except:
        pass
    try:
        print(number.normalize())
    except:
        print(number)

    r = tk.Tk()
    r.withdraw()
    r.clipboard_clear()
    r.clipboard_append(number)
    r.update() # now it stays on the clipboard after the window is closed
    r.destroy()
else:
    print("Not a valid Casio URL")