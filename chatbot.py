import random

def reply(user):
    user = user.lower()

    if "hello" in user:
        return "Hello!"

    elif "name" in user:
        return "I am Python Chatbot"

    elif "college" in user:
        return "I am your project chatbot"

    elif "how are you" in user:
        return "I am fine"

    elif "bye" in user:
        return "Goodbye"

    else:
        return "I don't understand"


print("Chatbot started (type bye to stop)")

while True:
    user = input("You: ")

    if user.lower() == "bye":
        print("Chatbot: Goodbye")
        break

    print("Chatbot:", reply(user))