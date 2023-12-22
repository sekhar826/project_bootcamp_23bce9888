print("Hello! I'm your interactive conversation chatbot. Let's chat!")

while True:
    user_input = input("You: ").lower()

    if "exit" in user_input:
        print("Chatbot: Goodbye! It was nice chatting with you.")
        break
    elif "propose" in user_input:
        print("Chatbot: Oh, that's unexpected! I'm just a program, so I'm afraid I can't accept proposals. Let's keep chatting.")
    elif "love" in user_input or "marry" in user_input:
        print("Chatbot: I appreciate the sentiment, but I'm not capable of love or marriage. Let's continue our conversation.")
    else:
        print("Chatbot: I enjoy our conversation! If you have any other topics in mind, feel free to share.")
