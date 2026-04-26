# AI Supply Chain Agent (ADK + A2A + MCP)

This project is a multi-agent system built with Google's **Agent Development Kit (ADK)**. It automates a supply chain workflow by coordinating specialized agents that communicate via **A2A (Agent-to-Agent)** and **MCP (Model Context Protocol)**.

##  System Architecture
The project consists of an **Orchestrator** and three sub-agents:
1.  **Inventory Agent**: Uses **MCP** to query stock levels from a database.
2.  **Finance Agent**: Hosted as a **Remote A2A Server**; handles budget approvals and human-in-the-loop validation.
3.  **Logistics Agent**: Finds and executes shipping options.

##  Setup & Installation

### 1. Clone the repository
```bash
git clone <your-repo-url>
