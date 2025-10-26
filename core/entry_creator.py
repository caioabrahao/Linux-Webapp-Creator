import os

#USER VARIABLES
app_name='appname'
app_url='appurl'
app_comment=''

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

    Categories=;
    Keywords=;

    NoDisplay=false
    '''

    with open(f'{directory}{app_name}.desktop', 'w') as f:
        f.write(desktop_entry)
    print("File Created!")
    os.chmod(f'{directory}{app_name}.desktop', 0o755)
    exit()

def sanitize_url(raw_url):
    raw_url = raw_url.strip()
    if raw_url.startswith("https://"):
        raw_url = raw_url.replace('https://', "")
    elif raw_url.startswith('http://'):
        raw_url = raw_url.replace('http://', "")
    
    full_url = f'https://{raw_url}'
    return full_url


def ask_creation_data():
    global app_name, app_url, app_comment

    print("Lets create your Webapp! \nFirst we need a name.\n")
    app_name = input("App Name: ")

    print("Now tell me the URL... \n")
    input_url = input("App URL: ")
    app_url = sanitize_url(input_url)

    print("Wanna add an app comment? \n")
    app_comment = input("App Comment: ")

    print("Great! Creating your desktop app...")
    create_file()


# MAIN LOGIC
def startCreator():
    ask_creation_data()