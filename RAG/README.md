## RAG (Retrieval-Augmented Generation)

É uma técnica que combina modelos de linguagem com mecanismos de recuperação de informações para melhorar a geração de texto. Por exemplo, caso um modelo treinado não contenha informações específicas sobre determinado tema, a partir do RAG é possível recuperar informações de fontes externas, como documentos ou banco de dados, para fornecer respostas mais precisas e informadas.

### Principais desafios dos LLMs que RAG ajuda a resolver

- **Conhecimento de Domínio (domain knowledge)** - LLMs podem não ter informações específicas de uma área especifica, tornando suas respostas menos precisas.

Com o RAG é possível realizar a integração de dados de um determinado domínio a partir de fontes externas.

- **Alucinações (hallucinations)** - LLMs às vezes geram respostas incorretas ou incoerentes.

Como o RAG utiliza sistemas de recuperação de informações de fontes externas em tempo real, há uma redução na probabilidade de gerar alucinações, com isso a confiabilidade das respostas será maior.

- **Dados de treinamento não são recentes (training data cut off)** - Tem um conhecimento limitado ao período que foram treinados, ignorando eventos ou informações recentes.

O RAG pode buscar informações atualizadas em bases de dados ou na internet, com isso, as respostas sempre estarão atualizadas

### Etapas do REG (pipeline básica)

Primeira etapa: **Indexação dos dados (Data Indexing)**

Constitui um pipeline para ingerir dados de uma fonte e indexá-lo.

O método típico é converter todos os dados privados em embeddings armazenados em um banco de dados vetorial

- 1° Documentos em diversos formatos.
- 2° Data Splitting.
  - Para cada documento é necessário dividir os documentos em partes, pois cada modelo tem seu limite de tokens de entrada (4 mil tokens, 5 mil tokens, etc). Então por conta disso é necessário realizar o "split" (divisão) dos textos de um documento.
- 3° Conversão dos textos em _embeddings_.
  - Transforma os textos em vetores.
- 4° No final, temos um vetor de _embeddings_ (base de dados vetorial com todos os documentos armazenados).

Segunda etapa: **Recuperação de dados e geração das respostas (Data Retrieval e Generation)**

É a chain em si, que processa o pedido do usuário e recupera os dados relevantes do índice (ou da base de dados), depois passando-os para o modelo usar como contexto.

- 1° Usuário faz uma pergunta para a LLM.
- 2° É feita uma consulta à base de dados sendo retornados os principais tópicos.
  - Ao invés de termos a resposta direta da LLM é realizado essa consulta para a resposta ser mais precisa.
- 3° Para gerar a resposta temos a combinação do texto que está na base de dados com o conheicimento que a LLM já possui.
  - No final, esses dados são adicionados no texto final retornado pela LLM.

O LangChain tem vários componentes projetados para ajudar a criar aplicativos de **perguntas e respostas** e aplicativos RAG de modo geral.
