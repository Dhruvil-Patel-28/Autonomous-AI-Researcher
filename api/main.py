from fastapi import FastAPI
from agents.research_agent import run_agent

app = FastAPI()

@app.post("/research")
def research(query: str):

    result = run_agent(query)

    return {"response": result}