# pip install rich

from rich import print

def hello_world():
    print("[bold][green]Hello[/green],[yellow] World![/yellow][/bold]")

if __name__ == "__main__":
    hello_world()
else:
    print("[red]This is not the main module[/red]")