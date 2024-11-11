from langchain_openai import ChatOpenAI


def creat_llm(model_name="gpt-4o", temperature=0.6):
    model = ChatOpenAI(model=model_name,
                       api_key="sk-edZ3GHEedohbclOl92E142DaC11c40839f4f44Bf59Fe2610",
                       base_url="https://api.gptapi.us/v1/chat/completions",
                       temperature=temperature)
    return model
