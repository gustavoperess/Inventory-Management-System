from openai import OpenAI

class GPT_PROMPT:
    def __init__(self, api_key, product):
        self.api_key = api_key
        self.product = product

    def chat_prompt(self):
        client = OpenAI(
            api_key= self.api_key
        )
        prompt = f"Tell me more about {self.product} if this is a fruit, veggie, dairy, meat or seafood give me one receipt for it. .\n\n\n\n\n\n"

        chat_completion = client.chat.completions.create(
            messages=[
                {
                    "role": "user",
                    "content": prompt
                }
            ],
            model="gpt-3.5-turbo"
        )

        return chat_completion.choices[0].message.content