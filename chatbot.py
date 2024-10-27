import re
import random
from collections import defaultdict
import json

class SimpleAIBot:
    def __init__(self):
        # Initialize knowledge base
        self.knowledge_base = {
            "greetings": {
                "patterns": [r"hi|hello|hey|greetings", r"how are you"],
                "responses": ["Hello!", "Hi there!", "Hey! How can I help?", "Greetings!"]
            },
            "farewell": {
                "patterns": [r"bye|goodbye|see you|later"],
                "responses": ["Goodbye!", "See you later!", "Have a great day!"]
            },
            "gratitude": {
                "patterns": [r"thanks|thank you|appreciate"],
                "responses": ["You're welcome!", "Happy to help!", "Anytime!"]
            },
            "name": {
                "patterns": [r"what.*your name|who are you"],
                "responses": ["I'm White rabbit!", "Call me White rabbit", "White rabbit at your service!"]
            }
        }
        
        # Store conversation context
        self.context = defaultdict(str)
        self.last_intent = None

    def load_knowledge(self, filename):
        """Load knowledge base from a JSON file"""
        try:
            with open(filename, 'r') as f:
                self.knowledge_base.update(json.load(f))
            return True
        except Exception as e:
            print(f"Error loading knowledge base: {e}")
            return False

    def save_knowledge(self, filename):
        """Save knowledge base to a JSON file"""
        try:
            with open(filename, 'w') as f:
                json.dump(self.knowledge_base, f, indent=4)
            return True
        except Exception as e:
            print(f"Error saving knowledge base: {e}")
            return False

    def add_knowledge(self, intent, patterns, responses):
        """Add new patterns and responses to the knowledge base"""
        if intent not in self.knowledge_base:
            self.knowledge_base[intent] = {
                "patterns": patterns,
                "responses": responses
            }
        else:
            self.knowledge_base[intent]["patterns"].extend(patterns)
            self.knowledge_base[intent]["responses"].extend(responses)

    def identify_intent(self, message):
        """Match user input against patterns to identify intent"""
        message = message.lower()
        
        for intent, data in self.knowledge_base.items():
            for pattern in data["patterns"]:
                if re.search(pattern, message):
                    return intent
        
        return "unknown"

    def get_response(self, message):
        """Generate a response based on the user's message"""
        intent = self.identify_intent(message)
        self.last_intent = intent
        
        if intent in self.knowledge_base:
            return random.choice(self.knowledge_base[intent]["responses"])
        
        return "I'm not sure how to respond to that. Could you rephrase or ask something else?"

    def chat(self):
        """Start an interactive chat session"""
        print("Bot: Hello! I'm White rabbit. Type 'quit' to exit.")
        
        while True:
            user_input = input("You: ").strip()
            
            if user_input.lower() in ['quit', 'exit', 'bye']:
                print("Bot: Goodbye!")
                break
                
            response = self.get_response(user_input)
            print("Bot:", response)

# Example usage and how to extend the bot
if __name__ == "__main__":
    # Create and initialize the bot
    bot = SimpleAIBot()
    
    # Add custom knowledge
    bot.add_knowledge(
        "weather",
        [r"weather|temperature|forecast"],
        ["I'm sorry, I don't have access to weather information.", 
         "I can't check the weather, but I hope it's nice outside!"]
    )
    
    # Start the chat
    bot.chat()