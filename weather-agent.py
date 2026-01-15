from langchain.agents import create_agent
from dotenv import load_dotenv
import os
import json
import sys

load_dotenv()
# api_key = os.getenv("OPENAI_API_KEY") # Safer, returns None if not found
# print(api_key)

def get_weather(city: str) -> str:
    """Get weather for a given city."""
    return f"It's always sunny in {city}!"

def get_temperature(city: str) -> str:
    """Get temperature for a given city."""
    return f"It's always warm and high temperature in {city}!"    

agent = create_agent(
    model="gpt-4o-mini",
    tools=[get_weather, get_temperature],
    system_prompt="You are a helpful assistant",
)

def main(args):
    # args is a list of the command-line arguments (excluding the script name)
    print("Welcome to the AI chat! Type 'exit' to end the conversation.")

    while True:
        human_message = input("You: ")
        if human_message.lower() == 'exit':
            print("Goodbye!")
            break
        result = agent.invoke(
            {"messages": [{"role": "user", "content":human_message}]}
        )
        if "messages" in result:
            print (result)
            response = result["messages"][-1].content if result["messages"] else None
            print(f"Response: {response}")
        else:
            print("Full result:")
            print(json.dumps(result, indent=2, default=str))


if __name__ == "__main__":
    # Pass all arguments *except* the script name to the main function
    main(sys.argv[1:]) 