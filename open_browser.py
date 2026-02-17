import webbrowser

def open_browser(instruction):
    if ('open' in instruction) or ('browser' in instruction):
        if ('python' in instruction):
            webbrowser.open('https://www.python.org/')
        elif ('google' in instruction):
            webbrowser.open('https://www.google.com/')
        elif ('facebook' in instruction):
            webbrowser.open('https://www.facebook.com/')
        elif ('skylight' in instruction):
            webbrowser.open('https://www.robotevents.com/teams/V5RC/20850S')
    else:
        print("instruction not recognized please include 'open', 'python' and 'browser' in your instruction")

if __name__ == "__main__":
    instruction = input("Enter a website to open: ")
    open_browser(instruction)