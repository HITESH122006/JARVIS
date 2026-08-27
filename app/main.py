from command_processor import process_command


def main():
    print("=" * 55)
    print("             JARVIS DESKTOP v1.0")
    print("=" * 55)
    print("Type a command or 'exit' to quit.\n")

    while True:
        command = input("You: ").strip()

        if not command:
            continue

        response = process_command(command)

        if response == "EXIT":
            print("JARVIS: Shutting down. Goodbye.")
            break

        print(f"JARVIS: {response}")


if __name__ == "__main__":
    main()