from openai_wrapper import OpenAIChatWrapper

if __name__ == "__main__":
    # Replace with your API key
    API_KEY = "your-api-key"

    # Create an instance of the wrapper
    chat_wrapper = OpenAIChatWrapper(key=API_KEY)

    # Prepare messages for the conversation
    messages = [
        {"role": "system", "content": "You are a helpful assistant."},
        {"role": "user", "content": "What is the capital of France?"}
    ]

    functions = [{
        "name": "example_function",
        "description": "An example function to demonstrate function calling.",
        "parameters": {
            "type": "object",
            "properties": {
                "param1": {"type": "string", "description": "The first parameter."},
                "param2": {"type": "integer", "description": "The second parameter."}
            },
            "required": ["param1"]
        }
    }]

    # Get the chat completion response with custom parameters
    response = chat_wrapper.chat_completion(
        messages,
        temperature=0.9,  # Custom temperature
        max_tokens=7,     # Custom max_tokens
        top_p=0.9,        # Custom top_p
        frequency_penalty=0.1,  # Custom frequency_penalty
        presence_penalty=0.2,   # Custom presence_penalty
        stop=["\n"],           # Custom stop sequence
        n=1,                    # Number of completions
        logit_bias={"50256": -100},  # Custom logit bias
        user="test_user",        # Custom user identifier
        timeout=30,                # Custom timeout in seconds
        function_call="auto",     # Enable function calling
        functions=functions
    )

    if response:
        print("Assistant:", response)

