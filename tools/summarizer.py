from utils.llm import get_llm

llm = get_llm()

def summarize(text: str):

    prompt = f"""
    Summarize the following research information clearly:

    {text}
    """

    return llm.invoke(prompt).content