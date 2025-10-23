from dotenv import load_dotenv
load_dotenv()

from ollama import chat, ChatResponse

user_text = input("Seu texto: ")

response: ChatResponse = chat(model='gemma3', messages=[
  {
    'role': 'user',
    'content': user_text,
  },
  
])
print(response['message']['content'])