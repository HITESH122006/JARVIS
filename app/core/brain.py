import ollama


class JarvisBrain:
    def __init__(self):
        self.model = "llama3.2:3b"

        self.messages = [
            {
                "role": "system",
                "content": """
You are JARVIS, an intelligent AI desktop assistant.

Your personality:
- Intelligent
- Calm
- Professional
- Helpful
- Concise

Your responsibilities:
- Understand what the user wants.
- Reason about the user's request.
- Give useful suggestions when appropriate.
- Ask questions when important information is missing.
- Never claim that you performed an action unless the system
  actually performed it.

You are currently operating in conversation-only mode.
Later you will receive tools that allow you to control the
user's computer.
"""
            }
        ]

    def ask(self, user_input: str) -> str:

        self.messages.append({
            "role": "user",
            "content": user_input
        })

        response = ollama.chat(
            model=self.model,
            messages=self.messages
        )

        answer = response["message"]["content"]

        self.messages.append({
            "role": "assistant",
            "content": answer
        })

        return answer