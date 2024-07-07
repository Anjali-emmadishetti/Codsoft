# Simple rule-based chatbot
def chatbot_response(user_input):
    # Convert user input to lowercase to handle case-insensitive matching
    user_input = user_input.lower()

    # Predefined responses based on user input
    if 'hello' in user_input:
        return "Hello! How can I assist you today?"
    elif 'how are you' in user_input:
        return "I'm just a bot, but I'm doing great! How about you?"
    elif 'name' in user_input:
        return "I am a simple chatbot created to assist you."
    elif 'help' in user_input:
        return "Sure! I'm here to help. What do you need assistance with?"
    elif 'bye' in user_input:
        return "Goodbye! Have a great day!"
    else:
        return "I'm sorry, I didn't understand that. Can you please rephrase?"

# Main loop to keep the chatbot running
def main():
    print("Chatbot: Hi there! Type 'bye' to exit the chat.")
    while True:
        # Get user input
        user_input = input("You: ")
        
        # Exit the chat if the user types 'bye'
        if 'bye' in user_input.lower():
            print("Chatbot: Goodbye! Have a great day!")
            break
        
        # Get chatbot response
        response = chatbot_response(user_input)
        
        # Print chatbot response
        print("Chatbot:", response)

# Run the main loop
if __name__ == "__main__":
    main()

