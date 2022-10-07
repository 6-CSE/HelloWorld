# Author: Álvaro Masanori Sato

class text_style:
   BOLD = '\033[1m'
   END = '\033[0m'
   RED = '\033[91m'

print(f"\n{text_style.RED}{text_style.BOLD}HELLO WORLD!{text_style.END}\n")
