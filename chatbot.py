while True:
    user_input = input("you:").lower()
    if "hello" in user_input:
        print("Bot: Hi there!")
    elif "how are you" in user_input:
        print("Bot: I'm fine, thanks!")
    elif "bye" in user_input:
        print("Bot: Goodbye!")
        break
    else:
        print("Bot: sorry, I don't understand.")        