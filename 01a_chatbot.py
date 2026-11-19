# Question: Demonstrate a simple chatbot with a minimum of 10 conversations.
"""A small rule-based chatbot that supports at least ten conversation intents."""
import re

RULES = [
    (r"\b(hi|hello|hey|holla|hola)\b", "Hello! How can I help you?"),
    (r"\bwhat is your name\b", "I'm AIML Bot."),
    (r"\bhow are you\b", "I'm doing well, thanks for asking."),
    (r"\bwhere are you from\b", "I live in this Python program."),
    (r"\bwhat do you do\b", "I answer simple questions using pattern matching."),
    (r"\bwho created you\b", "I was created as an AIML lab exercise."),
    (r"\bwhat is ai\b", "AI is the study of systems that perform tasks associated with intelligence."),
    (r"\bwhat is machine learning\b", "Machine learning lets computers learn patterns from data."),
    (r"\bthank(s| you)\b", "You're welcome!"),
    (r"\bbye|goodbye\b", "Goodbye!"),
]

def reply(message: str) -> str:
    text = message.lower().strip()
    for pattern, answer in RULES:
        if re.search(pattern, text):
            return answer
    return "I don't know that one yet. Try asking about AI or machine learning."

def main() -> None:
    print("AIML Lab Chatbot (type 'bye' to exit)")
    while True:
        message = input("You: ")
        print("Bot:", reply(message))
        if re.search(r"\b(bye|goodbye)\b", message.lower()):
            break

if __name__ == "__main__":
    main()
