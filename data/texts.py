# MAIN MENU 
mainMenu_md = """ 
# 🐧 Linux Webapp Creator | by [caioabrahao](https://github.com/caioabrahao)

1. Start Creator
2. Help
3. Exit
"""

# FILE CREATED SUCCESS MESSAGE
def successMessage(directory, app_name):
    createFileSuccess_md = f"""
    # File Created!
    ## File created at `{directory}{app_name}.desktop`
    """
    return createFileSuccess_md
