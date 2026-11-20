import os
import aiml

def main():
    kernel = aiml.Kernel()
    
    if os.path.exists("prac1_symptom_rules.aiml"):
        kernel.learn("prac1_symptom_rules.aiml")
    elif os.path.exists("flu.aiml"):
        kernel.learn("flu.aiml")
    else:
        print("Error: AIML file not found!")
        return

    print("Harshwardhan Chauhan 26K4HIT003")
    print("Welcome to the flu diag center")
    
    while True:
        user_input = input("You: ").strip().lower()
        if user_input == 'exit':
            print("Goodbye!")
            break
        response = kernel.respond(user_input)
        print("Expert System: " + response)

if __name__ == "__main__":
    main()
