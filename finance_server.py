from adk import Agent, to_a2a
import uvicorn
import os
from dotenv import load_dotenv

load_dotenv()

# Define the Finance Agent
finance_agent = Agent(
    name="FinanceAgent",
    model=os.getenv("MODEL_NAME"),
    instructions="You are a financial officer. Approve orders under $1000 automatically. For orders over $1000, ask for human approval."
)

@finance_agent.tool
def get_approval_threshold():
    return {"threshold": 1000}

# Convert to A2A compatible app
app = to_a2a(finance_agent, port=8001)

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8001)