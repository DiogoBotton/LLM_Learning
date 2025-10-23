# Bibliotecas necessárias:
# - langchain
# - langchain_ollama

# Execute o arquivo com python ollama_langchain.py

from langchain_ollama import ChatOllama
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import PromptTemplate

# Template para o modelo Phi-3
template = """
<|system|>
  {system_prompt}<|end|>
<|user|>
  {input}<|end|>
<|assistant|>
"""

llm = ChatOllama(
  model="phi3",
  temperature=0.5
)

user_text = input("Seu texto: ")

sys_prompt = "Você é um assistente prestativo e responde a perguntas gerais."

prompt = PromptTemplate.from_template(template.format(system_prompt = sys_prompt, input = user_text))

chain = prompt | llm | StrOutputParser()

res = chain.invoke({"input": user_text})

print(res)

# Exemplo com stream
# for chunk in chain.stream({"input": user_text}):
#   print(chunk, end="", flush=True)