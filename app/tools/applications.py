import os
import subprocess
import webbrowser
from pathlib import Path
from datetime import datetime


APPLICATIONS = {
    "chrome": [
        r"C:\Program Files\Google\Chrome\Application\chrome.exe",
        r"C:\Program Files (x86)\Google\Chrome\Application\chrome.exe",
    ],
    "vscode": [
        r"C:\Users\%USERNAME%\AppData\Local\Programs\Microsoft VS Code\Code.exe",
        r"C:\Program Files\Microsoft VS Code\Code.exe",
    ],
}


def open_application(name: str) -> str:
    name = name.lower().strip()

    if name == "calculator":
        subprocess.Popen("calc.exe")
        return "Opening Calculator."

    if name == "notepad":
        subprocess.Popen("notepad.exe")
        return "Opening Notepad."

    if name in ["file explorer", "explorer"]:
        subprocess.Popen("explorer.exe")
        return "Opening File Explorer."

    if name in ["command prompt", "cmd"]:
        subprocess.Popen("cmd.exe")
        return "Opening Command Prompt."

    if name == "terminal":
        subprocess.Popen("wt.exe")
        return "Opening Windows Terminal."

    if name in APPLICATIONS:
        for path in APPLICATIONS[name]:
            path = os.path.expandvars(path)

            if os.path.exists(path):
                subprocess.Popen(path)
                return f"Opening {name}."

        return f"I couldn't find {name} on this computer."

    return f"I don't know how to open {name} yet."


def open_folder(folder_name: str) -> str:
    folder_name = folder_name.lower().strip()

    folders = {
        "desktop": Path.home() / "Desktop",
        "downloads": Path.home() / "Downloads",
        "documents": Path.home() / "Documents",
        "pictures": Path.home() / "Pictures",
        "videos": Path.home() / "Videos",
        "music": Path.home() / "Music",
    }

    if folder_name not in folders:
        return f"I don't know the {folder_name} folder."

    folder = folders[folder_name]

    if folder.exists():
        os.startfile(folder)
        return f"Opening {folder_name}."

    return f"I couldn't find your {folder_name} folder."


def open_website(url: str) -> str:
    webbrowser.open(url)
    return f"Opening {url}."


def close_application(name: str) -> str:
    name = name.lower().strip()

    processes = {
        "chrome": "chrome.exe",
        "vscode": "Code.exe",
        "vs code": "Code.exe",
        "notepad": "notepad.exe",
        "calculator": "CalculatorApp.exe",
    }

    if name not in processes:
        return f"I don't know how to close {name} yet."

    process = processes[name]

    subprocess.run(
        ["taskkill", "/IM", process, "/F"],
        capture_output=True,
        text=True
    )

    return f"Closed {name}."


def take_screenshot() -> str:
    try:
        from PIL import ImageGrab

        screenshots_folder = Path.home() / "Pictures" / "JARVIS Screenshots"
        screenshots_folder.mkdir(parents=True, exist_ok=True)

        timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
        file_path = screenshots_folder / f"screenshot_{timestamp}.png"

        screenshot = ImageGrab.grab()
        screenshot.save(file_path)

        return f"Screenshot saved to {file_path}"

    except Exception as error:
        return f"Could not take screenshot: {error}"


def lock_computer() -> str:
    subprocess.run(["rundll32.exe", "user32.dll,LockWorkStation"])
    return "Locking the computer."