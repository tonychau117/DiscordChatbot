import random

def get_response(message: str) -> str:
    pMessage = message.lower()

    if pMessage == "hello":
        return "Hey!"
    
    if pMessage == "roll":
        return str(random.randint(1,6))
    
    if pMessage == "!help":
        return "HELLLPPPPPPPPPPPPPP"
    
    else:
        return "I'm sorry, I don't understand. Use '!help' if you need clairification"