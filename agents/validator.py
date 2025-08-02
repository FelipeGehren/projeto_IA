from langchain.prompts import PromptTemplate
from langchain.schema import HumanMessage
from app.agents.models import llm_gemini_flash
from route_checker import verificar_rota

template = """
Você é um agente inteligente que valida se a pergunta do usuário contém os **filtros obrigatórios** de uma ou mais rotas de uma API.

## Objetivo:
Verificar se todos os campos marcados como `required: true` na especificação OpenAPI das rotas fornecidas estão presentes na pergunta feita pelo usuário.


## Instruções:
1. Analise a(s) rota(s) e identifique os campos marcados como obrigatórios (`required: true`), tanto em `parameters` (query/path/header) quanto em `requestBody`, se aplicável.
2. Verifique se esses campos aparecem na pergunta do usuário.
3. Se **todos os campos obrigatórios estiverem presentes**, retorne:
```json
{{ "validated": true }}
```
4. Se algum campo obrigatório estiver ausente, retorne:
```json
{{
  "validated": false,
  "missing_fields": [
    {{
      "name": "nome_do_campo_faltante",
      "in": "query/path/header/body",
      "required": true,
      "schema": {{ ... }}  // conforme aparece na OpenAPI
    }},
    ...
  ]
}}
```

5. Se não houver nenhum campo obrigatório na rota, retorne:
```json
{{ "validated": true }}
```

### Responda apenas com o JSON final e não inclua explicações adicionais.


Pergunta do usuário: 
{pergunta}

Rotas do sistema:
{rota}
"""

def verificar_filtros(pergunta):
    prompt = PromptTemplate(
        template=template,
        input_variables=["pergunta", "openapi"]
    )

    rota = verificar_rota(pergunta)

    prompt_format = prompt.format(pergunta=pergunta, rota=rota)
    resposta = llm_gemini_flash.invoke([HumanMessage(content=prompt_format)])
    return resposta.content, rota

resposta = verificar_filtros(pergunta="Quantos livros tenho salvos?")
print(resposta)

