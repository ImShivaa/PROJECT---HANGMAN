import spacy

# TO LOAD
nlp = spacy.load("en_core_web_sm")

def advanced_spacy_chatbot():
    name = input("Enter your name: ")
    print(f"Chatbot: Welcome, {name}! Ready to chat. Type 'exit' to stop.")
    
    while True:
        user_input = input(f"{name}: ").lower()
        if user_input in ["exit", "bye"]:
            print(f"Chatbot: Thank you for using the chatbot, {name}! Chat again soon.")
            break
        doc = nlp(user_input)
        if any(greeting in user_input for greeting in ["hi", "hello", "heyy", "hiii"]):
            print("Chatbot: Hello! How are you?")
            if input(f"{name}: ").lower() == "how are you":
                print("Chatbot: I'm well!")
        elif "recommend" in user_input:
            print("Chatbot: Have you tried 'The Matrix'? It’s a must-watch!")
        elif "book" in user_input:
            print("Chatbot: Check out 'Sapiens' by Yuval Noah Harari—it’s insightful.")
        elif "weather" in user_input:
            print("Chatbot: I wish I could step outside, but I hope it’s nice!")
        else:
            print("Chatbot: That’s interesting. Can you share more details?")
            
advanced_spacy_chatbot()
