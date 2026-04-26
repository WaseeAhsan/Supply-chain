import os
from dotenv import load_dotenv
from adk import Agent, RemoteA2aAgent, MCPToolbox

load_dotenv()
MODEL = os.getenv("MODEL_NAME")

# 1. Inventory Agent (Uses MCP Toolbox)
inventory_toolbox = MCPToolbox(config_path="tools_config.yaml")
inventory_agent = Agent(
    name="InventoryAgent",
    model=MODEL,
    instructions="Monitor stock and provide item details using the toolbox.",
    tools=[inventory_toolbox]
)

# 2. Logistics Agent
logistics_agent = Agent(
    name="LogisticsAgent",
    model=MODEL,
    instructions="Find shipping options and execute shipments."
)

@logistics_agent.tool
def find_shipping_options(destination: str):
    return ["Standard (5 days) - $800", "Expedited (1 day) - $5000"]

# 3. Finance Agent (Connects to the A2A Server)
# In production, use the actual hosted URL of finance_server.py
finance_remote = RemoteA2aAgent(url="http://localhost:8001")

# 4. Orchestrator
orchestrator = Agent(
    name="SupplyChainOrchestrator",
    model=MODEL,
    instructions="Coordinate between Inventory, Finance, and Logistics to solve supply chain issues.",
    agents=[inventory_agent, logistics_agent, finance_remote]
)

if __name__ == "__main__":
    orchestrator.chat("Check stock for 'alternator' and order 100 units if low.")