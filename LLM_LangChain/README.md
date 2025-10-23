## Passo a passo com Olama

O Ollama é uma ferramenta para utilizar modelos de LLM em máquina local.

- Ollama é uma ferramenta de código aberto que possibilita a execução, criação e compartilhamento dos LLMs diretamente no próprio computador
- Ollama pode ser instalada pelo site ou através de imagens Docker.
- É compatível com sistemas operacionais macOS, Linux e Windows.
- O Ollama pode ser integrado ao LangChain. Primeiramente utilizaremos através da interface do próprio Ollama. Em seguida usaremos pelo LangChain.

Necessário fazer o download do Ollama no link abaixo:
[ollama.com](https://ollama.com/)

Modelos disponíveis no Ollama:

- [https://ollama.com/library](https://ollama.com/library)

Sempre antes de utilizar o modelo é necessário baixá-lo com o comando abaixo:

```bash
ollama run <nome-do-modelo>
ollama run gemma3:1b
```

Será realizado o download do modelo caso ainda não esteja baixado. Caso esteja baixado iniciará uma conversa com o modelo dentro da CLI.
