import openai

class OpenAIChatWrapper:
    def __init__(self, key=None, model="gpt-4o", temperature=0.7, max_tokens=1000, top_p=1.0, frequency_penalty=0.0, presence_penalty=0.0, stop=None, n=1, logit_bias=None, user=None, timeout=None, function_call=None, functions=None):
        """
        Initialize the wrapper with the API key and default settings.
        """
        self.api_key = key
        if not self.api_key:
            raise ValueError("API key is required. Set it in the environment variable or pass it explicitly.")
        self.model = model
        self.default_temperature = temperature
        self.default_max_tokens = max_tokens
        self.default_top_p = top_p
        self.default_frequency_penalty = frequency_penalty
        self.default_presence_penalty = presence_penalty
        self.default_stop = stop
        self.default_n = n
        self.default_logit_bias = logit_bias
        self.default_user = user
        self.default_timeout = timeout
        self.default_function_call = function_call
        self.default_functions = functions
        openai.api_key = self.api_key

    def chat_completion(self, messages, **kwargs):
        """
        Generate chat completion using OpenAI API.

        Parameters:
        - messages (list): List of messages for the chat.
        - kwargs (dict): Additional optional parameters for customization.

        Returns:
        - str: Response content from the assistant.
        """
        # Set defaults if not provided in kwargs
        kwargs.setdefault("temperature", self.default_temperature)
        kwargs.setdefault("max_tokens", self.default_max_tokens)
        kwargs.setdefault("model", self.model)
        kwargs.setdefault("top_p", self.default_top_p)
        kwargs.setdefault("frequency_penalty", self.default_frequency_penalty)
        kwargs.setdefault("presence_penalty", self.default_presence_penalty)
        kwargs.setdefault("stop", self.default_stop)
        kwargs.setdefault("n", self.default_n)
        kwargs.setdefault("logit_bias", self.default_logit_bias)
        kwargs.setdefault("user", self.default_user)
        kwargs.setdefault("timeout", self.default_timeout)
        kwargs.setdefault("function_call", self.default_function_call)
        kwargs.setdefault("functions", self.default_functions)

        try:
            response = openai.ChatCompletion.create(
                messages=messages,
                **kwargs
            )
            
            return response.choices[0].message.content.strip()
        except Exception as e:
            print(f"An error occurred: {e}")
        return None
