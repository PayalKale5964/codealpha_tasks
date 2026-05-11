# Simple Chatbot Project using Python

print("===== Welcome to Simple Chatbot =====")
print("Type 'bye' to exit")

while True:
    
    # Taking input from user
    user = input("You: ").lower()

    # Chatbot responses
    if user == "hello":
        print("Bot: Hi! Nice to meet you.")

    elif user == "how are you":
        print("Bot: I am doing great!")

    elif user == "what is your name":
        print("Bot: My name is Python Chatbot.")

    elif user == "have you eaten something":
        print("Bot: Yes! I had data for breakfast.")

    elif user == "who made you":
        print("Bot: I was created using Python.")

    elif user == "bye":
        print("Bot: Goodbye! Have a nice day.")
        break

    else:
        print("Bot: Sorry, I don't understand that.")
