from data.texts import mainMenu_md
from core.entry_creator import startCreator

from rich.prompt import Prompt # type: ignore
from rich.console import Console # type: ignore
from rich.markdown import Markdown # pyright: ignore[reportMissingImports]

console = Console()

def mainMenu():
    console.print(Markdown(mainMenu_md), style="green")

    option = Prompt.ask("🕴️Where to, boss?", choices=["1", "2", "3"], default="1")
    match option:
        case '1':
            startCreator()
        case '2':
            print('Not sure how to help ya mate')
            input("")
            mainMenu()
        case '3':
            print('Exiting program... Goodbye!')
        case _:
            print('Invalid Input!')


# MAIN LOGIC
def main():
    mainMenu()

main()