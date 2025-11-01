## Agentes e Tools (ferramentas)

As LLMs encontram dificuldades com determinadas tarefas que envolvem lógica, cálculo matemáticos ou pesquisa. Uma das formas de resolver este problema é integrar a LLM a um conjunto de ferramentas (tools). Esse sistema com a integração é chamada de **Agente LLM**.

Existe uma integração com o ambiente externo, pois o agente usa um motor de raciocínio para determinar quais ações tomar para obter um resultado. Por exemplo, pode ser integrado com os mecanismos de pesquisa da Google e a Wikipedia.

- Os agentes possuem um nível maior de capacidade de raciocínio por terem acesso a ferramentas externas.
- Podem selecionar ferramentas conforme necessário, em uma sequência que considerem adequada.
- O próprio agente pode selecionar a ordem das ações a serem executadas utilizando as ferramentas.

### Ferramentas (tools)

São os principais componentes de agentes que realizam tarefas individuais.

As tools são basicamente apenas métodos/classes aos quais o agente tem acesso que podem fazer coisas como: fazer uma pesquisa na web, interagir com APIs, executar uma consulta em um banco de dados, etc.

Uma coleção de ferramentas no LangChain é chamada de *Toolkit*.

![Toolkit](readme-imgs/image.png)

### Vantagens dos agentes

- **Flexibilidade:** Podem ajustar suas ações com base nos resultados intermediários, ou seja, eles podem ser mais adaptáveis a mudanças no contexto.
- **Raciocínio dinâmico:** Utilizam modelos de linguagem que podem determinar a sequência de ações, o que permite a tomada de decisões em tempo real e maior inteligência nas interações.
- **Manutenção simplificada:** Menos necessidade de codificação manual, pois o modelo de linguagem que vai guiar as ações.
- **Capacidade de interação:** Podem integrar múltiplas ferramentas e fontes de informação, recuperados por meio de diferentes tools.
- **Produção de ações:** Enquanto os modelos de linguagem sozinhos apenas produzem texto, os agentes podem invocar ferramentas e realizar ações com base nas instruções fornecidas pelo modelo.
- **Adequação a tarefas complexas:** São mais eficazes em lidar com interações complexas em contextos mais sensíveis.
- **Realimentação de resultados:** Os resultados das ações podem ser realimentados no modelo para determinar se são necessárias mais ações ou se a tarefa pode ser concluída.

Com isso, podemos concluir que os agentes possuem um mecanismo de raciocínio mais inteligente do que a utilização simples de um modelo de linguagem.