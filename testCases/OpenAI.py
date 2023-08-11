# import openai
#
# openai.api_key = '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'
#
#
# def generate_text(prompt):
#     # Make an API call to GPT-3
#     response = openai.Completion.create(
#         engine="text-davinci-002",  # Replace with the appropriate GPT-3 engine version
#         prompt=prompt,
#         max_tokens=100  # Adjust the length of the generated text as needed
#     )
#
#     # Extract and return the generated text from the response
#     return response['choices'][0]['text']
#
#
# # Example usage
# prompt_text = "Once upon a time"
# generated_text = generate_text(prompt_text)
# print(generated_text)

import openai
import os

from dotenv import load_dotenv, find_dotenv
_ = load_dotenv(find_dotenv())

openai.api_key  = os.getenv('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')