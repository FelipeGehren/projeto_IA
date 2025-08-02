from langchain.prompts import PromptTemplate
from langchain.schema import HumanMessage
from app.agents.models import llm_gemini_flash

template = """

Você é um agente especialista em APIs REST e OpenAPI. Sua tarefa é analisar a pergunta do usuário e identificar as rotas da API mais relevantes para responder à solicitação.

Você receberá:
- A pergunta do usuário
- A especificação da API no formato OpenAPI 3.0 (em YAML ou JSON)

Com base nisso, você deve identificar:
1. Quais endpoints da API são mais adequados para atender à solicitação
2. Quais parâmetros devem ser informados (query, path, headers, body, etc)
3. Qual o método HTTP apropriado (GET, POST, PUT, DELETE, etc)

Sua resposta deve ser estritamente no seguinte formato JSON:

```json
[
  {{
    "path": "/exemplo/de/rota",
    "method": "GET",
    "description": "Descrição da finalidade da rota",
    "parameters": [
      {{
        "name": "param1",
        "in": "query",
        "required": true,
        "type": "string",
        "description": "Descrição do parâmetro"
      }},
      {{
        "name": "id",
        "in": "path",
        "required": true,
        "type": "integer",
        "description": "ID do recurso"
      }}
    ],
    "requestBody": {{
      "required": true,
      "content": {{
        "application/json": {{
          "schema": {{
            "field1": "string",
            "field2": "integer"
          }}
        }}
      }}
    }}
  }}
]
```


Pergunta do usuário:
{pergunta}

Documentação Openapi:
{openapi}



Retorne apenas o JSON solicitado.

"""

def verificar_rota(pergunta):
    prompt = PromptTemplate(
        template=template,
        input_variables=["pergunta", "openapi"]
    )

    with open('openapi.json', 'r', encoding='utf-8') as file:
        openapi = file.read()


    prompt_format = prompt.format(pergunta=pergunta, openapi=openapi)
    resposta = llm_gemini_flash.invoke([HumanMessage(content=prompt_format)])
    return resposta.content
