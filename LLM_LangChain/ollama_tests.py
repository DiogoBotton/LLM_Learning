# Bibliotecas necessárias:
# - ollama

# Execute o arquivo com python ollama_tests.py

from ollama import chat, ChatResponse

user_text = input("Seu texto: ")

response: ChatResponse = chat(
  model='gemma3:1b', # Modelo baixado e rodando localmente
  messages=[
  {
    'role': 'system',
    'content': "Você é um assistente prestativo e responde a perguntas gerais.",
  },
  {
    'role': 'user',
    'content': user_text,
  },
])

print(response['message']['content'])