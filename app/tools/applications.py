import os
import subprocess
import webbrowser


APPLICATIONS = {
    "chrome": r"C:\Program Files\Google\Chrome\Application\chrome.exe",
    "vscode": r"C:\Users\%USERNAME%\AppData\Local\Programs\Microsoft VS Code\Code.exe",
}


def open_application(name: str) -> str:
    name = name.lower().strip()

    if name == "calculator":
        subprocess.Popen("calc.exe")
        return "Opening Calculator."

    if name == "notepad":
        subprocess.Popen("notepad.exe")
        return "Opening Notepad."

    if name == "file explorer":
        subprocess.Popen("explorer.exe")
        return "Opening File Explorer."

    if name in APPLICATIONS:
        path = os.path.expandvars(APPLICATIONS[name])

        if os.path.exists(path):
            subprocess.Popen(path)
            return f"Opening {name}."

        return f"I couldn't find {name} at the configured location."

    return f"I don't know how to open {name} yet."


def open_website(url: str) -> str:
    webbrowser.open(url)
    return f"Opening {url}."
    