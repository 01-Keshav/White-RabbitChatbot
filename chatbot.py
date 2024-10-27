import nltk
import random
import string

# Download NLTK resources
nltk.download('punkt')
# A simple set of responses
responses = {
    "greeting": ["Hello!", "Hi there!", "Greetings!", "How can I help you?"],
    "farewell": ["Goodbye!", "See you later!", "Take care!"],
    "thanks": ["You're welcome!", "No problem!", "Glad to help!"],
    "unknown": ["I'm not sure I understand.", "Can you rephrase that?", "Let's talk about something else."]
}

# Function to process user input and respond
def respond(user_input):
    user_input = user_input.lower()
    # Tokenize the input
    tokens = nltk.word_tokenize(user_input)
    
    # Check for greetings
    if any(word in tokens for word in ["hello", "hi", "hey"]):
        return random.choice(responses["greeting"])
    
    # Check for farewells
    elif any(word in tokens for word in ["bye", "goodbye", "see you"]):
        return random.choice(responses["farewell"])
    
    # Check for thanks
    elif any(word in tokens for word in ["thank", "thanks", "appreciate"]):
        return random.choice(responses["thanks"])
    
    # Default response for unknown inputs
    else:
        return random.choice(responses["unknown"])

# Main loop for the chatbot
def chat():
    print("Chatbot: Hello! I'm a White Rabbit chatbot. Type 'exit' to end the chat.")
    while True:
        user_input = input("You: ")
        if user_input.lower() == 'exit':
            print("Chatbot: Goodbye! Have a great day!")
            break
        response = respond(user_input)
        print(f"Chatbot: {response}")

# Start the chat
if __name__ == "__main__":
    chat()