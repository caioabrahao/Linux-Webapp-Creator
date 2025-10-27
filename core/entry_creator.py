import os, sys, time
from pathlib import Path

# sobe um nível e adiciona ao sys.path
parent_dir = Path(__file__).resolve().parent.parent
sys.path.append(str(parent_dir))

from .input_sanitization import sanitize_url
from data.texts import successMessage

from rich.progress import track
from rich import print
from rich.console import Console
from rich.markdown import Markdown

console = Console()

#USER VARIABLES
app_name='null'
app_url='null'
app_comment=''
app_categories=[]
app_keywords=[]

#PROGRAM VARIABLES
directory = os.path.expandvars('$HOME/.local/share/applications/')

def create_file():
    desktop_entry = f'''
    [Desktop Entry]
    Type=Application

    Name={app_name}
    Exec=brave --app={app_url} --user-data-dir={directory}/webapp_sessions/{app_name.lower()}_session
    Icon={app_name}

    Comment={app_comment}

    Categories={app_categories}
    Keywords={app_keywords}

    NoDisplay=false
    '''

    for i in track(range(1), description="✨ Creating Desktop File..."):
        time.sleep(1)  # Simulate work just to give it some flair

    with open(f'{directory}{app_name}.desktop', 'w') as f:
        f.write(desktop_entry)

    successMessage_md = successMessage(directory, app_name)
    console.print(Markdown(successMessage_md), style="yellow")

    os.chmod(f'{directory}{app_name}.desktop', 0o755) # Make it executable, just in case
    exit()


def ask_creation_data():
    global app_name, app_url, app_comment, app_keywords, app_categories

    # ASK FOR THE NAME
    print("[blue bold]Lets create your Webapp! [/blue bold] \nFirst we need a name.\n")
    app_name = input("➡️ App Name: ")

    #ASK FOR THE URL
    print("Now tell me the URL... \n")
    input_url = input("➡️ App URL: ")
    app_url = sanitize_url(input_url)

    #ASK FOR A COMMENT - OPTIONAL
    print("Wanna add an app comment? \n")
    app_comment = input("➡️ App Comment: ")

    #ASK FOR A CATEGORY - OPTIONAL
    print("What category is the app? (eg: Gaming, Messaging, Coding, etc...) \n[grey50 italic]Write nothing to skip [/grey50 italic]")
    app_categories = input("➡️ App Category: ")


# MAIN LOGIC
def startCreator():
    ask_creation_data()

    print("Great! Creating your desktop app...")
    create_file()