import tkinter as tk


def reply(user):
    user = user.lower()

    if "hello" in user:
        return "Hello!"

    elif "name" in user:
        return "I am Python Chatbot"

    elif "how are you" in user:
        return "I am fine"

    elif "college" in user:
        return "I am your project chatbot"

    elif "python" in user:
        return "Python is a programming language"

    elif "bye" in user:
        return "Goodbye"

    else:
        return "I don't understand"


def send():
    user = entry.get()

    if user == "":
        return

    chat.config(state=tk.NORMAL)

    chat.insert(tk.END, "You: " + user + "\n", "user")
    bot = reply(user)
    chat.insert(tk.END, "Bot: " + bot + "\n\n", "bot")

    chat.config(state=tk.DISABLED)

    entry.delete(0, tk.END)
    chat.see(tk.END)


window = tk.Tk()
window.title("AI Chatbot Project")
window.geometry("500x600")
window.config(bg="#2c3e50")


chat = tk.Text(window,
               bg="#ecf0f1",
               font=("Arial", 12),
               state=tk.DISABLED)

chat.tag_config("user", foreground="blue")
chat.tag_config("bot", foreground="green")

scroll = tk.Scrollbar(window, command=chat.yview)
chat.config(yscrollcommand=scroll.set)

chat.pack(padx=10, pady=10, fill=tk.BOTH, expand=True)
scroll.pack(side=tk.RIGHT, fill=tk.Y)


entry = tk.Entry(window, font=("Arial", 14))
entry.pack(padx=10, pady=10, fill=tk.X)


button = tk.Button(window,
                   text="Send",
                   font=("Arial", 12),
                   bg="#27ae60",
                   fg="white",
                   command=send)

button.pack(pady=5)


window.mainloop()