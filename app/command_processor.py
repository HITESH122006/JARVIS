from tools.applications import open_application, open_website


def process_command(command: str) -> str:
    command = command.lower().strip()

    if command.startswith("open "):
        target = command[5:].strip()

        websites = {
            "youtube": "https://www.youtube.com",
            "github": "https://github.com",
            "google": "https://www.google.com",
        }

        if target in websites:
            return open_website(websites[target])

        return open_application(target)

    if command in ["exit", "quit", "shutdown"]:
        return "EXIT"

    return "I don't understand that command yet."