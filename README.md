# OpenAI Chat Wrapper

This project is a Python application that provides a simple wrapper around the OpenAI API for generating chat completions. The wrapper is designed to simplify interactions with OpenAI's GPT models by offering customizable parameters and support for advanced features such as function calling.

## Table of Contents

- [Installation](#installation)
- [Usage](#usage)
- [Features](#features)
- [Configuration](#configuration)
- [Project Structure](#project-structure)
- [Example](#example)
- [Testing](#testing)

---

## Installation

### Prerequisites

- Python 3.7+
- `openai` Python package

### Steps

1. **Clone the repository**

   ```bash
   git clone https://github.com/yourusername/openai_chat_wrapper.git


2. Navigate to the project directory

   cd openai_chat_wrapper

3. Install dependencies

   pip install openai

## Usage

1. Initialize the wrapper

from openai_chat_wrapper import OpenAIChatWrapper

API_KEY = "your-api-key"
chat_wrapper = OpenAIChatWrapper(key=API_KEY)

2. Generate chat completions

messages = [
    {"role": "system", "content": "You are a helpful assistant."},
    {"role": "user", "content": "What is the capital of France?"}
]

response = chat_wrapper.chat_completion(messages)
print("Assistant:", response)

3. Customize parameters

response = chat_wrapper.chat_completion(
    messages,
    temperature=0.9,
    max_tokens=50,
    top_p=0.9
)

4. Enable function calling

functions = [{
    "name": "example_function",
    "description": "An example function.",
    "parameters": {
        "type": "object",
        "properties": {
            "param1": {"type": "string"},
            "param2": {"type": "integer"}
        },
        "required": ["param1"]
    }
}]

response = chat_wrapper.chat_completion(
    messages,
    function_call="auto",
    functions=functions
)

### Features

* Simple initialization and configuration.
* Customizable parameters (temperature, max tokens, penalties, etc.).
* Supports function calling for advanced use cases.
* Robust error handling.

### Configuration
Environment Variables
You can optionally configure the API key using environment variables.

Variable	        |    Description
------------------|-----------------------
OPENAI_API_KEY	  |   Your OpenAI API key.


### Project Structure

openai_chat_wrapper/

openai_chat_wrapper/

│
├── openai_chat_wrapper/           # Main application module

│   ├── __init__.py                # Package initializer

│   ├── wrapper.py                 # Core wrapper logic
│

├── example.py                     # Example script demonstrating usage

├── tests/                         # Unit tests

│   ├── test_wrapper.py            # Tests for the wrapper functionality
│

├── README.md                      # Project documentation

├── .gitignore                     # Git ignore rules

├── requirements.txt               # Dependencies



### Example
API Endpoint
This wrapper can also be integrated into a larger application or REST API. Here's a sample request to fetch a chat completion:


{
  "messages": [
    {"role": "user", "content": "What is the capital of France?"}
  ]
}

* Response

{
  "role": "assistant",
  "content": "The capital of France is Paris."
}


### Testing
Running Tests
To ensure the wrapper works correctly:

pytest
