import sys

# Check if 'names' package is installed
try:
    import names
except ImportError:
    print("Installing the 'names' package...")
    subprocess.check_call([sys.executable, "-m", "pip", "install", "names"])
    import names

def main():
    while True:
        try:
            say_num = int(input("How many people would you like me to say \"HELLO\" to? [Enter a number from 1 to 999]: "))
            if 1 <= say_num <= 999:
                break
            else:
                print("Please enter a number between 1 and 999.")
        except ValueError:
            print("Please enter a valid number.")

    for _ in range(say_num):
        print(f"Hello, {names.get_first_name()}!")

if __name__ == "__main__":
    main()

    
