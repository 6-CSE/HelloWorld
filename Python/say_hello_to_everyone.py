
import subprocess
import sys

# check exists package
try:
    import names
except ImportError:
    subprocess.check_call([sys.executable, "-m", "pip", "install", "names"])
    import names

while 1 > 0:
    try:
        say_num = int(input("How many who would you like me to say \"HELLO\" to ? [ENTER NUMBER 1-999]:"))
        if say_num <= 0:
            print("Please enter number more then 0")
            continue
        break
    except ValueError:
        print("Please enter number !")
        continue

while say_num > 0:
    print(f"Hello! {names.get_first_name()}")
    say_num = say_num - 1
    