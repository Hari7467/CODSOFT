import re
def chatbot():
    print("Hello! I'm a simple chatbot. How can I help you today?")
    
    while True:
        user_input = input("You: ").lower()  

        if 'bye' in user_input or 'exit' in user_input:
            print("Goodbye! Have a great day!")
            break
        
        elif 'hello' in user_input or 'hi' in user_input:
            print("Chatbot: Hello! How are you?")
        
        elif 'how are you' in user_input:
            print("Chatbot: I'm just a bot, but I'm doing great! Thanks for asking!")
        
        elif 'name' in user_input:
            print("Chatbot: I'm a chatbot created by a developer!")
        
        elif 'time' in user_input:
            from datetime import datetime
            now = datetime.now()
            print(f"Chatbot: The current time is {now.strftime('%H:%M:%S')}")
        
        elif 'joke' in user_input:
            print("Chatbot: Why don't skeletons fight each other? They don't have the guts!")
        
        else:
            print("Chatbot: I'm sorry, I didn't understand that. Can you try asking something else?")
            
chatbot()
