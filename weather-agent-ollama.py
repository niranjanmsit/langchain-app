from ollama import chat

def get_temperature(city: str) -> str:
  """Get the current temperature for a city
  
  Args:
    city: The name of the city

  Returns:
    The current temperature for the city
  """
  temperatures = {
    'New York': '22°C',
    'London': '15°C',
  }
  return temperatures.get(city, 'Unknown')

available_functions = {
  'get_temperature': get_temperature,
}
messages = [{'role': 'user', 'content': "What is the temperature in New York?"}]
# directly pass the function as part of the tools list
response = chat(model='qwen3:4b', messages=messages, tools=available_functions.values(), think=True)
print  (response)
# add the assistant message to the messages
messages.append(response.message)
if response.message.tool_calls:
    print('tool call required by llm');
  # process each tool call 
    for call in response.message.tool_calls:
    # execute the appropriate tool
        if call.function.name == 'get_temperature':
            result = get_temperature(**call.function.arguments)
        # elif call.function.name == 'get_conditions':
        #   result = get_conditions(**call.function.arguments)
        else:
            result = 'Unknown tool'
        # add the tool result to the messages
        messages.append({'role': 'tool',  'tool_name': call.function.name, 'content': str(result)})
print("after tool call")

print(messages)
# def main(args):
#     # args is a list of the command-line arguments (excluding the script name)
#     print("Welcome to the AI chat! Type 'exit' to end the conversation.")

#     while True:
#         human_message = input("You: ")
#         if human_message.lower() == 'exit':
#             print("Goodbye!")
#             break
#         result = agent.invoke(
#             {"messages": [{"role": "user", "content":human_message}]}
#         )
#         if "messages" in result:
#             print (result)
#             response = result["messages"][-1].content if result["messages"] else None
#             print(f"Response: {response}")
#         else:
#             print("Full result:")
#             print(json.dumps(result, indent=2, default=str))


# if __name__ == "__main__":
#     # Pass all arguments *except* the script name to the main function
#     main(sys.argv[1:]) 