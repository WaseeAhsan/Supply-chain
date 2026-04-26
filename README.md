# AI Supply Chain Orchestrator (ADK + A2A + MCP)

This project is a high-level implementation of an autonomous supply chain management system using Google's **Agent Development Kit (ADK)**. It represents a paradigm shift from simple chatbots to **Micro-Agent Architectures**, where specialized AI entities collaborate across distributed environments to solve complex business logic.

---

## 🏗️ Detailed Project Structure

The project is modularly designed to simulate a real-world enterprise environment where different departments (Inventory, Finance, Logistics) operate as independent services.

```text
supply_chain_project/
├── main.py                 # The Gateway & Orchestrator
│                           # - Houses the SupplyChainOrchestrator
│                           # - Local Inventory & Logistics Agents
├── finance_server.py       # The Remote A2A Service
│                           # - Runs as a standalone FastAPI/Uvicorn server
│                           # - Simulates a secure, cross-departmental API
├── tools_config.yaml       # MCP Metadata Configuration
│                           # - Maps human language to SQL/Database queries
│                           # - Enables "Zero-Code" database integration
├── .env                    # Environment Secrets (API Keys)
├── requirements.txt        # Python dependencies
└── .gitignore              # Ensures security by blocking credential uploads

🌍 Real-Life Problem & Solution
The Problem: The "Human Glue" Requirement
In most current supply chains, different departments use incompatible software. For example:

Warehousing uses a PostgreSQL database.

Finance uses a proprietary ERP with strict manual approval gates.

Logistics uses external carrier APIs (FedEx/UPS).

Currently, humans act as the "glue"—taking data from a database, emailing it to finance for approval, and then manually booking a shipment. This is slow, prone to error, and expensive.

The Solution: Autonomous Micro-Agents
This project eliminates the manual middleman. By using MCP and A2A, the AI can "reach" into the database, "talk" to the finance server, and "negotiate" with the logistics provider automatically.

🛠️ Technological Core: MCP & A2A
1. MCP (Model Context Protocol)
MCP acts as a universal adapter between Large Language Models (LLMs) and data sources.

How it’s used here: The Inventory Agent uses an MCP Toolbox. Instead of the LLM writing fragile SQL code, it simply asks the toolbox to "get stock levels."

The Benefit: If the company switches from PostgreSQL to MongoDB, you only update the MCP config—you don't need to retrain or update the Agent’s logic.

2. A2A (Agent-to-Agent Protocol)
A2A allows AI agents to communicate over standard web protocols (HTTP/JSON).

How it’s used here: The Finance Agent lives on a separate server (finance_server.py). The Orchestrator communicates with it via a well-known agent card.

Human-in-the-Loop: A2A supports "long-running operations." If a purchase is too expensive, the A2A server pauses the automation, asks a human manager for approval, and then resumes the workflow once the manager clicks "Approve."

📖 Real-Life Scenario: "The Critical Stock-Out"
Imagine a car manufacturing plant where a specific part—an Alternator—is running low.

Autonomous Monitoring: The Inventory Agent (via MCP) checks the PostgreSQL database and sees only 5 alternators remain.

Cost Estimation: The agent calculates that ordering a batch of 100 alternators will cost $25,000.

Cross-Department Handoff: The Orchestrator realizes this exceeds the local spending limit. It initiates an A2A call to the Finance Server.

Manager Intervention: The Finance Agent sends a push notification to the CFO: "Urgent: Restock for Alternators needed ($25k). Current stock: 5 units. Approve?"

Workflow Resumption: The CFO approves. The Finance Agent sends a "Success" token back to the Orchestrator.

Logistics Fulfillment: The Logistics Agent automatically queries shipping rates, chooses the "Expedited Air" option, and logs the tracking number into the system.

🚀 Execution Guide
Phase 1: Setup
Install the necessary libraries:

Bash
pip install google-adk uvicorn python-dotenv
Phase 2: Launch the Infrastructure
Start the Finance Department (A2A Server):

Bash
python finance_server.py
This hosts the finance logic on port 8001.

Launch the Supply Chain Brain (Orchestrator):

Bash
python main.py
Phase 3: Test the System
Type the following into the Orchestrator terminal:

"Check the stock for alternators and if we are low, order enough to reach 100 units and get it shipped to our LA warehouse."

The system will then chain the Inventory, Finance, and Logistics agents together to complete the task.


git clone <https://github.com/WaseeAhsan/Supply-chain.git>
