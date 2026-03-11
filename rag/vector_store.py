from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain_community.vectorstores import FAISS

embeddings = HuggingFaceEmbeddings()

vector_store = FAISS.from_texts(
    ["AI agents are autonomous systems that can plan and execute tasks."],
    embeddings
)

def retrieve_docs(query):
    docs = vector_store.similarity_search(query, k=2)
    return "\n".join([d.page_content for d in docs])