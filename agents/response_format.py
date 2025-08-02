from langchain.prompts import PromptTemplate
from langchain.schema import HumanMessage
from app.agents.models import llm_gemini_flash
from validator import verificar_filtros
import requests

template = """
Você é um agente cujo trabalho é receber uma pergunta que o usuário fez, receber os dados que estão associados à pergunta dele num formato json e formatar um texto sucinto, mas explicativo e humanizado, referente aos dados desse json. 

Observações gerias: Seja mais direto e sem muito exagero na sua resposta.
Atenção: Retire todo e qualquer markdown que vier na resposta, deixe apenas texto cru.

Aqui está o que ele perguntou:
{pergunta}
Aqui está a resposta:
{resultado}
"""

def executar_rota(rota):
    path_para_execucao = rota[0]['path']

    resultado_api = requests.get(f"http:/127.0.0.1:5000{path_para_execucao}")
    return resultado_api


def gerar_resposta(pergunta):
    prompt = PromptTemplate(
        template=template,
        input_variables=["pergunta", "resultado"]
    )

    validacao, rota =  verificar_filtros(pergunta)

    if validacao['validated'] == False:
        ...

    resultado_api = executar_rota(rota=rota)
  
    prompt_format = prompt.format(pergunta=pergunta, resultado=resultado_api)
    resposta = llm_gemini_flash.invoke([HumanMessage(content=prompt_format)])

    return resposta.content