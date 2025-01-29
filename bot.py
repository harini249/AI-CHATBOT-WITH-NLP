import nltk
from nltk.chat.util import Chat, reflections

# Define some basic patterns and responses related to Python programming
pairs = [
    (r"Hi|Hello|Hey", ["Hello! How can I assist you with Python programming today?"]),
    (r"How do I install Python?", ["You can download Python from the official website: https://www.python.org/downloads/"]),
    (r"How do I declare a variable in Python?", ["In Python, you declare a variable simply by assigning a value: `x = 5`"]),
    (r"How do I define a function?", ["You can define a function using the `def` keyword: `def my_function():`"]),
    (r"(.*) (list|tuple|dictionary) (.*)", ["In Python, lists are defined with square brackets: `[1, 2, 3]`, tuples with parentheses: `(1, 2, 3)`, and dictionaries with curly braces: `{key: value}`"]),
    (r"How do I handle errors in Python?", ["You can handle errors using `try-except` blocks like this: `try: ... except: ...`"]),
    (r"Explain Python's OOP concept", ["Python supports object-oriented programming (OOP). You can define classes and objects to structure your code using inheritance, encapsulation, and polymorphism."]),
    (r"(.*) (exit|quit|bye)", ["Goodbye! Happy coding with Python!"]),
]

# Create a chatbot with these pairs
chatbot = Chat(pairs, reflections)

# Function to start the chat
def start_chat():
    print("Chatbot: Hello! Type 'exit' to end the chat.")
    while True:
        user_input = input("You: ")
        if user_input.lower() in ['exit', 'quit', 'bye']:
            print("Chatbot: Goodbye!")
            break
        response = chatbot.respond(user_input)
        print(f"Chatbot: {response}")

# Start the chatbot
if __name__ == "__main__":
    start_chat()
