import openai
import json

# Load OpenAI API key from config file
with open('config.json') as config_file:
    config = json.load(config_file)
    openai.api_key = config["openai_api_key"]

def generate_response(prompt):
    # Use the OpenAI API to generate a response
    response = openai.Completion.create(
        engine="text-davinci-002",  # You can experiment with different engines
        prompt=prompt,
        max_tokens=150,  # Adjust the response length as needed
        temperature=0.7  # Higher values make the output more random, lower values make it more deterministic
    )
    
    return response.choices[0].text.strip()

# Main loop for the chat application
print("Welcome to ChatGPT!")
while True:
    user_input = input("You: ")
    
    if user_input.lower() == 'exit':
        print("Goodbye!")
        break
    
    prompt = f"You: {user_input}\nChatGPT:"
    response = generate_response(prompt)
    
    print(f"ChatGPT: {response}")

#JLdp
