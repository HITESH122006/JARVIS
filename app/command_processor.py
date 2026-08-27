from tools.applications import (
    open_application,
    open_folder,
    open_website,
    close_application,
    take_screenshot,
    lock_computer,
)


def process_command(command: str) -> str:
    original_command = command.strip()
    command = original_command.lower()

    # Exit
    if command in ["exit", "quit", "shutdown"]:
        return "EXIT"

    # Open applications
    open_prefixes = [
        "open ",
        "launch ",
        "start ",
        "run ",
    ]

    for prefix in open_prefixes:
        if command.startswith(prefix):
            target = command[len(prefix):].strip()

            websites = {
                "youtube": "https://www.youtube.com",
                "github": "https://github.com",
                "google": "https://www.google.com",
            }

            folders = [
                "desktop",
                "downloads",
                "documents",
                "pictures",
                "videos",
                "music",
            ]

            if target in websites:
                return open_website(websites[target])

            if target in folders:
                return open_folder(target)

            return open_application(target)

    # Close applications
    close_prefixes = [
        "close ",
        "exit ",
        "stop ",
    ]

    for prefix in close_prefixes:
        if command.startswith(prefix):
            target = command[len(prefix):].strip()
            return close_application(target)

    # Screenshot
    screenshot_commands = [
        "take screenshot",
        "take a screenshot",
        "screenshot",
        "capture screen",
    ]

    if command in screenshot_commands:
        return take_screenshot()

    # Lock
    lock_commands = [
        "lock computer",
        "lock my computer",
        "lock pc",
        "lock laptop",
    ]

    if command in lock_commands:
        return lock_computer()

    return "I don't understand that command yet."