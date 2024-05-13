from openai import OpenAI


class ChatOpenAI:
    def __init__(self, model_name, api_key):
        self.model_name = model_name
        self.client = OpenAI(api_key=api_key)

    def call(self, messages):
        stream = self.client.chat.completions.create(
            model=self.model_name,
            messages=[
                {"role": m["role"], "content": m["content"]} for m in messages
            ],
            stream=True
        )
        return stream